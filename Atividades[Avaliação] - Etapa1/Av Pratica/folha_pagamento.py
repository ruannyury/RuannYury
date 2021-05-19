from movimento_folha import MovimentoFolha

COLABORADORES = set()


class FolhaPagamento:
    def __init__(self, mes, ano, total_descontos=0, total_proventos=0):
        self._mes = mes
        self._ano = int(ano)
        self._total_descontos = total_descontos
        self._total_proventos = total_proventos
        self._movimentos = []

    # Inserir todos os objetos do tipo MovimentoFolha na lista movimentos do objeto FP:
    def inserir_movimentos(self, movimento):
        if isinstance(movimento, MovimentoFolha):
            self._movimentos.append(movimento)
            self.inserir_colaboradores(movimento.get_cod_colaborador)

    @staticmethod
    def inserir_colaboradores(cod_colaborador):
        COLABORADORES.add(cod_colaborador)

    def infos_colaborador(self, cod_colaborador):
        total_descontos = 0
        total_proventos = 0
        salario_atual = 0
        for movimento in self._movimentos:
            if movimento.get_cod_colaborador == cod_colaborador:
                if movimento.get_qual_tipo_movimento == 'Desconto':
                    total_proventos += movimento.get_valor
                elif movimento.get_qual_tipo_movimento == 'Desconto':
                    total_descontos += movimento.get_valor
                if movimento.get_descricao == 'Salario':
                    salario_atual = movimento.get_valor

        return total_proventos, total_descontos, salario_atual

    def infos_folha_pag(self):
        total_descontos = 0
        total_proventos = 0
        total_salarios = 0
        for colab in COLABORADORES:
            provent, descont, salario = self.infos_colaborador(colab)
            total_descontos += descont
            total_proventos += provent
            total_salarios += salario
        return total_proventos, total_descontos, total_salarios

    def calcular_folha(self):
        total_proventos, total_descontos, total_salarios = self.infos_folha_pag()
        total_a_pagar = total_proventos - total_descontos
        str_ = "Total de salários atual = {} \nTotal de Proventos= {}" \
               "\nTotal de Descontos = {}\nTotal a Pagar = {}\n".format(total_salarios,
                                                                        total_proventos,
                                                                        total_descontos,
                                                                        total_a_pagar)

        return str_
