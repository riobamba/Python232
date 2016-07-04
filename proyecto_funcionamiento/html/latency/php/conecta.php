<?php
$ip="10.100.100.13";
$usr="consulta";
$pass="consulta";
$bd="seiscomp3";


function conectar(){

$bd1= new mysqli("10.100.100.232","consulta","consulta","seiscomp3");
if ($bd1->connect_errno) {
   return null;
//return "no se conecta";
}else{

   //return "se conecta";
    return $bd1;

}

}


?>

