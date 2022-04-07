#importando la clase del constructor de usuarios.
from usuario import Usuario


#INICIAR LA CLASE DEL CRUD:
class CRUD_Usuarios:

    #MINI CONSTRUCTOR
    def __init__(self):

        #creando un verctor para guardar a los usuarios. simulando una base de datos.
        self.usuarios = []


    #METODO PARA CREAR USUARIOS.
    def CreateUser(self, nombre,correo,pwd,edad):
        id = len(self.usuarios)
        nuevoUsuario = Usuario(id,correo,pwd,nombre,edad)
        self.usuarios.append(nuevoUsuario)
        return nuevoUsuario.dump()