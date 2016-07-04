<?php
$data = $_POST['data'];
//$data="1&2&3&4&";
//echo $data;

$array=explode("&",$data);

foreach($array as $obj){
    $url = $url.$obj."\n";   

}


$file = fopen("datos.txt", "w");
                fwrite($file, $url . PHP_EOL);
                fclose($file);

?>
