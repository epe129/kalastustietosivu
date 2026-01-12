<!-- luodaan yhteys tietokantaan -->
<?php
$serverinnimi = "localhost";
$kayttajannimi = "kalastustietosivu";
$salasana = "2007";
$dbnimi = "kalastustietosivu";
// yhteys tietokantaan
$yhteys = new mysqli($serverinnimi, $kayttajannimi, $salasana, $dbnimi);
// tarkistaa että yhteys toimii
if ($yhteys->connect_error) {
    echo "Yhteyden muodostaminen epäonnistui";
}
?>
<!DOCTYPE html>
<html>
    <head>
        <style>
            .otsikko {
                text-align: center;
                font-size: 2.5rem;
            }

            .main {
                margin-left: auto;
                margin-right: auto;
                width: fit-content;
            }

            .main div {
                padding: 20px;
                float: left;
            }
        </style>
    </head>
<body>
    <h1 class="otsikko">Kalastustietoja</h1> 

    <div class="main">

        <div>
            <h2>Kalat painon mukaan</h2>
            <?php

            // haetaan dataa tietokannasta
            $sql_hae = "SELECT laji, paino FROM kala ORDER BY paino DESC";

            
            $tulos = $yhteys->query($sql_hae);

            // tarkistaa että tivejä on enemmän kuin nolla
            if ($tulos->num_rows > 0) {
                while($rivi = $tulos->fetch_assoc()) {
                    echo $rivi["laji"]. " ".$rivi["paino"]." kg"."<br/>";
                }
            } else {
                echo "Mitään ei löytynyt";
            }            
            ?>
        </div>
        
        <div>
            <h2>Kalat pituuden mukaan</h2>
            <?php
            
            // haetaan dataa tietokannasta
            $sql_hae = "SELECT laji, pituus FROM kala ORDER BY pituus DESC";

            
            $tulos = $yhteys->query($sql_hae);

            // tarkistaa että tivejä on enemmän kuin nolla
            if ($tulos->num_rows > 0) {
                while($rivi = $tulos->fetch_assoc()) {
                    echo $rivi["laji"]. " ".$rivi["pituus"]." cm"."<br/>";
                }
            } else {
                echo "Mitään ei löytynyt";
            }
            
            ?>
        </div>

        
        <div>
            <h2>Kalat saanti määrät</h2>
            <?php
            
            // haetaan dataa tietokannasta
            $sql_hae = "SELECT laji, COUNT(laji) as maara FROM kala GROUP BY laji ORDER BY maara DESC";

            $tulos = $yhteys->query($sql_hae);

            // tarkistaa että tivejä on enemmän kuin nolla
            if ($tulos->num_rows > 0) {
                while($rivi = $tulos->fetch_assoc()) {
                    echo $rivi["laji"]. " ".$rivi["maara"]."<br/>";
                }
            } else {
                echo "Mitään ei löytynyt";
            }

            ?>
        </div>

    </div>
</body>
</html>