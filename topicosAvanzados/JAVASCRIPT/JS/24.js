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

class Carro extends Vehiculo{
    constructor(numLLantas, numPuertas, color, modelo, numCilindros){
        super(numLLantas, numPuertas, color)
        this.modelo       =modelo
        this.numCilindros =numCilindros
    }
    describirVehiculo(){
        //return`soy un ${this.modelo} de ${this.numLLantas} llantas`
        return `${super.describirVehiculo()}`
    }
}


const mazda = new Carro(6,4,'rojo','mazda 2020',4)
console.log(mazda.describirVehiculo());


