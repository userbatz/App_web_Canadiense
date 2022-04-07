# PASO 1: AGREGAR LAS LIBRERIAS QUE SE UTILIZARAN EN EL PROYECTO.
from flask import Flask, json, jsonify
from flask_cors import CORS
from flask import request
from CRUD_usuarios import CRUD_Usuarios


#INICIALIZANDO NUESTRO SERVIDOR.
crudUsuario = CRUD_Usuarios()


app = Flask(__name__)
CORS(app)

#PETICIONES HTTP: GET, POST, DELETE, PUT
# GET = OBTENER INFORMACIÓN.
#POST = ENVIAR INFORMACION.
#DELETE = ELIMINAR INFORMACION.
#PUT =  MODIFICAR LA INFORMACION.

#CRUD: las funciones básicas de un programa.
#CREATE, READ, UPDATE, DELETE.



#RUTAS........ ROUTERS
# RUTA PRINCIPAL: 
@app.route('/', methods=["GET"] )
def Inicial():
    print('hola soy la pagina inicial...')   #mensaje que se verá en consola
    return jsonify({"MENSAJE": "BIENVENIDO", "NOMBRE": "GERSON"}) #mensaje se verá en el navegador



#RUTA PARA INGRESAR AL METODO DE CREAR USUARIO:
@app.route('/usuario', methods=["POST"])
def crearUsuario():
    nombre = request.json["nombre"] #En este espacio estamos leyendo lo que el cliente envía en formato JSON
    correo = request.json["correo"]
    pwd = request.json["pwd"]
    edad = request.json["edad"]
    res = crudUsuario.CreateUser(nombre,correo,pwd,edad)
    return jsonify({"mensaje": "usuario registrado correctamente"})













#INDICAR PUERTO DE SALIDA.
if __name__=='__main__':
    app.run(debug=True, port=3000)

    