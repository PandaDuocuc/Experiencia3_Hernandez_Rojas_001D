document.addEventListener("DOMContentLoaded", function() {
    // Función para validar el formulario al enviar
    document.getElementById("postulacionForm").addEventListener("submit", function(event) {
        event.preventDefault();
        validarFormulario();
    });
});

function validarFormulario() {
    // Validaciones de campos
    let isValid = true;
    let nombre = document.getElementById("nombre").value;
    let apellidos = document.getElementById("apellidos").value;
    let celular = document.getElementById("celular").value;
    let rut = document.getElementById("rut").value;
    let genero = document.getElementById("genero").value;
    let contraseña = document.getElementById("password").value;

    if (nombre.length < 3 || nombre.length > 20) {
        alert("El nombre debe tener entre 3 y 20 caracteres.");
        isValid = false;
    }

    if (apellidos.length < 3 || apellidos.length > 20) {
        alert("El apellido paterno debe tener entre 3 y 20 caracteres.");
        isValid = false;
    }

    const celularRegexx = /^[0-9]{9}$/;
    if (!celularRegexx.test(celular)) {
        alert("El número de celular debe tener 9 dígitos.");
        isValid = false;
    }

    const rutRegex = /^\d{1,2}\.\d{3}\.\d{3}-[\dkK]$/;
    if (!rutRegex.test(rut)) {
        alert("El RUT no es válido.");
        isValid = false;
    }

    if (genero === "") {
        alert("Seleccione un género.");
        isValid = false;
    }

    if (contraseña.length < 6 || contraseña.length > 100) {
        alert("La contraseña debe tener al menos 6 caracteres.");
        isValid = false;
    }    

    // Si todas las validaciones pasan, se envía el formulario
    if (isValid){
        document.getElementById("postulacionForm").submit();
    }
}

function mostrarPassword() {
    var passwordInput = document.getElementById("password");
    if (passwordInput.type === "password") {
        passwordInput.type = "text";
    } else {
        passwordInput.type = "password";
    }
}