class Pessoa:
    def __init__(self, *filhos, nome=None, idade=33):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá{id(self)}'

if __name__ == '__main__':
    edipo = Pessoa(nome='Édipo')
    marcos = Pessoa(edipo, nome='Marcos')
    print(Pessoa.cumprimentar(marcos))
    print(id(marcos))
    print(marcos.cumprimentar())
    print(marcos.nome)
    print(marcos.idade)
    for filho in marcos.filhos:
        print(filho.nome)