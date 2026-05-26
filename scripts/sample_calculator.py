"""
sample_calculator.py — calculadora de tamanho de amostra para auditoria

Dois métodos:
  - Atribuição de atributos (compliance / ToE binário)
  - MUS — Monetary Unit Sampling (saldos monetários)

Uso:
    python3 sample_calculator.py attribute --population 500 --er 0.05 --tr 0.10
    python3 sample_calculator.py mus --population-value 10000000 --materiality 300000 --er 0.05
"""

import argparse
import math


# ─── Attribute Sampling ───────────────────────────────────────────────────────

_ATTR_CONFIDENCE = {
    0.90: {0: 2.31, 1: 3.89, 2: 5.33, 3: 6.69, 4: 8.00},
    0.95: {0: 3.00, 1: 4.75, 2: 6.30, 3: 7.76, 4: 9.16},
    0.99: {0: 4.61, 1: 6.64, 2: 8.41, 3: 10.05, 4: 11.61},
}


def attribute_sample(
    population: int,
    expected_rate: float,
    tolerable_rate: float,
    confidence: float = 0.95,
    max_errors: int = 0,
) -> dict:
    """
    population      — número de itens na população
    expected_rate   — taxa de erro esperada (0.0–1.0)
    tolerable_rate  — taxa de erro tolerável (risco de controle)
    confidence      — nível de confiança (0.90 / 0.95 / 0.99)
    max_errors      — máximo de erros esperados na amostra
    """
    factors = _ATTR_CONFIDENCE.get(confidence)
    if factors is None:
        raise ValueError(f"Confiança deve ser 0.90, 0.95 ou 0.99. Recebido: {confidence}")
    if max_errors not in factors:
        raise ValueError(f"max_errors deve ser 0–4. Recebido: {max_errors}")

    cf = factors[max_errors]
    if tolerable_rate <= 0:
        raise ValueError("tolerable_rate deve ser > 0")

    n_unlimited = math.ceil(cf / tolerable_rate)

    if population > 0:
        n = math.ceil(n_unlimited / (1 + n_unlimited / population))
    else:
        n = n_unlimited

    precision = tolerable_rate - expected_rate

    return {
        "método": "Atribuição de Atributos",
        "população": population,
        "taxa_esperada": f"{expected_rate:.1%}",
        "taxa_tolerável": f"{tolerable_rate:.1%}",
        "precisão": f"{precision:.1%}",
        "confiança": f"{confidence:.0%}",
        "max_erros_permitidos": max_errors,
        "fator_confiança": cf,
        "n_sem_ajuste": n_unlimited,
        "n_ajustado": n,
        "interpretação": (
            f"Testar {n} itens. Se {max_errors} ou menos erros → controle efetivo. "
            f"Se mais → inefetivo."
        ),
    }


# ─── MUS — Monetary Unit Sampling ────────────────────────────────────────────

def mus_sample(
    population_value: float,
    materiality: float,
    expected_error: float = 0.0,
    confidence: float = 0.95,
) -> dict:
    """
    population_value  — valor total da população (R$)
    materiality       — materialidade de performance (R$)
    expected_error    — erro esperado total (R$)
    confidence        — nível de confiança (0.90 / 0.95)
    """
    rf_map = {0.90: 2.31, 0.95: 3.00, 0.99: 4.61}
    rf = rf_map.get(confidence)
    if rf is None:
        raise ValueError(f"Confiança deve ser 0.90, 0.95 ou 0.99. Recebido: {confidence}")

    if materiality <= 0:
        raise ValueError("materiality deve ser > 0")

    ef = 1.0
    if expected_error > 0:
        ratio = expected_error / materiality
        if ratio >= 1.0:
            raise ValueError("expected_error deve ser < materiality")
        ef = 1 / (1 - ratio * (1 - 1 / rf))

    interval = materiality / rf / ef
    n = math.ceil(population_value / interval)

    return {
        "método": "MUS — Monetary Unit Sampling",
        "valor_população": f"R$ {population_value:,.2f}",
        "materialidade": f"R$ {materiality:,.2f}",
        "erro_esperado": f"R$ {expected_error:,.2f}",
        "confiança": f"{confidence:.0%}",
        "fator_confiança_RF": rf,
        "fator_expansão": round(ef, 4),
        "intervalo_seleção": f"R$ {interval:,.2f}",
        "n_amostra": n,
        "interpretação": (
            f"Selecionar {n} itens com intervalo de R$ {interval:,.0f}. "
            f"Se erro projetado < R$ {materiality:,.0f} → saldo auditável sem ajuste."
        ),
    }


# ─── CLI ─────────────────────────────────────────────────────────────────────

def _print_result(result: dict):
    print()
    for k, v in result.items():
        label = k.replace("_", " ").capitalize()
        print(f"  {label:<28} {v}")
    print()


def main():
    parser = argparse.ArgumentParser(
        description="Calculadora de tamanho de amostra para auditoria"
    )
    sub = parser.add_subparsers(dest="method", required=True)

    pa = sub.add_parser("attribute", help="Amostragem por atributos (ToE binário)")
    pa.add_argument("--population",  type=int,   required=True)
    pa.add_argument("--er",          type=float, required=True,  help="Taxa de erro esperada (0.0–1.0)")
    pa.add_argument("--tr",          type=float, required=True,  help="Taxa de erro tolerável (0.0–1.0)")
    pa.add_argument("--confidence",  type=float, default=0.95,   help="0.90 / 0.95 / 0.99")
    pa.add_argument("--max-errors",  type=int,   default=0,      help="Máximo de erros permitidos (0–4)")

    pm = sub.add_parser("mus", help="Monetary Unit Sampling")
    pm.add_argument("--population-value", type=float, required=True)
    pm.add_argument("--materiality",      type=float, required=True)
    pm.add_argument("--er",               type=float, default=0.0,  help="Erro esperado em R$")
    pm.add_argument("--confidence",       type=float, default=0.95)

    args = parser.parse_args()

    if args.method == "attribute":
        result = attribute_sample(
            population=args.population,
            expected_rate=args.er,
            tolerable_rate=args.tr,
            confidence=args.confidence,
            max_errors=args.max_errors,
        )
    else:
        result = mus_sample(
            population_value=args.population_value,
            materiality=args.materiality,
            expected_error=args.er,
            confidence=args.confidence,
        )

    _print_result(result)


if __name__ == "__main__":
    main()
