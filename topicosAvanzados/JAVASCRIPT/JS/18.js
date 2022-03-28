//while

let i = 1

while( i<=100 ){
    //.....
    let valor = i%2 === 0 ? `${i} es par` : `${i} es impar`
    console.log(valor);
    i++;
}