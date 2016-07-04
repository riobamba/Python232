var rsnc= [];
var rnac=[];
var inter=[];

function consulta_allstations(fecha) {
    rsnc= [];
    rnac=[];
    inter=[];
    //alert(fecha)
    $.ajax({
        url: 'php/allstations.php',


        data: {
            dia: fecha
        },

        type: 'POST',

        dataType: 'json',

        success: function(json) {
            valida_allstations(json);
        },

        error: function(xhr, status) {
            alert('Disculpe, existió un problema');
        },

        complete: function(xhr, status) {
            //alert('Petición realizada');
        }
    });
}

function escribe(datos){

$.ajax({
        url: 'php/escribe.php',


        data: {
            data: datos
        },

        type: 'POST',

        dataType: 'json',

        success: function() {
            alert('Archivo generado correctamente')
        },

        error: function(xhr, status) {
           // alert('Disculpe, existió un problem al escribir un archivo');
        },

        complete: function(xhr, status) {
            //alert('Petición realizada');
        }
    });


}

function valida_allstations(all) {
    
    $.getJSON('http://10.100.100.13:8081/query/stations.json', function(data) {
        for (var i = 0; i < data.Inventory.network.length; i++) {
            var dataEstacion = data.Inventory.network[i].station;
            var red=data.Inventory.network[i].code;
            for (var j = 0; j< dataEstacion.length;j++) {
                //dataEstacion[j].latitude, dataEstacion[j].longitude,
                var longitude = dataEstacion[j].longitude;
                var latitude = dataEstacion[j].latitude;
                var nameEstation = dataEstacion[j].code;
                var code= "";
                var codes=new Array();
                var sensorLocation = dataEstacion[j].sensorLocation;
                var encontrado=false;
                
                for(var n = 0; n<sensorLocation.length;n++){
                     codes.push(sensorLocation[n].code);
                }
                if (filtrarEstaciones(nameEstation)==false) {
                for (var o = 0; o < codes.length; o++) {
                    code=codes[o];
                    for (var m = 0; m < all.length; m++) {
                        //if(nameEstation=="ROSC"){
                         // code="00"  ;
                        //}
                    var dato={};

                    
                    if(all[m].station==nameEstation && all[m].loc==code){
                        
                        if ((red=="CM" && parseFloat(all[m].average) > 0) && (code=="00" || code=="20") ){
                            dato["station"]=nameEstation;
                            dato["longitude"]=longitude;
                            dato["latitude"]=latitude;
                            dato["funcionamiento"]=all[m].average;
                            rsnc.push(dato);
                            encontrado=true;
                        }

                        if ((red=="CM" && parseFloat(all[m].average) > 0) && (code=="") ){
                            dato["station"]=nameEstation;
                            dato["longitude"]=longitude;
                            dato["latitude"]=latitude;
                            dato["funcionamiento"]=all[m].average;
                            rsnc.push(dato);
                            encontrado=true;
                        }



                        if ((red=="CM" && parseFloat(all[m].average) > 0) && (code=="10" ) ){
                            dato["station"]=nameEstation;
                            dato["longitude"]=longitude;
                            dato["latitude"]=latitude;
                            dato["funcionamiento"]=all[m].average;
                            rnac.push(dato);
                            encontrado=true;
                        }
                         if ((red!="CM" && parseFloat(all[m].average) > 0)  ){
                            dato["station"]=nameEstation;
                            dato["longitude"]=longitude;
                            dato["latitude"]=latitude;
                            dato["funcionamiento"]=all[m].average;
                            inter.push(dato);
                            encontrado=true;
                        }
                        
                    }
                }
                if (encontrado==false) {
                    
                    var dato={};
                      if (red=="CM"  && (code=="00" || code=="20")){
                            dato["station"]=nameEstation;
                            dato["longitude"]=longitude;
                            dato["latitude"]=latitude;
                            dato["funcionamiento"]="0";
                            rsnc.push(dato);  
                            }
                        if (red=="CM"  && (code=="10" )){
                            dato["station"]=nameEstation;
                            dato["longitude"]=longitude;
                            dato["latitude"]=latitude;
                            dato["funcionamiento"]="0";
                            rnac.push(dato);  
                            }
                        if (red!="CM" && code=="" ){
                            dato["station"]=nameEstation;
                            dato["longitude"]=longitude;
                            dato["latitude"]=latitude;
                            dato["funcionamiento"]="0";
                            inter.push(dato);  
                            }
                }

                }

                }
                
               
            };

        };
        escribeFuncionamiento();
    })


}
var repetidas=new Array();
function escribeFuncionamiento(){
    var addInter='-72.31 7.86 0.0 ## CAPV   <br>'+
'-77.33 0.14 0.0 ## CASC   <br>'+
'-84.95 10.29 99.0 ## JTS  <br>'+
'-59.97 -0.73 0.0 ## PTGA  <br>'+
'-80.03 0.78 0.0 ## PTGL   <br>'+
'-63.18 -8.95 0.0 ## SAML  <br>'+
'-70.63 8.88 99.0 ## SDV   <br>'+
'-66.15 18.11 99.0 ## SJG  <br>'+
'-88.28 20.23 0.0 ## TEIG  <br>';
    var addInterSta='CAPV<br>'+
'CASC<br>'+
'JTS <br>'+
'PTGA<br>'+
'PTGL<br>'+
'SAML<br>'+
'SDV <br>'+
'SJG <br>'+
'TEIG<br>';
    var addInterVal='0.0<br>'+
'0.0<br>'+
'99.0<br>'+
'0.0<br>'+
'0.0<br>'+
'0.0<br>'+
'99.0<br>'+
'99.0<br>'+
'0.0<br>';
    var addRnac='-74.09 4.64 0.0 ## REAC   <br>';

    sortByKey(rsnc, "station");
    sortByKey(rnac, "station");
    sortByKey(inter, "station");
    var sol=0;
    var vil=0;
    var zar=0;
    var dat="";
    repetidas=new Array();
    for (var i = 0; i < rsnc.length; i++) {
        if(verificarRepetidas(rsnc[i].station)==false){
            if (rsnc[i].station=="LL1C"  || rsnc[i].station=="LL5C" || rsnc[i].station=="LL6C" ) {
            $("#sub").append((parseFloat(rsnc[i].longitude)).toFixed(2)+"   "+(parseFloat(rsnc[i].latitude)).toFixed(2)+" "+(parseFloat(rsnc[i].funcionamiento).toFixed(1))+" ## "+rsnc[i].station+"<br>");
            $("#subl").append(rsnc[i].station+"<br>");
            $("#subp").append(rsnc[i].funcionamiento+"<br>");
	    dat=dat+(parseFloat(rsnc[i].longitude)).toFixed(2)+" "+(parseFloat(rsnc[i].latitude)).toFixed(2)+" "+(parseFloat(rsnc[i].funcionamiento).toFixed(1))+" ## "+rsnc[i].station+"&";
        }else{
		
                $("#rsnc").append((parseFloat(rsnc[i].longitude)).toFixed(2)+"   "+(parseFloat(rsnc[i].latitude)).toFixed(2)+" "+(parseFloat(rsnc[i].funcionamiento).toFixed(1))+" ## "+rsnc[i].station+"<br>");
                $("#rsncl").append(rsnc[i].station+"<br>");
                $("#rsncp").append(rsnc[i].funcionamiento+"<br>");
		dat=dat+(parseFloat(rsnc[i].longitude)).toFixed(2)+" "+(parseFloat(rsnc[i].latitude)).toFixed(2)+" "+(parseFloat(rsnc[i].funcionamiento).toFixed(1))+" ## "+rsnc[i].station+"&";

            
        }
        }
        repetidas.push(rsnc[i].station)
        
    }
	dat=dat+"------&";
    repetidas=new Array();
    for (var i = 0; i < rnac.length; i++) {
        if(verificarRepetidas(rnac[i].station)==false){
        $("#rnac").append((parseFloat(rnac[i].longitude)).toFixed(2)+"  "+(parseFloat(rnac[i].latitude)).toFixed(2)+" "+(parseFloat(rnac[i].funcionamiento).toFixed(1))+" ## "+rnac[i].station+"<br>");
        $("#rnacl").append(rnac[i].station+"<br>");
        $("#rnacp").append(rnac[i].funcionamiento+"<br>");
	dat=dat+(parseFloat(rnac[i].longitude)).toFixed(2)+" "+(parseFloat(rnac[i].latitude)).toFixed(2)+" "+(parseFloat(rnac[i].funcionamiento).toFixed(1))+" ## "+rnac[i].station+"&";

        }
        repetidas.push(rnac[i].station)
        
    }
    $("#rnac").append(addRnac);

	dat=dat+"------&";	
    repetidas=new Array();
    for (var i = 0; i < inter.length; i++) {
        if(verificarRepetidas(inter[i].station)==false){
        $("#inter").append((parseFloat(inter[i].longitude)).toFixed(2)+"   "+(parseFloat(inter[i].latitude)).toFixed(2)+" "+(parseFloat(inter[i].funcionamiento).toFixed(1))+" ## "+inter[i].station+"<br>");
        if(filtrarObservatorios(inter[i].station)==false){
        $("#interl").append(inter[i].station+"<br>");
        $("#interp").append(inter[i].funcionamiento+"<br>");
	dat=dat+(parseFloat(inter[i].longitude)).toFixed(2)+" "+(parseFloat(inter[i].latitude)).toFixed(2)+" "+(parseFloat(inter[i].funcionamiento).toFixed(1))+" ## "+inter[i].station+"&";

        }
        }
        repetidas.push(inter[i].station)
    }
    $("#inter").append(addInter)
    $("#interl").append(addInterSta)
    $("#interp").append(addInterVal)

    $('#carga').hide();
    $( "#ini" ).prop( "disabled", false );

    escribe(dat);
    
}

function sortByKey(array, key) {
    return array.sort(function(a, b) {
        var x = a[key]; var y = b[key];
        return ((x < y) ? -1 : ((x > y) ? 1 : 0));
    });
}

function filtrarEstaciones(nomEstacion){
    var estacionesFuera=["PUAC","AGCC","MORC","MORC","SNPBC","SNPBC","VMM05","VMM06","VMM07","VMM09","VMM10","EZNC","LL2C","LL3C","LL4C","PGA4","PGA5","SA1C","SA2C","ACON","ANWB","AUCA","BBGH","BONI","CNGN","CRIN","GRGR","GRTK","MASN","REFF"]
    for (var i = 0; i < estacionesFuera.length; i++) {
          if (estacionesFuera[i]==nomEstacion) {
            return true;
          }
      } 

      return false; 
}
 function verificarRepetidas(nombre){
    for (var i = 0; i < repetidas.length; i++) {
        if(repetidas[i]==nombre){
            return true;
        }
    }
    return false;
 }

 function filtrarObservatorios(nomEstacion){
   /* var estacionesFuera=["MARP","SOTA","PCON","ANIL","ELA","GCUF"]
    for (var i = 0; i < estacionesFuera.length; i++) {
          if (estacionesFuera[i]==nomEstacion) {
            return true;
          }
      } */

      return false; 

 }
