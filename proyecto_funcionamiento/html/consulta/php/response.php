<?php
$net = $_POST['netw'];
$cha = $_POST['cha'];
$sta = $_POST['sta'];

$cha2=str_replace("&", ",", $cha);
$url ="http://10.100.100.232:8091/fdsnws/station/1/query?net=".$net."&sta=".$sta."&loc=*&cha=".$cha2."&level=response&format=xml&includecomments=true&nodata=404";



$file = fopen("../data/log.xml", "w");
		fwrite($file, $url . PHP_EOL);
		fclose($file);

try {
	if (false !== ($xml = file_get_contents($url))) {
		$file = fopen("../data/response.xml", "w");
		fwrite($file, $xml . PHP_EOL);
		fclose($file);
		echo "ok";
	} else {
		echo "Lo sentimos no hay información de respuesta para esta(s) componente(s)";
	}

} catch (Exception $e) {
	echo 'Excepción capturada: ', $e -> getMessage(), "\n";
}
?>