<!-- luodaan yhteys tietokantaan -->
<?php
$configs = include('config.php');
$serverinnimi = $configs["serverinnimi"];
$kayttajannimi = $configs["kayttajannimi"];
$salasana = $configs["salasana"];
$dbnimi = $configs["dbnimi"];
// yhteys tietokantaan
$conn = new mysqli($serverinnimi, $kayttajannimi, $salasana, $dbnimi);
// tarkistaa että yhteys toimii
if ($conn->connect_error) {
    echo "Yhteyden muodostaminen epäonnistui";
}
?>