//POO - CLASES
class Vehiculo{
    constructor(numLLantas, numPuertas, color){
        this.numLLantas=numLLantas
        this.numPuertas=numPuertas
        this.color=color
    }

    describirVehiculo(){
        return`soy un vehiculo de ${this.numLLantas} llantas`
    }
}

const bici = new Vehiculo(2,0,'azul');
console.log(bici.describirVehiculo());

class Carro{
    constructor(numLLantas, numPuertas, color, modelo, numCilindros){
        this.numLLantas   =numLLantas
        this.numPuertas   =numPuertas
        this.color        =color
        this.modelo       =modelo
        this.numCilindros =numCilindros
    }
    describirCarro(){
        return `soy un ${this.modelo} de ${this.numLLantas} llantas`
    }
}

const mazda = new Carro (4,4,'Amarillo','Mazda 1990', 4)
const honda = new Carro (4,4,'Amarillo','honda 2000', 4)

console.log(mazda.describirCarro())
console.log(honda.describirCarro());
