<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
  $laji = htmlspecialchars($_POST["laji"]);



  $sql = 'INSERT INTO tarppi (aika, kalastaja_id, viehe_id, vapa_id, paikka) VALUES ("{aika}", "{kalastaja_id}", "{viehe_id}", "{vapa_id}", "{paikka}")';
  $sql = 'INSERT INTO kala (tarppi_id, pituus, paino, laji_id) VALUES ("{tarppi_id}", "{pituus}", "{paino}", "{laji_id}")';

  }
?>