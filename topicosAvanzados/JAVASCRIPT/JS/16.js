//switch

const metodoDePago = 'tarjeta';

switch(metodoDePago){
    case 'tarjeta':
        console.log('Pagaste con tarjeta');
        break;
    
    default:
        console.log('Aun no has pagado');
        break;
}