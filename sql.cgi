#!/usr/pkg/bin/php


<?php

// PDO + SQLite
$pdo = new PDO('sqlite:res/bs.db');
$statement = $pdo->query("SELECT * FROM items ORDER BY RANDOM()");

$i=0;

while($row = $statement->fetch(PDO::FETCH_ASSOC)) {
 $i++;
 if($i > 4) {break;}
 //if($_GET["gen"] == 'w') {
 if($row['gen'][$i] == $_GET['gen'] || $_GET['gen'] == 'a' || !$_GET['gen']) {
 echo "<div style='display:inline-block;'>";
  echo "<div style='width:100%;margin:30px;' align='center'>";
   echo "<img align='center' src='res/items/";
    echo $row['img'];
    echo "' width='100px'>";
   echo "<br>";
   echo htmlentities($row['name']);
   echo "<br>";
  echo "</div>
 </div>";}
}
?>
