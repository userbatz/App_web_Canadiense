
async function iniciarSesion() {

    //paso 1: capturar los valores de los textboxs del frontend.
    let correo = document.getElementById('txtEmail').value;
    let pwd = document.getElementById('txtPwd').value;

    //CONECTARNOS CON TODOS LOS VALORES DE UNA RUTA EN NUESTRO BACKEND
    let res = await fetch("http://localhost:3000/auth",{
        method: "POST",
        headers: {'Content-type': 'application/json'},
        body: JSON.stringify(
            {
                "correo": correo,
                "pwd": pwd
            }
        )
    })

    

    if(res.status == 200) {
        alert('bienvenido al sistema')
        window.location.href = "http://127.0.0.1:5500/FRONTEND/index.html"
    }else {
        /* res = await res.json()
        alert(res.mensaje) */
        alert('ACCESO DENEGADO')
    }

}