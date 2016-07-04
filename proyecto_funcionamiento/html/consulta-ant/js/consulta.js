var area = "todos";
var fechaini = "";
var fechafin = "";
var promin = "";
var promax = "";
var magmin = "";
var magmax = "";
var tipmag = "";
var maxlat = "";
var minlon = "";
var maxlon = "";
var minlat = "";
var jevento="";
var peticion = "http://10.100.100.232:18081/events/query?";
//var peticion = "http://service.iris.edu/fdsnws/event/1/query?";
var url;
function construirConsulta() {

	fechaini = $("#datetimepicker_mask").val();
	if (fechaini.length > 0) {
		fechaini = "start=" + fechaini.replace(" ", "T") + "&";
	}

	fechafin = $("#datetimepicker_mask1").val();
	if (fechafin.length > 0) {
		fechafin = "end=" + fechafin.replace(" ", "T") + "&";
	}

	promin = $("#profundidad_minima").val();
	if (promin.length > 0) {
		promin = "mindepth=" + promin + ".0&";
	}
	promax = $("#profundidad_maxima").val();
	if (promax.length > 0) {
		promax = "maxdepth=" + promax + ".0&";
	}

	magmin = $("#magnintud_minima").val();
	if (magmin.length > 0) {
		magmin = "minmag=" + magmin + ".0&";
	}

	magmax = $("#magnitud_maxima").val();
	if (magmax.length > 0) {
		magmax = "maxmag=" + magmax + ".0&";
	}

	$('select#tipomag').on('change', function() {
		tipmag = $(this).val();
		tipmag = "magtype=" + tipmag + "&";
	});

	if (area == "area") {
		maxlat = "maxlat=" + $("#latmax").val() + "&";
		minlon = "minlon=" + $("#lonmin").val() + "&";
		maxlon = "maxlon=" + $("#lonmax").val() + "&";
		minlat = "minlat=" + $("#latmin").val() + "&";

	} else {
		maxlat = "";
		minlon = "";
		maxlon = "";
		minlat = "";
	}
	//http://10.100.100.232:18081/events/query?start=2016-02-10T00:00:00&end=2016-02-11T17:00:00&minmag=3.0&maxmag=6.0&mindepth=100.0
	url = peticion + fechaini + fechafin + magmin + magmax + tipmag + promin + promax + maxlat + minlon + maxlon + minlat ;

	$("#ruta").html('<a href="' +url+ '" TARGET="_new">' + url + '</a> ');

}

function ejecutarConsulta() {

	$.ajax({
		url : url,
		type : 'GET',

		success : function(xml) {
			var contenido = "";
			var linea = xml.split("\n");
			var linea1="";
			for (var i = 0; i <= linea.length-2; i++) {
				linea1=linea[i];

				var datos=linea1.split(";");

				for (var j = 0; j <= datos.length-1; j++) {
					var type = datos[10]
					var text = datos[12]
					var timevalue = datos[2]
					var author = datos[9]
					var latitudevalue = datos[5]
					var longitudevalue = datos[6]
					var depthvalue = datos[7]
					var typemag = datos[4]
					var valuemag = datos[3]
					
				};
				contenido = contenido + "<tr><td>" + type + "</td><td>" + text + "</td><td>" + timevalue + "</td><td>" + author + "</td><td>" + latitudevalue + "</td><td>" + longitudevalue + "</td><td>" + depthvalue + "</td><td>" + typemag + "</td><td>" + valuemag + "</td></tr>"
			};

				
	
			
			$("#tabla").html(contenido);
			$('#tabla_general').show();
		},

		error : function(xhr, status) {
			alert('Disculpe, existió un problema');
		},

		complete : function(xhr, status) {
			// alert('Petición realizada');
		}
	});
}

function construirJson() {

	var win = window.open('mapa.html?c='+url, '_blank');
			win.focus();
}




