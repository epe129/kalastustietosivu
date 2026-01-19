<?php
// luodaan yhteys tietokantaan 
// saa configista databasen yhteyden luomiseen arvot
$configs = include('config.php');
$serverinnimi = $configs["serverinnimi"];
$kayttajannimi = $configs["kayttajannimi"];
$salasana = $configs["salasana"];
$dbnimi = $configs["dbnimi"];
// yhteys tietokantaan
$yhteys = new mysqli($serverinnimi, $kayttajannimi, $salasana, $dbnimi);
// tarkistaa että yhteys toimii
if ($yhteys->connect_error) {
    echo "Yhteyden muodostaminen epäonnistui";
}
$lajit = array("Ahven", "Hauki", "Kuha", "Siika", "Taimen", "Made", "Lohi");
?>
<!DOCTYPE html>
<html>
    <head>
        <link rel="stylesheet" href="style.css">
        <script src="script.js"></script>
    </head>
<body>
    <h1 class="otsikko">Kalastustietoja</h1> 
    <div id="1">
        <h2>Kalat painon mukaan</h2>
        <?php
        // haetaan dataa tietokannasta
        $sql_hae = "SELECT laji, paino FROM kala, laji WHERE kala.laji_id=laji.id ORDER BY paino DESC";
        $rivien_maarat = 0;
        $tulos = $yhteys->query($sql_hae);
        // tarkistaa että tivejä on enemmän kuin nolla
        if ($tulos->num_rows > 0) {
            while($rivi = $tulos->fetch_assoc()) {
                $rivien_maarat += 1;
                $lajiKuvaHaku = $rivi["laji"];
                if (in_array($rivi["laji"], array_slice($lajit, 0,7)))
                {
                    echo "<img src='./kuvat/$lajiKuvaHaku.jpg' alt='Ei ole kuvaa' width='50' height='25'> ";   
                } 
                if ($rivien_maarat == 1) {
                    echo $rivi["laji"]. " ".$rivi["paino"]." kg"."🥇"."<br/>";
                } else if ($rivien_maarat == 2) {
                    echo $rivi["laji"]. " ".$rivi["paino"]." kg"."🥈"."<br/>";
                } else if ($rivien_maarat == 3) {
                    echo $rivi["laji"]. " ".$rivi["paino"]." kg"."🥉"."<br/>";
                } else {
                    echo $rivi["laji"]. " ".$rivi["paino"]." kg"."<br/>";
                }
            }
        } else {
            echo "Mitään ei löytynyt";
        }            
        ?>
    </div>
    <div id="2">
        <h2>Kalat pituuden mukaan</h2>
        <?php
        // haetaan dataa tietokannasta
        $sql_hae = "SELECT laji, pituus FROM kala, laji WHERE kala.laji_id=laji.id ORDER BY pituus DESC";
        $rivien_maarat = 0;
        $tulos = $yhteys->query($sql_hae);
        // tarkistaa että tivejä on enemmän kuin nolla
        if ($tulos->num_rows > 0) {
            while($rivi = $tulos->fetch_assoc()) {
                $rivien_maarat += 1;
                $lajiKuvaHaku = $rivi["laji"];
                if (in_array($rivi["laji"], array_slice($lajit, 0,7)))
                {
                    echo "<img src='./kuvat/$lajiKuvaHaku.jpg' alt='Ei ole kuvaa' width='50' height='25'> ";   
                } 
                if ($rivien_maarat == 1) {
                    echo $rivi["laji"]. " ".$rivi["pituus"]." cm"."🥇"."<br/>";
                } else if ($rivien_maarat == 2) {
                    echo $rivi["laji"]. " ".$rivi["pituus"]." cm"."🥈"."<br/>";
                } else if ($rivien_maarat == 3) {
                    echo $rivi["laji"]. " ".$rivi["pituus"]." cm"."🥉"."<br/>";
                } else {
                    echo $rivi["laji"]. " ".$rivi["pituus"]." cm"."<br/>";
            }
        }
        } else {
            echo "Mitään ei löytynyt";
        }
        ?>
    </div>
    <div id="3">
        <h2>Kalalajien saanti määrät</h2>
        <?php
        // haetaan dataa tietokannasta
        $sql_hae = "SELECT laji, COUNT(laji) as maara FROM laji GROUP BY laji ORDER BY maara DESC";
        $tulos = $yhteys->query($sql_hae);
        // tarkistaa että tivejä on enemmän kuin nolla
        if ($tulos->num_rows > 0) {
            // lisää laji arrayhyn jos lajia ei ole array:ssa
            while($rivi = $tulos->fetch_assoc()) {
                if (in_array($rivi["laji"], $lajit))
                {
                null;
                } else {
                    array_push($lajit, $rivi["laji"]);
                }
                $lajiKuvaHaku = $rivi["laji"];
                if (in_array($rivi["laji"], array_slice($lajit, 0,7)))
                {
                    echo "<img src='./kuvat/$lajiKuvaHaku.jpg' alt='Ei ole kuvaa' width='50' height='25'> ";   
                } 
                echo $rivi["laji"]. " ".$rivi["maara"]." kpl"."<br/>";
            }
        } else {
            echo "Mitään ei löytynyt";
        }
        ?>
    </div>
    <div id="4">
        <h2>Kalalajien saanti määrät eri vavoilla</h2>
        <?php
        // haetaan dataa tietokannasta
        $sql_hae = "SELECT vapa, COUNT(vapa) as maara FROM vapa GROUP BY vapa ORDER BY maara DESC";
        $tulos = $yhteys->query($sql_hae);
        // tarkistaa että tivejä on enemmän kuin nolla
        if ($tulos->num_rows > 0) {
            while($rivi = $tulos->fetch_assoc()) {
                echo $rivi["vapa"]. " ".$rivi["maara"]." kpl"."<br/>";
            }
        } else {
            echo "Mitään ei löytynyt";
        }
        ?>
    </div>
    <div id="5">
        <h2>Kalalajien saanti määrät eri vieheillä</h2>
        <?php
        // käy lajit arraysta
        foreach ($lajit as $x) {
            $tulos = $yhteys->query("SELECT COUNT(laji) AS maara, laji, viehe FROM viehe, tarppi, kala, laji WHERE viehe.id=tarppi.viehe_id AND tarppi.id=kala.tarppi_id AND kala.laji_id=laji.id AND laji='$x' GROUP BY viehe;");
            // tarkistaa että tivejä on enemmän kuin nolla
            if ($tulos->num_rows > 0) {
                while($rivi = $tulos->fetch_assoc()) {
                    $lajiKuvaHaku = $rivi["laji"];
                    if (in_array($rivi["laji"], array_slice($lajit, 0,7)))
                    {
                        echo "<img src='./kuvat/$lajiKuvaHaku.jpg' alt='Ei ole kuvaa' width='50' height='25'> ";   
                    } 
                    echo $rivi["laji"]. " ".$rivi["viehe"]. " ".$rivi["maara"]." kpl"."<br/>";
                }
            } 
        }
        ?>
    </div>
</body>
</html>



    <!-- <div id="5">
        <h2>Kalalajien saanti määrät eri vieheillä</h2>
        <?php            
        // haetaan dataa tietokannasta
        $sql_hae = "SELECT viehe, COUNT(viehe) as maara FROM viehe, tarppi, kala WHERE viehe.id=tarppi.viehe_id AND tarppi.id=kala.tarppi_id GROUP BY viehe ORDER BY maara DESC";
        $tulos = $yhteys->query($sql_hae);
        // tarkistaa että tivejä on enemmän kuin nolla
        if ($tulos->num_rows > 0) {
            while($rivi = $tulos->fetch_assoc()) {
                echo $rivi["viehe"]. " ".$rivi["maara"]." kpl"."<br/>";
            }
        } else {
            echo "Mitään ei löytynyt";
        }
        ?>
    </div> -->