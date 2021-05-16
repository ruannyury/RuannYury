"""
    Módulo notafiscal -
    Classe NotaFiscal -
        Atributos :
            id        - informado.
            codigo    - informado.
            data      - informado.
            cliente   - informado.
            itens     - informado
            valornota - calculado.
"""
import datetime
from cliente import Cliente
from itemnotafiscal import ItemNotaFiscal


class NotaFiscal:
    def __init__(self, id3, codigo, cliente):
        self._Id = id3
        self._codigo = codigo
        self._cliente = cliente
        self._data = datetime.datetime.now()
        self._itens = []
        self._valorNota = 0.0

    def set_cliente(self, cliente):
        if isinstance(cliente, Cliente):
            self._cliente = cliente

    def data_nota(self):
        lista_data_e_hora = str(self._data).split()  # Separa o resultado de "datetime.datetime.now()" numa lista
        # com 2 elementos, a data e a hora
        data_lista = lista_data_e_hora[0].split('-')  # Divide em strings apenas a data, primeiro elemento da lista
        # acima
        data_final_nota = f'{data_lista[2]}/{data_lista[1]}/{data_lista[0]}'  # Ordena a data na nossa ordem padrão
        return data_final_nota  # Retorna a data formatada

    def adicionar_item(self, item):
        if isinstance(item, ItemNotaFiscal):
            self._itens.append(item)

    def calcular_total_nota(self):
        valor = 0.0
        for item in self._itens:
            valor = valor + item.get_valor_item()
        self._valorNota = valor

    def get_valor_nota(self):
        return self._valorNota

    def imprimir_nota_fiscal(self):
        """
        Formatação final da nota fiscal, a string completa de saída. Método principal do programa.
        """
        linhas = '-' * 111

        formatacao_nota = '{}\n' \
                          'NOTA FISCAL{:>100}\n' \
                          'Cliente:{:>6}{:>4}Nome: {}\n' \
                          'CPF/CNPJ: {}\n' \
                          '{}\n' \
                          'ITENS\n' \
                          '{}\n' \
                          'Seq{:>3}Descricao{:>52}QTD{:>7}Valor Unit{:19}Preço\n' \
                          '{}  {}    {}     {}     {}'.format(linhas,
                                                              self.data_nota(),
                                                              self._cliente.get_codigo(), ' ', self._cliente.get_nome(),
                                                              self._cliente.get_cnpjcpf(),
                                                              linhas,
                                                              linhas,
                                                              ' ', ' ', ' ', ' ',
                                                              '-' * 4, '-' * 56, '-' * 5, '-' * 12, '-' * 18)

        if len(self._itens) > 0:  # Adicionando e formatando os itens, elementos finais da nota
            for item_nota in self._itens:
                formatacao_nota += '\n\n{}{:>3}{}'.format(item_nota.get_sequencial(), ' ', item_nota.get_descricao())
                formatacao_nota += ' ' * (60 - len(item_nota.get_descricao()))  # Controlando de acordo com a descrição
                '''formatacao_nota += '{:>5}{:>17.2}{:>23.2}'.format(item_nota.get_quantidade(),
                                                                  item_nota.get_valor_unitario(),
                                                                  item_nota.get_valor_item())'''
                formatacao_nota += '{:.2f}             {:.2f}                  {:.2f}'.format(
                    item_nota.get_quantidade(), item_nota.get_valor_unitario(),
                    item_nota.get_valor_item())

        formatacao_nota += '\n%s\nValor Total: %.2f' % (linhas, self._valorNota)
        print(formatacao_nota)
