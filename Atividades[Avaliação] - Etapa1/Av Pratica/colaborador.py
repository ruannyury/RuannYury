from movimento_folha import MovimentoFolha


class Colaborador:
    def __init__(self, codigo, nome, endereco, telefone, bairro, cep, cpf, salario_atual):
        self._codigo = codigo
        self._nome = nome
        self._endereco = endereco
        self._telefone = telefone
        self._bairro = bairro
        self._cep = cep
        self._cpf = cpf
        self._salario_atual = salario_atual
        self._movimentos = []

    def inserir_movimentos1(self, movimento):
        if isinstance(movimento, MovimentoFolha):
            self._movimentos.append(movimento)

    def separar_movimentos(self):
        proventos = {}
        descontos = {}
        for movimento in self._movimentos:
            if movimento.get_tipo_movimento == "Provento":
                proventos[movimento.get_descricao] = movimento.get_valor
            elif movimento.get_tipo_movimento == "Desconto":
                descontos[movimento.get_descricao] = movimento.get_valor
        return proventos, descontos

    def calcular_salario(self, folha_pag):
        total_proventos, total_descontos, salario = folha_pag.infos_colaborador(self._codigo)
        folha_completa = "\nCódigo: {}\nNome: {}" \
                         "\nSalário Antigo: {}\nSalário Atual: {}" \
                         "\nTotal Proventos: {}\nTotal Descontos: {}" \
                         "\nValor Líquido a Receber: {}".format(self._codigo,
                                                                self._nome,
                                                                self._salario_atual,
                                                                salario,
                                                                total_proventos,
                                                                total_descontos,
                                                                total_proventos - total_descontos,
                                                                )

        proventos, descontos = self.separar_movimentos()
        folha_completa += "{:>8}DESCRIÇÃO{:>15}VALOR{:>15}TIPO\n".format("", "", "")
        for provento in proventos:
            folha_completa += "{:>15}:{:>15}{:>7}{:>15}-PROVENTO\n".format(provento, "",
                                                                           proventos[provento], "")

        for desconto in descontos:
            folha_completa += "{:>15}:{:>15}{:>7}{:>15}-DESCONTO\n".format(desconto, "",
                                                                           descontos[desconto], "")

        return folha_completa
