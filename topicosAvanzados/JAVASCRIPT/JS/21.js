//this en JAVA SCRIPT

window.nombre='xenia'
window.total=60

const reservacion = {
    nombre: 'Pedro',
    apellido: 'Sola',
    total: 5000,
    pagado: false,
    informacion: function() {
        console.log(this);
        console.log(`Cliente ${reservacion.nombre} reservo y debe pagar ${reservacion.total}`);
    }
}

const reservacion2 = {
    nombre: 'Pedro',
    apellido: 'Sola',
    total: 5000,
    pagado: false,
    informacion: () => {
        console.log(this);
        console.log(`Cliente ${this.nombre} reservo y debe pagar ${this.total}`);
    }
}

//this funciona con function [llama al objeto] pero no con => (this  en => llama a todo el window)

reservacion.informacion()
reservacion2.informacion()