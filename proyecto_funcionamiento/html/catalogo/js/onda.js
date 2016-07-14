var fechainionda = "";
var fechafinonda = "";
var estacion1 = "";
var canal = "";
var toda = "BAR2,BBAC,BET,BET,BRR,CAP2,CBOC,CHI,CRJC,CRU,CUM,DBB,ELA,FLO2,GARC,GCUF,GR1C,GUA,GUY2C,HEL,IMO,IPA,LCBC,LL1C,LL2C,LL4C,MACC,MAL," + "MAP,MARA,MON,NOR,OCA,ORTC,PAL,PAM,PCON,PIZC,POP2,PRA,PRV,PTA,PTB,PTGC,PTLC,RGC,ROSC,RUS,SJC,SMAR,SML,SOL,SOTA,SPBC,TAM,TOL,TUM," + "URE,URI,VIL,YOT,ZAR,REAC,AUA1,AZU,BCIP,CACAO,CAPV,CASC,CUSE,DABV,ELOV,GMAL,GTBY,JTS,LPAZ,MTDJ,OTAV,PAC1,PAYG,PNME,PTGA,PTGL,PTP," + "SAML,SDDR,SDV,SJG,SOCV,TBTG,TEIG,TGUH,TULM,UPA,UPD2,CARME,CBARI,CBET2,CBMAL,CBOG1,CBSOL,CCNEG,CCRUZ,CCUFI,CCUMB,CFLOR,CGAR2,CGR1C," + "CGUYA,CH4C,CIBA1,CMACA,CMAN1,CNIZA,CNOCA,COCAN,CORTC,CPALC,CPAM,CPAS1,CPAS2,CPBER,CPIZC,CPROV,CPTAR,CRECR,CROSA,CSTM1,CTAME," + "CTUM2,CTUM3,CURIB,CVALL,CYOTO,RACO2";

//var peticionOnda = "http://service.iris.edu/fdsnws/dataselect/1/query?net=IU&";
var peticionOnda = "http://10.100.100.232:8091/fdsnws/dataselect/1/query?net=CM&";
var urlOnda;
function construirConsultaOnda() {

	fechainionda = $("#dateinionda").val();
	if (fechainionda.length > 0) {
		fechainionda = "starttime=" + fechainionda.replace(" ", "T") + "&";
	}

	fechafinonda = $("#datefinonda").val();
	if (fechafinonda.length > 0) {
		fechafinonda = "endtime=" + fechafinonda.replace(" ", "T") + "&";
	}
	estacion = "";
	estacion1 = "";
	estacion = $("#datos1").val();
	if (estacion.length > 0) {
		if (estacion == "Todas") {
			estacion = "sta=" + toda + "&";
			estacion1 = "sta=Todas&";
			//estacion1 = "sta=*&";
		} else {
			estacion = "sta=" + estacion + "&";
			estacion1 = estacion;
		}

	}
	//alert(estacion)

	/*	estacion = "";
	 $("#datos1 option:selected").each(function() {
	 estacion += $(this).text() + ",";
	 });
	 estacion="sta=" +estacion.substring(0, estacion.length-1)+"&";
	 //alert(texto);
	 */

	canal = $("#canal").val();
	if (canal.length > 0) {
		canal = "cha=" + canal + "&";
	}

	urlOnda = peticionOnda + estacion + "loc=*&" + canal + fechainionda + fechafinonda + 'nodata=404';
	var mostrar=peticionOnda + estacion1 + "loc=*&" + canal + fechainionda + fechafinonda + 'nodata=404';
	$("#rutaonda").html('<a href="' + urlOnda + '" TARGET="_new">' + mostrar + '</a> ');

}

