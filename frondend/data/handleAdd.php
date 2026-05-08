<?php
session_start();
$db = include('db_connection.php');
$laji = $pituus = $paino = $paikka = $aika = $viehe = $vapa = $email = "";
$kalastaja_id = $viehe_id = $vapa_id = $tarppi_id = $laji_id = 0;
if ($_SERVER["REQUEST_METHOD"] == "POST") {
  unset( $_SESSION['SuccesfullAdd'] );
  unset( $_SESSION['ErrorAdd'] );
  $laji = htmlspecialchars($_POST["laji"]);
  $pituus = htmlspecialchars($_POST["pituus"]);
  $paino = htmlspecialchars($_POST["paino"]);
  $paikka = htmlspecialchars($_POST["paikka"]);
  $aika = htmlspecialchars($_POST["aika"]);
  $viehe = htmlspecialchars($_POST["viehe"]);
  $vapa = htmlspecialchars($_POST["vapa"]);
  $email = $_SESSION["email"];
  $kysely1 = "SELECT id FROM kalastaja WHERE email ='$email'";
  $tulos1 = $conn->query($kysely1);
  $kysely2 = "SELECT id FROM vapa WHERE vapa ='$vapa'";
  $tulos2 = $conn->query($kysely2);
  $kysely3 = "SELECT id FROM viehe WHERE viehe ='$viehe'";
  $tulos3 = $conn->query($kysely3);
  $kysely4 = "SELECT id FROM laji WHERE laji ='$laji'";
  $tulos4 = $conn->query($kysely4);  
  if ($tulos1->num_rows > 0 and $tulos2->num_rows > 0 and $tulos3->num_rows > 0) {
    while($rivi = $tulos1->fetch_assoc()) {
      $kalastaja_id = $rivi["id"];
    }
    while($rivi2 = $tulos2->fetch_assoc()) {
      $vapa_id = $rivi2["id"];
    }
    while($rivi3 = $tulos3->fetch_assoc()) {
      $viehe_id = $rivi3["id"];
    }
    while($rivi4 = $tulos4->fetch_assoc()) {
      $laji_id = $rivi4["id"];
    }
  }
  $conn->query("INSERT INTO tarppi (aika, kalastaja_id, viehe_id, vapa_id, paikka) VALUES ('$aika', '$kalastaja_id', '$viehe_id', '$vapa_id', '$paikka')");
  $tarppi_id = $conn->insert_id;; 
  $sql = "INSERT INTO kala (tarppi_id, pituus, paino, laji_id) VALUES ('$tarppi_id', '$pituus', '$paino', '$laji_id')";
  if ($conn->multi_query($sql) === TRUE) {
    $_SESSION["SuccesfullAdd"] = true;
    header("Location: ../main/lisaa.php"); 
    exit;
    } else {
      $_SESSION["ErrorAdd"] = true;
      header("Location: ../main/lisaa.php"); 
      exit;
    }
  }

?>


  <!-- echo $laji;
  echo $pituus;
  echo $paino;
  echo $paikka;
  echo $aika;
  echo $viehe;
  echo $vapa;
   -->