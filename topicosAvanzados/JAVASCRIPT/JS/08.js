//arreglos

const numero = [10,20,30,40,50,60]

console.log('Recorrido con function')
numero.forEach(function (valor){
    console.log(valor)
})

console.log('Recorrido con arrow function')
numero.forEach(
    num=>console.log(num)
)