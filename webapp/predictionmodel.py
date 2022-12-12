from webapp.utilsdb import Utils

class PredictionModel:
    def __init__(self, id=0, description="",state=0):
        self.Id=id
        self.Description = description
        self.State = state

    def Insert(self):
        sql="UPDATE Model set Descr='{1}',Stat={2} WHERE ModelId={0}"
        sql = sql.format(self.Id,self.Description,self.State)
      
        return Utils.ExecutaComandoSQL(sql)
    
    def Update(self):
        sql="UPDATE Model set Descr='{1}',Stat={2} WHERE ModelId={0}"
        sql = sql.format(self.Id,self.Description,self.State)
      
        return Utils.ExecutaComandoSQL(sql)

    @staticmethod
    def Delete(id):
        sql="DELETE FROM Model WHERE ModelId={0}"
        sql = sql.format(id)
      
        return Utils.ExecutaComandoSQL(sql)

    @staticmethod
    def GetAll():
        lst = []
        sql="SELECT * FROM Model"
        
        for id,desc,state in Utils.ExecutaConsultaMySQL(sql):
            model = PredictionModel(id,desc,state)
            lst.append(model)
        
        return lst
    
    def Get(self,id):
        
        sql="SELECT * FROM Model WHERE ModelId={0}"
        sql = sql.format(id)
        
        try:    
            for id,desc,state in Utils.ExecutaConsultaSQL(sql):
                self.Id = id
                self.Description = desc
                self.State = state
        except:
            print("not found")