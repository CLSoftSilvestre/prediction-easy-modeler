import pyodbc
import pymysql

class Utils:
    @staticmethod
    def ExecutaComandoSQL(sql):
        resultado=0
        cs="""DRIVER={MySQL ODBC 5.1 Driver};
        USER=root;PASSWORD=admins;
        SERVER=mysqldb;
        DATABASE=tarefasdb;
        PORT=3306"""
        try:
            conn= pyodbc.connect(cs)
            cursor = conn.cursor()
            cursor.execute(sql)
            resultado=cursor.rowcount
            conn.commit()
            print("resultado=",resultado)
        except  pyodbc.Error as erro:
            print(erro)
        finally:
            pass
            #cursor.close()
            #conn.close()
        return resultado
    @staticmethod
    def ExecutaConsultaSQL(sql):
        resultado=[]
        cs="""DRIVER={MySQL ODBC 5.1 Driver};
        USER=root;PASSWORD=admins;
        SERVER=mysqldb;
        DATABASE=tarefasdb;
        PORT=3306"""
        try:
            conn= pyodbc.connect(cs)
            cursor = conn.cursor()
            registos = cursor.execute(sql)
            resultado = registos.fetchall()
            
            conn.commit()
            print("resultado=",resultado)
        except  pyodbc.Error as erro:
            print(erro)
        finally:
            pass
            #cursor.close()
            #conn.close()
        return resultado
    @staticmethod
    def ExecutaComandoMySQL(sql):
        resultado=0
        # Connect to the database
        connection = pymysql.connect(host='mysqldb',
                             user='root',
                             password='admins',
                             database='tarefasdb',
                             cursorclass=pymysql.cursors.DictCursor)
        try:
            with connection:
                with connection.cursor() as cursor:
                    cursor.execute(sql)
                    connection.commit()
        except  pyodbc.Error as erro:
            print(erro)
        finally:
            pass
        return resultado
    @staticmethod
    def ExecutaConsultaMySQL(sql):
        resultado=[]
        
        try:
            # Connect to the database
            connection = pymysql.connect(host='mysqldb',
                             user='root',
                             password='admins',
                             database='tarefasdb',
                             cursorclass=pymysql.cursors.DictCursor)
            with connection:
                with connection.cursor() as cursor:
                    # Read a single record
                    cursor.execute(sql)
                    #result = cursor.fetchall()
                    resultado = cursor.fetchall()
                    print(resultado)
        except  pyodbc.Error as erro:
            print(erro)
        finally:
            pass
        return resultado  