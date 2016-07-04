<?php
header("Content-disposition: attachment; datos.txt");
header("Content-type: application/txt");
readfile("datos.txt");
?>
