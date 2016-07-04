<?php
   class MyDB extends SQLite3
   {
      function __construct()
      {
         $this->open('../py/disponiblidad.db');
      }
   }

   $db = new MyDB();
   if(!$db){
      echo $db->lastErrorMsg();
   } else {
      echo "Opened database successfully\n";
   }

   $sql =<<<EOF
      SELECT * from funcionamiento where fecha="2016-06-17";
EOF;

   $ret = $db->query($sql);
   while($row = $ret->fetchArray(SQLITE3_ASSOC) ){
      echo "net= ". $row['net'] . "\n";
      echo "sta = ". $row['sta'] ."\n";
      echo "fecha = ". $row['fecha'] ."\n";
      echo "fun =  ".$row['fun'] ."\n<br>";
   }
   echo "Operation done successfully\n";
   $db->close();
?>