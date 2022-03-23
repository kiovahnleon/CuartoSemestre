

const persona={
    nombre: 'Kiovahn',
    genero: 'Hombre',
    edad: '21'
}


console.log("Forma 1 de accesar a los datos")
console.log(persona.nombre)
const nombrePersona = persona.nombre
console.log(nombrePersona)

console.log("Forma 2 de accesar a los datos")
console.log(persona["nombre"])
console.log(persona['edad'])

//acceso usando destructuring
const{nombre,genero,edad} = persona
console.log('\nAcceso a datos por destructuring')
console.log(nombre,genero,edad)

//agregar propiedad al objeto

persona.peso = 70
console.log(persona)