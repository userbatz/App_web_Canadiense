class Usuario:

    #PARA LA CLASE USUARIO ESTAREMOS GUARDANDO LOS SIGUIENTES DATOS:
    #ID, CORREO,PASSWORD,NOMBRE,EDAD

    #CONSTRUCTOR.
    def __init__(self, id,correo,pwd,nombre,edad):
        self.id = id
        self.correo = correo
        self.pwd = pwd
        self.nombre = nombre
        self.edad = edad
    
    #CREACION DE METODOS PARA EL PRUEBA DEL MOSTRADO DE DATOS Y PARA RETORNAR VALORES.

    #funcion de prueba.
    def saludar(self):
        print("hola mi nombre es: " + self.nombre + " Y TENGO : "+ self.edad)


    #funcion de retorno:
    def dump(self):
        return {
            "id": self.id,
            "correo": self.correo,
            "pwd": self.pwd,
            "nombre": self.nombre,
            "edad": self.edad
        }
        
