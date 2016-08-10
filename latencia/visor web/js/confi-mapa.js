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
var canalConsulta=new Array();
var stringCanales="";
var dialog;
var estaciones= new Array();
var map;
var latencia;

function initMap() {

	iniciarMapa();
	//crearMenu();

}

setInterval(myTimer, 10000);
function myTimer() {
	var dt = new Date();

	var month = dt.getMonth()+1;
	var day = dt.getDate();
	var year = dt.getFullYear();
	var hora = dt.getHours();
	var minuto= dt.getMinutes();
	var segundo=dt.getSeconds();
	var fecha=year+ceros(month)+ceros(day)+"."+ceros(hora)+ceros(minuto)+ceros(segundo);

	latencia= $.getJSON('http://10.100.100.232:8081/query/objects.json?QC&last='+fecha, function(data) {

	})


	marcadores2(latencia);
}
function ceros(num) {
	if (num < 10){
		return "0"+num;
	}else{
		return ""+num;
	}
}


//  ++++++++++Opciones Flotantes+++++++++++++++++++++++++++++++++
// tener en cuenta
//funcion crearMenu();
//aumentar la booleana en el array del mapa
//hacer estaciones global
// cambiar el id pigture por flotante y el css



function redSeleccionada(net) {
		//alert(net)
		for (var i = 0, length = estaciones.length; i < length; i++) {
			if(estaciones[i].tipo==net){
				if (estaciones[i].visible) {
					estaciones[i].setVisible(false)
					estaciones[i].visible=false;
				} else{
					estaciones[i].setVisible(true)
					estaciones[i].visible=true;
					};
				}else{
					}
		}
}

function crearMenu() {
	var opciones=""
	$.getJSON('http://10.100.100.232:8081/query/stations.json', function(data) {
		for (var i=0; i < data.Inventory.network.length; i++) {
			var env="\'"+data.Inventory.network[i].code+"\'";
			var desc=data.Inventory.network[i].description;
			if (desc.length>10) {
				//desc=desc.substring(0,25)+"..."
			};
			opciones=opciones+'<input type="checkbox" onchange="redSeleccionada('+env+')" checked>'+
					'<span class="check"></span>'+
					'<span class="caption"><small>'+desc+'</small></span><br>';
			};
			$( "#menuflotante" ).html(opciones);
		})
}
//+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++




function construirTabla(description,codigo,longitud,latitud,elevacion,data,i,j) {
	var da=data.Inventory.network[i].station;
	var sl=da[j].sensorLocation;
	nameStation=da[j].description;
	codeNetwork=data.Inventory.network[i].code;
	var canal="";
	codigostation=codigo;
	network=data;
	idnetwork=i;
	idstation=j;

	tabla='<table class="table striped hovered" id="main_table_demo">'+
		'<thead>		  '+
		'<tr>  '+
		'<th>Estación</th>'+
		'<th>'+codigo+'</th>'+
		'</tr>            '+
		'</thead>         '+
		'<tbody>          '+
		'<tr >             '+
		'    <td colspan="2">'+nameStation+'</td>   '+
		'</tr>            '+
		'<tr >             '+
		'    <td colspan="2">'+description+'</td>   '+
		'</tr>            '+
		'<tr>             '+
		'    <td>Latitud</td>   '+
		'    <td>'+latitud+'</td>   '+
		'</tr>            '+
		'<tr>             '+
		'    <td>Longitud</td>   '+
		'    <td>'+longitud+'</td>   '+
		'</tr>            '+
		'<tr>             '+
		'    <td>Elevación</td>   '+
		'    <td>'+elevacion+'</td>   '+
		'</tr>            '+
		'</tbody>         '+
		'</table>         '+
		'<button class="button success small-button" onclick="showDialog()">Historial de funcionamiento</button>'
	return tabla;
}

function marcadores() {

	cadena = $.getJSON('http://10.100.100.232:8081/query/stations.json', function(data) {
		var codigo,
		    longitud,
		    latitud,
		    elevacion,
		    canales;
		for ( var l=0; l < data.Inventory.network.length; l++) {
			var dataEstacion = data.Inventory.network[l].station;
			for (var j=0; j < dataEstacion.length; j++) {
				var label="";
				if (data.Inventory.network[l].code=="CM") {
					label="label1"
				} else if (data.Inventory.network[l].code=="OM"){
					label="label1"
				}else if (data.Inventory.network[l].code=="PP"){
					label="label2"
				}else if (data.Inventory.network[l].code=="OP"){
					label="label3"
				}else{
					label="label4"
				}

				estacion = new MarkerWithLabel({
					position : new google.maps.LatLng(dataEstacion[j].latitude, dataEstacion[j].longitude),
					icon : {
						path : google.maps.SymbolPath.CIRCLE,
						scale : 0, //tamaño 0
					},
					map : map,
					title : dataEstacion[j].code,
					visible:true,
					labelContent : dataEstacion[j].code,
					tipo : data.Inventory.network[l].code,
					labelAnchor : new google.maps.Point(10, 10),
					labelClass : label
				});

				estaciones.push(estacion);
				google.maps.event.addListener(estacion, 'click', (function(estacion, l, k) {
					var est = estacion;
					var i = j
					return function() {
						da = data.Inventory.network[l].station;
						infoWindow.setContent(construirTabla(data.Inventory.network[l].description, da[i].code, da[i].longitude, da[i].latitude, da[i].elevation, data, l, i));
						//infoWindow.setPosition();
						infoWindow.open(map, estacion);
					}
				})(estacion, l));

			};

		}
	})
}

function marcadores2(latencia) {

	cadena = $.getJSON('http://10.100.100.232:8081/query/stations.json', function(data) {
		var codigo,
			longitud,
			latitud,
			elevacion,
			canales;
		for ( var l=0; l < data.Inventory.network.length; l++) {
			var dataEstacion = data.Inventory.network[l].station;
			for (var j=0; j < dataEstacion.length; j++) {
				var label="";
				if (data.Inventory.network[l].code=="CM") {
					label="label1"
				} else if (data.Inventory.network[l].code=="OM"){
					label="label1"
				}else if (data.Inventory.network[l].code=="PP"){
					label="label2"
				}else if (data.Inventory.network[l].code=="OP"){
					label="label3"
				}else{
					label="label4"
				}

				estacion = new MarkerWithLabel({
					position : new google.maps.LatLng(dataEstacion[j].latitude, dataEstacion[j].longitude),
					icon : {
						path : google.maps.SymbolPath.CIRCLE,
						scale : 0, //tamaño 0
					},
					map : map,
					title : dataEstacion[j].code,
					visible:true,
					labelContent : dataEstacion[j].code,
					tipo : data.Inventory.network[l].code,
					labelAnchor : new google.maps.Point(10, 10),
					labelClass : label
				});

				estaciones.push(estacion);
				google.maps.event.addListener(estacion, 'click', (function(estacion, l, k) {
					var est = estacion;
					var i = j
					return function() {
						da = data.Inventory.network[l].station;
						infoWindow.setContent(construirTabla(data.Inventory.network[l].description, da[i].code, da[i].longitude, da[i].latitude, da[i].elevation, data, l, i));
						//infoWindow.setPosition();
						infoWindow.open(map, estacion);
					}
				})(estacion, l));

			};

		}
	})
}

function iniciarMapa() {
	var infoWindow = new google.maps.InfoWindow();
	var estacion = "";
	map = new google.maps.Map(document.getElementById('map_canvas'), {
		zoom : 6,
		center : {
			lat : 4.542903,
			lng : -73.569119
			},
		mapTypeId : google.maps.MapTypeId.TERRAIN
		});
	marcadores();
}

function showDialog(){
var da=network.Inventory.network[idnetwork].station;
var sl=da[idstation].sensorLocation;
var canal="";
var conta=0;
var col=0;

dialog = $("#dialog9").data('dialog');
if (!dialog.element.data('opened')) {
	$( "#station" ).html("<h3>"+codigostation+", "+nameStation+"</h3>");
	$( "#componentes" ).html(canal);
	dialog.open();
	} else {
	dialog.close();
	}
}
