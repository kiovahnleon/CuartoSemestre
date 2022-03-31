//Async, awaait

function descargarNuevosClientes(){
    return new Promise(resolve => {
            console.log('Descargando clientes...., esepere');

    setTimeout(()=>{
        resolve('los clientes fueron descargados');
    },5000);
    });

}

function descarrgarUltimosPedidos(){
    return new Promise(resolve => {
            console.log('Descargando pedidos...., esepere');

    setTimeout(()=>{
        resolve('los pedidos fueron descargados');
    },3000);
    });

}

async function app(){
    try {
        // const clientes = await descargarNuevosClientes();
        // const pedidos = await descarrgarUltimosPedidos();
        // console.log(clientes);
        // console.log(pedidos);

        const resultados = await Promise.all([descargarNuevosClientes(),descarrgarUltimosPedidos()]);

        console.log(resultados[0]);
        console.log(resultados[1]);

    } catch (error) {
        console.log(error);
    }
}

app();