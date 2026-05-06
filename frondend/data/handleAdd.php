<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
  $laji = htmlspecialchars($_POST["laji"]);
  $pituus = htmlspecialchars($_POST["pituus"]);
  $paino = htmlspecialchars($_POST["paino"]);
  $paikka = htmlspecialchars($_POST["paikka"]);
  $aika = htmlspecialchars($_POST["aika"]);
  $viehe = htmlspecialchars($_POST["viehe"]);
  $vapa = htmlspecialchars($_POST["vapa"]);
  echo $laji;
  echo $pituus;
  echo $paino;
  echo $paikka;
  echo $aika;
  echo $viehe;
  echo $vapa;


  $sql = 'INSERT INTO tarppi (aika, kalastaja_id, viehe_id, vapa_id, paikka) VALUES ("{aika}", "{kalastaja_id}", "{viehe_id}", "{vapa_id}", "{paikka}")';
  $sql = 'INSERT INTO kala (tarppi_id, pituus, paino, laji_id) VALUES ("{tarppi_id}", "{pituus}", "{paino}", "{laji_id}")';

  }
?>