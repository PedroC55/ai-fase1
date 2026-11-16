def soma(a: int, b: int) -> int:
    return a + b


def media(valores: list[float]) -> float:
    if not valores:
        raise ValueError("lista vazia")
    return sum(valores) / len(valores)
