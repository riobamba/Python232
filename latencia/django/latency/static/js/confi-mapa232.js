var url;
var tabla;
var cadena;
var network;
var idnetwork;
var idstation;
var codeNetwork;
var nameStation;
var codigostation;
var eventos = new Array();
var canalConsulta = new Array();
var stringCanales = "";
var dialog;
var map;
var latencia;
var estaciones = [];
var panel = new Array();
var urlservicio="http://127.0.0.1:8000/"
var servidor="232"
var soundID = "Thunder";
var soundID2 = "Thunder2";
var est_act=0;
var respuesta="";
var infoWindow = new google.maps.InfoWindow();

function initMap() {
    iniciarMapa();
    //crearMenu();

}

setInterval(myTimer, 10000);

function myTimer() {
    marcadores();

}



function redSeleccionada(net) {
    //alert(net)
    for (var i = 0, length = estaciones.length; i < length; i++) {
        if (estaciones[i].tipo == net) {
            if (estaciones[i].visible) {
                estaciones[i].setVisible(false)
                estaciones[i].visible = false;
            } else {
                estaciones[i].setVisible(true)
                estaciones[i].visible = true;
            };
        } else {}
    }
}

function crearMenu() {
    var opciones = ""
    $.getJSON('http://10.100.100.232:8081/query/stations.json', function(data) {
        for (var i = 0; i < data.Inventory.network.length; i++) {
            var env = "\'" + data.Inventory.network[i].code + "\'";
            var desc = data.Inventory.network[i].description;
            if (desc.length > 10) {
                //desc=desc.substring(0,25)+"..."
            };
            opciones = opciones + '<input type="checkbox" onchange="redSeleccionada(' + env + ')" checked>' +
                '<span class="check"></span>' +
                '<span class="caption"><small>' + desc + '</small></span><br>';
        };
        $("#menuflotante").html(opciones);
    })
}
//+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

function construirTabla(nombre,estacion) {
    var fil = "";
    var resp = "";
    tabla = '<table class="table striped hovered" id="main_table_demo">' +
        '<thead>		  ' +
        '<tr>  ' +
        '<th>'+ nombre+ '</th>' +
        '</tr>            ' +
        '</thead>         ' +
        '<thead>          ' +
        '<tr>  ' +
        '<th>Estado</th>' +
        '<th>Fecha</th>' +
        '</tr>            ' +
        '</thead>         ' +
        '<tbody>';

   $.getJSON(urlservicio+'historialEstacion/?servidor=232&estacion='+nombre, function(data) {
        var long =data.length
        if(long > 0){
            $.each(data, function(i, field) {
				b=field.valor;
				f=field.fecha;
				var fila = "";
				if(b == "in"){
				    b = "<font color='green'><b>Ingresa</b></font>";
				}
				if(b == "out"){
				    b = "<font color='red'><b>Sale</b></font>";;
				    fila = "<tr bgcolor='#FF0000'>"
				}
				fil += "<tr><td>" + b + "</td><td>" + f + "</td></tr>";
			});
			var fin=  '</tbody></table>';
			respuesta= tabla.concat(fil,fin);
			infoWindow.setContent(respuesta);
			infoWindow.open(map, estacion);
        }else{
            tabla = '<table class="table striped hovered" id="main_table_demo"><thead>' +
            '<tr><th>'+ nombre+ '</th></tr></thead>'+
            '<thead><tr><th>Sin Novedad</th></tr></thead></table>';
            infoWindow.setContent(tabla);
			infoWindow.open(map, estacion);
        }

	})
}

function marcadores() {
    $.getJSON(urlservicio+'latencia232/', function(data) {
    est_act=0;
        $.each(data, function(i, field) {
            var label = "";
            if (field.valor == 'ok') {
                 est_act+=1;
                label = "label1";
            } else if (field.valor == 'entra') {
                label = "label2";
            } else if (field.valor == 'salio') {
                label = "label3";
            } else {
                label = "label4";
            }
            for (var i = 0, length = estaciones.length; i < length; i++) {
                if (field.estacion == estaciones[i].title) {
                    if (field.valor != estaciones[i].valor) {
                        estaciones[i].setMap(null);
                        estaciones[i].valor = field.valor
                        estaciones[i].labelClass = label;
                        estaciones[i].setMap(map);
                    }
                }
            }
        });
    })

    $("#esta_activas").text("Activas "+est_act+"/"+estaciones.length);
    var nuevos = false;
    $.getJSON(urlservicio+'historial2/'+servidor, function(data) {

        $.each(data, function(i, field) {
            if (repetidosPanel(field)==false){
                if (field.valor == "in") {
                $.Notify({
                    caption: '       Ingresa ' + field.estacion,
                    content: field.fecha,
                    type: 'info',
                    timeout: 20000,
                    icon: "<span class='mif-checkmark'></span>"
                });
                if (field.admin!="INTER"){
                playSoundIngreso();
                }
            } else {
                $.Notify({
                    caption: '       Sale ' + field.estacion,
                    content: field.fecha,
                    type: 'warning',
                    timeout: 20000,
                    icon: "<span class='mif-cross'></span>"
                });
                if (field.admin!="INTER"){
                playSoundSalida();
                }
            }
            }


        });

        $.each(data, function(i, field) {
            if (repetidosPanel(field)==false){
                            nuevos = true;
            var aux = new Array();
            for (var i = 0, length = panel.length; i < (length - 1); i++) {
                aux.push(panel[i])
            }

            panel = new Array();
            panel.push(field)
            for (var i = 0, length = aux.length; i < length; i++) {
                panel.push(aux[i])
            }
            }

        });

        if (nuevos == true) {
            pintarPanel();
        }
    })

}

function repetidosPanel(field){
        for (var i = 0, length = panel.length; i < length; i++) {
            if (panel[i].estacion == field.estacion && panel[i].fecha == field.fecha) {
                    //alert(panel[i].estacion+" == "+field.estacion+" && "+panel[i].fecha+" =="+ field.fecha)
                    return true;
                }
        }
        return false;
}

function pintarPanel() {
    $("#history").empty();
    $.each(panel, function(i, field) {
        if (field.valor == "in") {
            $("#history").append("<div class='alert alert-success' role='alert'><strong>Ingresa " + field.estacion + "</strong><br>" + field.fecha + "</div>");
        } else {
            $("#history").append("<div class='alert alert-danger' role='alert'><strong>Sale " + field.estacion + "</strong><br>" + field.fecha + "</div>");
        }
    });
}

function clearOverlays() {
    for (var i = 0; i < estaciones.length; i++) {
        markersArray[i].setMap(null);
    }
    markersArray.length = 0;
}



function iniciarMapa() {

    var estacion = "";
    map = new google.maps.Map(document.getElementById('map_canvas'), {
        zoom: 6,
        center: {
            lat: 4.542903,
            lng: -73.569119
        },
        mapTypeId: google.maps.MapTypeId.TERRAIN
    });
    //marcadores();
    $.getJSON(urlservicio+'latencia232/', function(data) {
        $.each(data, function(i, field) {
            var label = "";
            if (field.valor == 'ok') {
                label = "label1";
            } else if (field.valor == 'entra') {
                label = "label2";
            } else if (field.valor == 'salio') {
                label = "label3";
            } else {
                label = "label4";
            }
            estacion = new MarkerWithLabel({
                position: new google.maps.LatLng(field.latitud, field.longitud),
                icon: {
                    path: google.maps.SymbolPath.CIRCLE,
                    scale: 0, //tamaño 0
                },
                map: map,
                title: field.estacion,
                visible: true,
                labelContent: field.estacion,
                valor: field.valor,
                labelAnchor: new google.maps.Point(10, 10),
                labelClass: label
            });

            estaciones.push(estacion);


            google.maps.event.addListener(estacion, 'click', (function(estacion) {
            		var est = estacion;
            		return function() {
            			//da = data.Inventory.network[l].station;
            			construirTabla(estacion.title,estacion);
            			//infoWindow.setContent(estacion.title+" "+estacion.valor);
            			//infoWindow.setPosition();

            		}
            	})(estacion));
        });
    })

    $("#history").empty();
    $.getJSON(urlservicio+'historial/'+servidor, function(data) {

        $.each(data, function(i, field) {
            panel.push(field)
            if (field.valor == "in") {
                $("#history").append("<div class='alert alert-success' role='alert'><strong>Ingresa " + field.estacion + "</strong><br>" + field.fecha + "</div>");
            } else {
                $("#history").append("<div class='alert alert-danger' role='alert'><strong>Sale " + field.estacion + "</strong><br>" + field.fecha + "</div>");
            }

        });
    })
    createjs.Sound.registerSound("static/assets/alarma.mp3", soundID);
    createjs.Sound.registerSound("static/assets/entra.mp3", soundID2);
}


function showDialog() {
    var da = network.Inventory.network[idnetwork].station;
    var sl = da[idstation].sensorLocation;
    var canal = "";
    var conta = 0;
    var col = 0;

    dialog = $("#dialog9").data('dialog');
    if (!dialog.element.data('opened')) {
        $("#station").html("<h3>" + codigostation + ", " + nameStation + "</h3>");
        $("#componentes").html(canal);
        dialog.open();
    } else {
        dialog.close();
    }
}

function playSoundSalida () {
  createjs.Sound.play(soundID);
}

function playSoundIngreso () {
  createjs.Sound.play(soundID2);
}

function sleep(milliseconds) {
  var start = new Date().getTime();
  for (var i = 0; i < 1e7; i++) {
    if ((new Date().getTime() - start) > milliseconds){
      break;
    }
  }
}