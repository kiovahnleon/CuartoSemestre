//fetch

function obtenerEmpleados(){
    const archivo = '1.json';
    fetch(archivo)
    .then(resultado => {return resultado.json()})
    .then(datos => {
        console.log(datos); 

        const {empleados}=datos;
        empleados.forEach(worker => {console.log(worker.id,worker.nombre,worker.puesto);})
        
    }
    )
}

obtenerEmpleados();
