class Perfil(object):
    def __init__(self, nome, telefone, empresa):
        self.nome = nome
        self.telefone = telefone
        self.empresa = empresa
        self.curtidas = 0
    def imprimir(self):
        print(f"\nNome : {self.nome}, Telefone: {self.telefone}, Empresa {self.empresa}, Curtidas: {self.curtidas}")

perfilVip = Perfil("Dumal", "Não informado", "Nike")
perfilVip.imprimir()
perfilVip.curtidas+=1
perfilVip.curtidas+=1
perfilVip.curtidas+=1
perfilVip.curtidas+=1
perfilVip.curtidas+=1
print("\n\nsegundo print")
perfilVip.imprimir()
print("\n\nterceiro print")
perfilVip.curtidas = 1000
perfilVip.imprimir()
