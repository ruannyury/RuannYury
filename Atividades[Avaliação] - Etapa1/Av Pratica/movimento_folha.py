from tipomovimento import TipoMovimento


class MovimentoFolha:
    def __init__(self, cod_colaborador, descricao, valor, tipo_movimento):
        self._descricao = descricao
        self._valor = valor
        self._cod_colaborador = cod_colaborador
        self._tipo_movimento = self.qual_tipo_movimento(tipo_movimento)

    @property
    def get_descricao(self):
        return self._descricao

    @property
    def get_valor(self):
        return self._valor

    @property
    def get_cod_colaborador(self):
        return self._cod_colaborador

    @staticmethod
    def qual_tipo_movimento(tipo_mov):
        if tipo_mov == 'P':
            return TipoMovimento.P.value

        elif tipo_mov == 'D':
            return TipoMovimento.D.value

        else:
            return 'Inválido.'

    @property
    def get_tipo_movimento(self):
        return self._tipo_movimento
