const carrito = [
    {nombre: 'Tele',precio: 500},
    {nombre: 'Celular',precio: 1500},
    {nombre: 'Tablet',precio: 300},
    {nombre: 'Laptop',precio: 200},
    {nombre: 'Bocina',precio: 170},
]

//foreach (solo para recorrer un arreglo)
const arreglo1  = carrito.forEach( producto => producto.nombre);

//map (da la posibilidad de de sacar informacion de ese arreglo y crear un arreglo nuevo)
const arreglo2 = carrito.map( producto => `${producto.nombre} - ${producto.precio}`);


console.log(arreglo2);