//arreglos

const numero = [5,10,20,50,100]

console.log('Recorrido con function')
numero.forEach(function (valor){
    console.log(valor)
})

console.log('Recorrido con arrow function')
numero.forEach(num=>console.log(num))

console.log('recorrido')
numero.forEach(function(num){
    console.log(num)
})

numero.forEach((num) => console.log(num))

numero.push(200)

numero.unshift(-10,0)

numero.shift()

ultimoNumero = numero.pop()
console.log(`El ultimo valor fue: ${ultimoNumero}`)

numero[4]=23

console.table(numero)

const meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo']

//eliminar elementos a partir de una posicion
//meses.splice(2,1)

let nuevosMeses = ['Diciembre',...meses,'Junio'];

console.log(nuevosMeses)