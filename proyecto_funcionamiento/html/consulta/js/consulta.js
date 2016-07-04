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
var peticion = "http://10.100.100.232:8091/fdsnws/event/1/query?";
//var peticion = "http://service.iris.edu/fdsnws/event/1/query?";
var url1;
function construirConsulta() {

	fechaini = $("#datetimepicker_mask").val();
	if (fechaini.length > 0) {
		fechaini = "starttime=" + fechaini.replace(" ", "T") + "&";
	}

	fechafin = $("#datetimepicker_mask1").val();
	if (fechafin.length > 0) {
		fechafin = "endtime=" + fechafin.replace(" ", "T") + "&";
	}

	promin = $("#profundidad_minima").val();
	if (promin.length > 0) {
		promin = "mindepth=" + promin + "&";
	}
	promax = $("#profundidad_maxima").val();
	if (promax.length > 0) {
		promax = "maxdepth=" + promax + "&";
	}

	magmin = $("#magnintud_minima").val();
	if (magmin.length > 0) {
		magmin = "minmag=" + magmin + "&";
	}

	magmax = $("#magnitud_maxima").val();
	if (magmax.length > 0) {
		magmax = "maxmag=" + magmax + "&";
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
	url1 = peticion + fechaini + fechafin + magmin + magmax + tipmag + 'orderby=time&format=xml&' + promin + promax + maxlat + minlon + maxlon + minlat + 'nodata=404';

	$("#ruta").html('<a href="' +url1+ '" TARGET="_new">' + url1 + '</a> ');

}

function ejecutarConsulta() {
	$.ajax({
		url : 'php/eventos.php',
		data : {
			urlx : url1
		},
		type : 'POST',
		
		success : function(xml) {
			var contenido = "";
			$(xml).find('event').each(function() {
				var event = $(this);

				var description = event.find("description");
				var type = description.find("type").text();
				var text = description.find("text").text();

				var origin = event.find("origin");
				var time = origin.find("time");
				var timevalue = time.find("value").text();

				var creationInfo = origin.find("creationInfo");
				var author = creationInfo.find("author").text();

				var latitude = origin.find("latitude");
				var latitudevalue = latitude.find("value").text();

				var longitude = origin.find("longitude");
				var longitudevalue = longitude.find("value").text();

				var depth = origin.find("depth");
				var depthvalue = depth.find("value").text();

				var status = origin.find("evaluationMode").text();

				var magnitude = event.find("magnitude");
				var typemag = magnitude.find("type").text();

				var mag = magnitude.find("mag");
				var valuemag = mag.find("value").text();

                                contenido = contenido + "<tr><td>" +status +"</td><td>" + type + ", " + text + "</td><td>" + timevalue + "</td><td>" + author + "</td><td>" + latitudevalue + "</td><td>" + longitudevalue + "</td><td>" +(parseInt(depthvalue)/1000) + "</td><td>" + typemag + "</td><td>" + valuemag + "</td></tr>"
			});
			$("#tabla").html(contenido);
			$('#tabla_general').show();
		},

		error : function(xhr, status) {
			alert('Disculpe, existió un problema');
		},

		complete : function(xhr, status) {
			// alert('Petición realizada');
		}/*, 
	
		beforeSend: function ( xhr ) {
        xhr.setRequestHeader('Access-Control-Allow-Headers', '*');
		xhr.setRequestHeader("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
    //xhr.setRequestHeader("Access-Control-Allow-Methods","POST, GET, OPTIONS, DELETE, PUT, HEAD");

    }*/
	});
}

function construirJson() {

	var win = window.open('mapa.html?c='+url1, '_blank');
			win.focus();
}





