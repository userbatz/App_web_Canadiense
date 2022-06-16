const ContentUsers = document.getElementById('ContentUsers');

async function getUsers() {


    //obteniendo información del servidor.
    let UserResponse = await fetch("http://localhost:3000/usuario",{
        method: "GET",
        headers: {'Content-type': 'application/json'},
    })

    
    //convirtiendo la variable a formato JSON
    const response = await UserResponse.json();
    
 
    console.log(response);
    //verificando conexion al servidor.
    if (UserResponse.status != 200) {
        console.log('hubo un problema al cargar la información');
        
    } else {
        console.log('datos cargados');
    }

    
 

    //deconstruir el elemento.
    const {datos: usuario} = response;
  

    limpiarbody()
   
    

    usuario.forEach( usuario => {
        

        //se crearon las variables que se encargarán de crear filas y las columnas de cada una de ellas.
        const filaNueva = document.createElement('tr');
        const colId = document.createElement('td');
        const colNombre = document.createElement('td');
        const colEdad = document.createElement('td');
        const colCorreo = document.createElement('td');
        const colPassword = document.createElement('td');
        const colAcciones = document.createElement('td');

        //creando variable para el boton MODIFICAR
        const btnModificar = document.createElement('button');
        btnModificar.classList.add('btn','btn-warning','btn-icon-split');
        btnModificar.innerText= "MODIFICAR USUARIO";



        //agregar a las columnas el boton.
        colAcciones.appendChild(btnModificar);


        //AGREGANDO LA INFORMACIÓN EN CADA COLUMNA DE DATOS.
        colId.innerText = usuario.id
        colNombre.innerText = usuario.nombre
        colEdad.innerText = usuario.edad
        colCorreo.innerText = usuario.correo 
        colPassword.innerText = usuario.pwd
        

        //agregando las columnas a la fila.
        filaNueva.appendChild(colId);
        filaNueva.appendChild(colNombre);
        filaNueva.appendChild(colEdad);
        filaNueva.appendChild(colCorreo);
        filaNueva.appendChild(colPassword);  
        filaNueva.appendChild(colAcciones);


        ContentUsers.appendChild(filaNueva);



    } );


}











function limpiarbody() {
    while(ContentUsers.firstChild){
        ContentUsers.removeChild(ContentUsers.firstChild)
    }
}

