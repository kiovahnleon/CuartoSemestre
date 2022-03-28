//ciclo for

const carrito = [
    {nombre: 'Tele',precio: 500},
    {nombre: 'Celular',precio: 1500},
    {nombre: 'Tablet',precio: 300},
    {nombre: 'Laptop',precio: 200},
    {nombre: 'Bocina',precio: 170},
]

// for(let i = 1 ; i < 10 ; i++){
//     if(i%2 === 0){
//         console.log('par');
//     }else{
//         console.log('impar');
//     }
// }

for(let i = 0 ; i< carrito.length ; i++){
    console.log(carrito[i].nombre);
}