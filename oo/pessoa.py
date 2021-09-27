class Pessoa:
    olhos = 2

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
    marcos.sobrenome = 'Silva'
    del marcos.filhos
    marcos.olhos = 1
    print(marcos.__dict__)
    print(edipo.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(edipo.olhos)
    print(marcos.olhos)
    print(id(Pessoa.olhos), id(marcos.olhos), id(edipo.olhos))


