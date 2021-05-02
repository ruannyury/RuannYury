def verificacao(a, b, c):
    """
    Verifica a possibilidade de se formar um triângulo com os lados inseridos.
    """
    if a <= 0 or b <= 0 or c <= 0:  # Os lados não podem ser negativos, obviamente
        return False
    else:
        if a < b + c and b < a + c and c < a + b:  # Condições de existência para o triângulo
            return True
        return False
