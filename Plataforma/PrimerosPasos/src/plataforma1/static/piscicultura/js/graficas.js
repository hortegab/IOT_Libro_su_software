// esta funcion es para crear datos secuencialmente
function range(start, stop, step) {
    var a = [start], b = start;
    while (b < stop) {
        a.push(b += step || 1);
    }
    return a;
}
// ajax es la tecnologia que usaremos para hacer consultas a la API usando GET
$.ajax({
        type: "GET",
        url: "/piscicultura/temperatura-pozo", //esta es la URL de la API para hacer un GET
        dataType: 'json',
        success: function (data){
        var xaxes = range(0,1*data.length,1)
        var datos = [];
        for(var i=0; i<data.length; i++){
            datos.push(data[i].valor)
        }
        console.log(datos)
        // de aqui hacia abajo van las graficas
         var ctx = document.getElementById('myChart');
         let chart = new Chart(ctx, {
             type: 'line',
             data: {
                 datasets: [{
                     label: 'Temperatura',
                     data: datos,
                     fill: false,
                     backgroundColor: ['#f44336'],
                     borderColor: ['#f44336'],
                 },
               
                 ],
                 labels: xaxes
             },
             options: {
                 scales: {
                     yAxes: [{
                         ticks: {
                             suggestedMin: 50,
                             suggestedMax: 100
                         }
                     }]
                 }
             }
         });

}}); // fin ajax