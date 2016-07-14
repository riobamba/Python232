<?php
$url = $_POST['urlx'];
//$url ="http://10.100.100.232:8091/fdsnws/event/1/query?starttime=2016-07-03T07:27:27&endtime=2016-07-04T07:27:27&orderby=time&format=xml&nodata=404";

try {
        if (false !== ($xml = file_get_contents($url))) {
                echo $xml;
        } else {
                echo "Lo sentimos no hay información de respuesta para esta(s) componente(s)";
        }

} catch (Exception $e) {
        echo 'Excepción capturada: ', $e -> getMessage(), "\n";
}

?>

