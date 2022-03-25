//funciones

//Declaracion de funcion (las pued utilizar en cualquier parte del archivo)
function suma1(a,b){
    console.log(a+b)
}

//expresion de funcion (solo se pueden usar despues de hacerlas)
const suma2= function(){
   console.log(10+10)
}

//suma2()
//console.log(suma2)

//IIFE
(function(){
    console.log('esta es una funcion');
})();