//PROMISES
const usuarioAutentificado = new Promise( (resolve,reject) =>{
    const auth = true
    if(auth){
        resolve('Usuario autentificado') //el promise se cumple
    }else{
        reject('No se puede iniciar sesion')//el promise no se cumple
    }
})

usuarioAutentificado
    .then((resultado)=> console.log(resultado))
    .catch((error)=> console.log(error))

//en los promise existen 3 valores
//Pending: no se ha cumplido pero tampoco se ha rechazado
//Fullfiled: ya se cumplio
//Rejected: no se cumplio
