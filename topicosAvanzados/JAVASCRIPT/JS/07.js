"use strict"

const persona={
    nombre: 'Kiovahn',
    genero: 'Hombre',
    edad: '21'
}

const medidas={
    peso: 70,
    estatura: 175
}

//usando el operador ... spread operator

const datosPaciente = {...persona, ...medidas}
console.log(datosPaciente)