//invocando la ejecucion estricta de js
"use strict"

//modificar, eliminar, congelar, selllar propiedades
const persona={
    nombre: 'Kiovahn',
    genero: 'Hombre',
    edad: '21'
}

//agregando una propiedad nueva al objeto
persona.peso=70

//eliminando un propiedad del objeto
delete persona.edad



//congelando el objeto
// Object.freeze(persona)
// persona.estatura=175

Object.seal(persona)
persona.nombre = 'Yelena'
delete persona.nombre

console.log(persona)