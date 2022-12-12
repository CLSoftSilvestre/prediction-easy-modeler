class tarefa():
    def __init__(self,id=0,descricao="",estado=0,url=""):
        self.id=id
        self.descricao=descricao
        self.estado=estado
        self.url=url

    @staticmethod
    def GetAll():
        lst=[]
        lst.append(tarefa(1,"Enviar email"))
        lst.append(tarefa(2,"Telefonar"))
        lst.append(tarefa(3,"Enviar avaliacao"))

        return lst