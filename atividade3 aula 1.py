class Perfil(object):
    def __init__(self, nome, telefone, empresa):
        self.__nome = nome
        self.__telefone = telefone
        self.__empresa = empresa
        self.__curtidas = 0
    def imprimir(self):
        print(f"\nNome : {self.__nome}, Telefone: {self.__telefone}, Empresa {self.__empresa}")
    def somarCurtidas(self):
        self.__curtidas+=1
    def get_nome(self):
        return self.__nome
    def set_nome(self, novoNome):
        self.__nome = novoNome

perfilVip = Perfil("Dumal", "Não informado", "Nike")
nomeAreaMaster = perfilVip.get_nome()
nomeAreaMaster+= " Silva"
perfilVip.set_nome("Carlinhos")
print(perfilVip.get_nome())





