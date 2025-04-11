<?php


$host = 'localhost';
$dbname = 'gestionstock';
$user = 'root';
$pwrd = '';
$encodage = 'utf8';


try {

  $conn = new PDO("mysql:dbname=$dbname;host=$host;charset=$encodage", $user, $pwrd,
  [PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION]);
} catch (PDOException $e) {

  echo "Conexxion Echoue !!" . $e->getmessage();

}
