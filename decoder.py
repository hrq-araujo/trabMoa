from brkga_mp_ipr.types import BaseChromosome

class TrabDecoder:
    """
    Dado um cromossomo (vetor de chaves aleatórias), seleciona as d colunas com menor valor de chave e calcula quantas linhas são cobertas.
    """
    def __init__(self, m, n, d, A):
        self.m = m  # número de linhas
        self.n = n  # número de colunas
        self.d = d  # número máximo de colunas a escolher
        self.A = A  # matriz de cobertura A[m][n]

    def decode(self, chromosome: BaseChromosome, rewrite: bool) -> float:
        # Seleciona os índices das d menores chaves
        selected = sorted(range(self.n), key=lambda i: chromosome[i])[:self.d]

        covered = set()
        for j in selected:
            for i in range(self.m):
                if self.A[i][j] == 1:
                    covered.add(i)

        return float(len(covered))  # fitness = número de linhas cobertas
