const boton = document.querySelector('#boton');

boton.addEventListener('click',() =>{
    Notification.requestPermission()
    .then(resultado => console.log(resultado))
})

if(Notification.permission == 'granted'){
    new Notification('Esta es una notificacion',{
        icon: 'img/hamster.png',
        body : 'La profe Xenia es la mejor'
    })
}

