

async function NewRegister() {
    let Nombre = document.getElementById('txtNombre').value;
    let Edad = document.getElementById('txtEdad').value;
    let Email = document.getElementById('txtEmail').value;
    let Password = document.getElementById('txtPassword').value;

    let res = await fetch("http://localhost:3000/usuario",{
        method: "POST",
        headers: {'Content-type': 'application/json'},
        body: JSON.stringify(
            {   
                "pwd": Password,
                "nombre": Nombre,
	            "correo": Email,
                "edad": Edad
            }
        )
    })

    res = await res.json();
    alert(res);
}