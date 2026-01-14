import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


# =========================
# Configurações do projeto
# =========================
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "desperdicio_operacional.csv"
OUTPUT_DIR = BASE_DIR / "output"

OUTPUT_DIR.mkdir(exist_ok=True)


# =========================
# Funções
# =========================
def carregar_dados(caminho_csv: Path) -> pd.DataFrame:
    """Carrega os dados operacionais do arquivo CSV."""
    df = pd.read_csv(caminho_csv)
    df["data"] = pd.to_datetime(df["data"])
    return df


def preparar_dados(df: pd.DataFrame) -> pd.DataFrame:
    """Cria métricas de desperdício e custo."""
    df = df.copy()
    df["taxa_desperdicio"] = (
        df["quantidade_descartada"] / df["quantidade_comprada"]
    )
    df["custo_desperdicio"] = (
        df["quantidade_descartada"] * df["custo_unitario"]
    )
    return df


def analise_por_material(df: pd.DataFrame) -> pd.Series:
    """Retorna o custo total de desperdício por material."""
    return (
        df.groupby("material")["custo_desperdicio"]
        .sum()
        .sort_values(ascending=False)
    )


def analise_por_setor(df: pd.DataFrame) -> pd.Series:
    """Retorna o custo total de desperdício por setor."""
    return df.groupby("setor")["custo_desperdicio"].sum()


def analise_mensal(df: pd.DataFrame) -> pd.Series:
    """Retorna o custo de desperdício por mês."""
    df = df.copy()
    df["mes"] = df["data"].dt.to_period("M")
    return df.groupby("mes")["custo_desperdicio"].sum()


def simular_reducao(df: pd.DataFrame, percentual: float = 0.3) -> float:
    """
    Simula a redução de desperdício nos materiais mais críticos.
    Retorna o percentual de redução obtido.
    """
    custo_atual = df["custo_desperdicio"].sum()

    desperdicio_material = analise_por_material(df)
    materiais_criticos = desperdicio_material.head(3).index

    df_simulado = df.copy()
    df_simulado.loc[
        df_simulado["material"].isin(materiais_criticos),
        "custo_desperdicio"
    ] *= (1 - percentual)

    custo_simulado = df_simulado["custo_desperdicio"].sum()

    reducao = (custo_atual - custo_simulado) / custo_atual * 100
    return reducao


# =========================
# Gráficos
# =========================
def gerar_grafico_barra(serie: pd.Series, titulo: str, nome_arquivo: str):
    serie.plot(kind="bar")
    plt.title(titulo)
    plt.ylabel("Custo (R$)")
    plt.xlabel("")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / nome_arquivo)
    plt.close()


def gerar_grafico_linha(serie: pd.Series, titulo: str, nome_arquivo: str):
    serie.plot(kind="line", marker="o")
    plt.title(titulo)
    plt.ylabel("Custo (R$)")
    plt.xlabel("Período")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / nome_arquivo)
    plt.close()


def gerar_grafico_pizza(serie: pd.Series, titulo: str, nome_arquivo: str):
    serie.plot(kind="pie", autopct="%1.1f%%")
    plt.title(titulo)
    plt.ylabel("")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / nome_arquivo)
    plt.close()


# =========================
# Execução principal
# =========================
def main():
    df = carregar_dados(DATA_PATH)
    df = preparar_dados(df)

    # Análises
    desperdicio_material = analise_por_material(df)
    desperdicio_setor = analise_por_setor(df)
    desperdicio_mensal = analise_mensal(df)

    # Gráficos
    gerar_grafico_barra(
        desperdicio_material,
        "Custo de Desperdício por Material",
        "desperdicio_por_material.png"
    )

    gerar_grafico_pizza(
        desperdicio_setor,
        "Distribuição do Desperdício por Setor",
        "desperdicio_por_setor.png"
    )

    gerar_grafico_linha(
        desperdicio_mensal,
        "Evolução Mensal do Desperdício",
        "desperdicio_mensal.png"
    )

    # Simulação
    reducao = simular_reducao(df)

    print("=== Relatório de Análise de Desperdício ===")
    print(f"Custo total desperdiçado: R$ {df['custo_desperdicio'].sum():.2f}")
    print(f"Redução estimada após otimizações: {reducao:.2f}%")


if __name__ == "__main__":
    main()
