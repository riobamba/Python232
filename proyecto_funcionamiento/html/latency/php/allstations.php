

<?php
$dia = $_POST['dia'];
 include("conecta.php");
 $bd = conectar();
/*
$sql="SELECT waveformID_stationCode AS station, ROUND((SUM( value ) /24),2) AS average, waveformID_locationCode AS loc FROM WaveformQuality ".
"WHERE created LIKE  '".$dia."%' AND parameter =  'availability' AND waveformID_locationCode =  '10' AND waveformID_channelCode LIKE  '%Z' ".
"GROUP BY waveformID_stationCode UNION SELECT waveformID_stationCode AS station, ROUND((SUM( value ) /24),2) AS average, waveformID_locationCode ".
"AS loc FROM WaveformQuality WHERE created LIKE  '".$dia."%' AND parameter =  'availability' AND waveformID_locationCode =  '00' ".
"AND waveformID_channelCode LIKE  '%Z' GROUP BY waveformID_stationCode UNION SELECT waveformID_stationCode AS station, ROUND((SUM( value ) /24 ". 
"),2) AS average, waveformID_locationCode AS loc FROM WaveformQuality WHERE created LIKE  '".$dia."%' AND parameter =  'availability' ".
"AND waveformID_locationCode =  '20' AND waveformID_channelCode LIKE  '%Z' GROUP BY waveformID_stationCode UNION ".
"SELECT waveformID_stationCode AS station, ROUND((SUM( value ) /24),2) AS average, waveformID_locationCode AS loc FROM WaveformQuality ".
"WHERE created LIKE  '".$dia."%' AND parameter =  'availability' AND waveformID_locationCode =  '' AND waveformID_channelCode LIKE  '%Z' ".
"GROUP BY waveformID_stationCode LIMIT 0 , 300 ";
*/

$sql="SELECT waveformID_stationCode AS station, ROUND((SUM( value ) /24),2) AS average, waveformID_locationCode AS loc FROM WaveformQuality WHERE created LIKE  '".$dia."%' AND parameter =  'availability' AND waveformID_locationCode =  '10' AND (waveformID_channelCode LIKE  'ENZ' OR waveformID_channelCode LIKE  'HNZ') GROUP BY waveformID_stationCode UNION  SELECT waveformID_stationCode AS station, ROUND((SUM( value ) /24),2) AS average, waveformID_locationCode AS loc FROM WaveformQuality WHERE created LIKE  '".$dia."%' AND parameter =  'availability' AND waveformID_locationCode =  '00' AND waveformID_channelCode LIKE  'HHZ' GROUP BY waveformID_stationCode UNION  SELECT waveformID_stationCode AS station, ROUND((SUM( value ) /24),2) AS average, waveformID_locationCode AS loc FROM WaveformQuality WHERE created LIKE  '".$dia."%' AND parameter =  'availability' AND waveformID_locationCode =  '20' AND waveformID_channelCode LIKE  'EHZ' GROUP BY waveformID_stationCode UNION  SELECT waveformID_stationCode AS station, ROUND(( SUM( value ) /24 ),2) AS average, waveformID_locationCode AS loc FROM WaveformQuality WHERE created LIKE  '".$dia."%' AND parameter =  'availability' AND waveformID_locationCode =  '' AND (waveformID_channelCode LIKE  'HHZ' OR waveformID_channelCode LIKE  'BHZ') GROUP BY waveformID_stationCode UNION  SELECT waveformID_stationCode AS station, ROUND((SUM( value ) /24),2) AS average, waveformID_locationCode AS loc FROM WaveformQuality WHERE created LIKE  '".$dia."%' AND parameter =  'availability' AND waveformID_locationCode =  '10' AND waveformID_channelCode LIKE  'BHZ' GROUP BY waveformID_stationCode UNION  SELECT waveformID_stationCode AS station, ROUND(( SUM( value ) /24),2) AS average, waveformID_locationCode AS loc FROM WaveformQuality WHERE created LIKE  '".$dia."%' AND parameter =  'availability' AND waveformID_locationCode =  '00' AND (waveformID_channelCode LIKE  'HNZ' OR waveformID_channelCode LIKE  'BHZ') GROUP BY waveformID_stationCode LIMIT 0 , 300";

if ($bd != null){
$resultado = $bd->query($sql);
$funcionamiento = array(); 
$i=0;
$resultado->data_seek(0);
while ($fila = $resultado->fetch_assoc()) {
    //echo $fila['station'] ." ".$fila['average']." ".$fila['loc']. "<br>";
    $funcionamiento[$i] = $fila;
    $i++;
}
//return $funcionamiento;
 echo json_encode($funcionamiento);
}else{
        echo "Error de coneccion";
}


?>

