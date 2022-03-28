//POO

//OBJECT LITERAL
const producto = {
    nombre: 'table',
    precio: 500
}

//objeto constructor
function Producto(nombre, precio){
    this.nombre=nombre
    this.precio=precio
}

const producto2 = new Producto('TV', 500);
const producto3 = new Producto('ipad', 4000)
console.log(producto2);
console.log(producto3);