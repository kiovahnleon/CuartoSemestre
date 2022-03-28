//Metodos de Funcion

const reproductor = {
    reproducir : function(id){
        console.log(`Reproduciendo ${id}`);
    },
    pausar: function(){
        console.log("Pausando...");
    },
    crearPlaylist: function(nombre){
        console.log(`Crendo la playlist ${nombre}`);
    },
    reproducirPlaylist : function(nombre){
        console.log(`Reproduciendo la playlist ${nombre}`);
    },
}

reproductor.borrarCancion = function(id){
    console.log(`Eliminando la cancion ${id}`);
}


reproductor.reproducir(40)
reproductor.pausar()
reproductor.borrarCancion(35)
reproductor.crearPlaylist('Liked Songs')
reproductor.reproducirPlaylist('Corazon')