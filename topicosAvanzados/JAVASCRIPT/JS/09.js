const meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo']


const carrito = [
    {nombre: 'Tele',precio: 500},
    {nombre: 'Celular',precio: 1500},
    {nombre: 'Tablet',precio: 300},
    {nombre: 'Laptop',precio: 200},
    {nombre: 'Bocina',precio: 170},
]

//Preguntar si esta marzo en el array meses

meses.forEach(function(mes){
    if(mes === 'Marzo'){
        console.log("Si está")
    }
})

//Otra manera de preguntar si hay un elemento en un array
let resultado = meses.includes('Marzo')


if (meses.includes('Marzo')){
    console.log('sista')
}

//Para buscar en un array con objetos
resultado = carrito.some(
    function(producto){
        return producto.nombre === 'Celular'
    }
)

resultado = carrito.some(producto => producto.nombre === 'Celular')

//Contar los precios
resultado = carrito.reduce(
    function(total,producto){
        return total + producto.precio
    },0
)

resultado = carrito.reduce((total, producto) => total + producto.precio, 0)

//filtrar elementos
resultado = carrito.filter(
    function(producto){
        return producto.precio < 1000
    }
)

resultado = carrito.filter(producto => producto.nombre === 'Tele')

console.log(resultado)