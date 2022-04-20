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


#RUTA PARA MOSTRAR TODOS USUARIOS REGISTRADOS DENTRO DEL SISTEMA
@app.route('/usuario', methods=["GET"])
def getUsuarios():
    return jsonify({"datos": crudUsuario.readUsers()})


#RUTA PARA ACTUALIZAR LOS USUARIOS MEDIANTE EL ID.
@app.route('/usuario', methods=["PUT"])
def updateUsuario():
    id_u = request.json["id"]
    nombre = request.json["nombre"] 
    correo = request.json["correo"]
    pwd = request.json["pwd"]
    edad = request.json["edad"]
    resultado = crudUsuario.updateUser(id_u,nombre,correo,pwd,edad)
    if resultado:
        return jsonify({"mensaje": "usuario" + nombre + "FUE MODIFICADO CON ÉXITO"})
    return jsonify({"mensaje": "USUARIO NO EXISTE EN LA BASE DE DATOS"})


#LOGIN DE USUARIOS:
@app.route('/auth', methods=["POST"])
def login():
    correo = request.json["correo"]
    pwd = request.json["pwd"]
    resultado = crudUsuario.loginUser(correo,pwd)
    if resultado is None:
        return jsonify({"mensaje": "USUARIO INCORRECTO"}), 400
    resultado.pop('pwd')
    return jsonify(resultado),200


    #codigos HTTP:
    # ERROR: 400
    # CORRECTO: 200
    # RECUERSO CREADO: 201
    # PETICION INCORRECTA: 2400
    # NO SE ENCONTRÓ EL RECURSO: 404








#INDICAR PUERTO DE SALIDA.
if __name__=='__main__':
    app.run(debug=True, port=3000)

    