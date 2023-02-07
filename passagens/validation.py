def origem_destino_iguais(origem, destino, lista_de_erros):
    if origem == destino:
        lista_de_erros['destino'] = 'Origem e destino não podem ser iguais'

def campo_numerico(valor_campo, nome_campo, lista_de_erros):
    if any(char.isdigit() for char in valor_campo):
        lista_de_erros[nome_campo] = 'Não inclua números neste campo'

