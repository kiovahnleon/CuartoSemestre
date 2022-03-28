//arrow function

const sumar = (n1,n2) => console.log(n1+n2);

sumar(620,20)


const cuadrado = num => console.log(num*num);

cuadrado(2)


const aprendiendo = tecnologia => console.log(`Estoy prendiendo ${tecnologia}`);

aprendiendo('Javascript')


const operaciones = (n1,n2) => {
    if(n1>n2){
        console.log('N1 es mayor que N2');
    }else{
        console.log('N2 es mayor que N1');
    }
}

operaciones(10,6)