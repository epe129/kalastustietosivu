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
$lajit = array("ahven", "harjus", "hauki", "jokirapu", "kiiski", "kirjolohi", "kolmipiikki", "kuha", "kuore", "lahna", "lohi", "made", "muikku", "pasuri", "rautu", "ruutana", "salakka", "särki", "säyne", "siika", "silakka", "sorva", "suutari", "taimen", "täplärapu");
$sql_hae = "SELECT laji, COUNT(laji) as maara FROM laji GROUP BY laji ORDER BY maara DESC";
$tulos = $yhteys->query($sql_hae);
if ($tulos->num_rows > 0) {
    // lisää laji arrayhyn jos lajia ei ole array:ssa
    while($rivi = $tulos->fetch_assoc()) {
        if (in_array($rivi["laji"], $lajit))
            {
                null;
            } else {
                array_push($lajit, $rivi["laji"]);
            }
    }
}
?>
<!DOCTYPE html>
<html style="background-image: url('tausta2.jpg'); background-repeat: no-repeat; background-size: 100% 100%; height: 100%;">
    <head>
        <!-- <link rel="stylesheet" href="style.css"> -->
        <!-- <script src="script.js"></script> -->
        <style>
            .otsikko {
                text-align: center;
                font-size: 3rem;
            }

            .show {
                margin: 0 auto;
                position: relative;
                padding: 20px;
                font-size: 1.5rem;
                height: 100%;
                width: 450px;
                display: none;
                border: 1px solid gray;
                border-radius: 5px;
                box-shadow: 2px 2px 5px black;
                background-color: white;
            }

            .main {
                margin: 0 auto;
                position: relative;
                height: 100%;
                width: 100%;
                display: none;
            }

            h2 {
                font-size: 2rem;
            }
        </style>
        <script>
            // näyttää diat aina noin 1000 millisekunnin välein
            let nayttaa = 0;
            let div_numero = 1;
            let display = setInterval(Nayta, 1000);
            function Nayta() {
                nayttaa += 1
                document.getElementById(div_numero).style.display = "block";
                document.getElementById("main").style.display = "block";
                if (nayttaa == 12) {
                    console.log("vaihtu")
                    document.getElementById(div_numero).style.display = "none";
                    document.getElementById("main").style.display = "none";
                    VaihdaDiv()
                }
            }
            function VaihdaDiv() {
                div_numero += 1
                nayttaa = 0
                if (div_numero == 6) {
                    div_numero = 1
                }
            }
        </script>
    </head>
<body>
    <h1 class="otsikko">Kalastustietoja</h1> 
    <div id="main" class="main">
        <div id="1" class="show">
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
                    if (in_array($rivi["laji"], array_slice($lajit, 0,25)))
                    {
                        echo "<img src='./kuvat/$lajiKuvaHaku.jpg' width='50' height='25'> ";   
                    } else {
                        echo "🐟";
                    }
                    if ($rivien_maarat == 1) {
                        echo "🥇".$rivi["laji"]. " ".$rivi["paino"]." kg"."<br/>";
                    } else if ($rivien_maarat == 2) {
                        echo "🥈".$rivi["laji"]. " ".$rivi["paino"]." kg"."<br/>";
                    } else if ($rivien_maarat == 3) {
                        echo "🥉".$rivi["laji"]. " ".$rivi["paino"]." kg"."<br/>";
                    } else {
                        echo $rivi["laji"]. " ".$rivi["paino"]." kg"."<br/>";
                    }
                }
            } else {
                echo "Mitään ei löytynyt";
            }            
            ?>
        </div>
        <div id="2" class="show">
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
                    if (in_array($rivi["laji"], array_slice($lajit, 0,25)))
                    {
                        echo "<img src='./kuvat/$lajiKuvaHaku.jpg' width='50' height='25'> ";   
                    } else {
                        echo "🐟";
                    }
                    if ($rivien_maarat == 1) {
                        echo "🥇".$rivi["laji"]. " ".$rivi["pituus"]." cm"."<br/>";
                    } else if ($rivien_maarat == 2) {
                        echo "🥈".$rivi["laji"]. " ".$rivi["pituus"]." cm"."<br/>";
                    } else if ($rivien_maarat == 3) {
                        echo "🥉".$rivi["laji"]. " ".$rivi["pituus"]." cm"."<br/>";
                    } else {
                        echo $rivi["laji"]. " ".$rivi["pituus"]." cm"."<br/>";
                }
            }
            } else {
                echo "Mitään ei löytynyt";
            }
            ?>
        </div>
        <div id="3" class="show">
            <h2>Kalalajien saanti määrät</h2>
            <?php
            // haetaan dataa tietokannasta
            $sql_hae = "SELECT laji, COUNT(laji) as maara FROM laji GROUP BY laji ORDER BY maara DESC";
            $tulos = $yhteys->query($sql_hae);
            // tarkistaa että tivejä on enemmän kuin nolla
            if ($tulos->num_rows > 0) {
                // lisää laji arrayhyn jos lajia ei ole array:ssa
                while($rivi = $tulos->fetch_assoc()) {
                    $lajiKuvaHaku = $rivi["laji"];
                    if (in_array($rivi["laji"], array_slice($lajit, 0,25)))
                    {
                        echo "<img src='./kuvat/$lajiKuvaHaku.jpg' width='50' height='25'> ";   
                    } else {
                        echo "🐟";
                    }
                    echo $rivi["laji"]. " ".$rivi["maara"]." kpl"."<br/>";
                }
            } else {
                echo "Mitään ei löytynyt";
            }
            ?>
        </div>
        <div id="4" class="show">
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
        <div id="5" class="show">
            <h2>Kalalajien saanti määrät eri vieheillä</h2>
            <?php
            // käy lajit arraysta
            foreach ($lajit as $x) {
                $tulos = $yhteys->query("SELECT COUNT(laji) AS maara, laji, viehe FROM viehe, tarppi, kala, laji WHERE viehe.id=tarppi.viehe_id AND tarppi.id=kala.tarppi_id AND kala.laji_id=laji.id AND laji='$x' GROUP BY viehe;");
                // tarkistaa että tivejä on enemmän kuin nolla
                if ($tulos->num_rows > 0) {
                    while($rivi = $tulos->fetch_assoc()) {
                        $lajiKuvaHaku = $rivi["laji"];
                        if (in_array($rivi["laji"], array_slice($lajit, 0,25)))
                        {
                            echo "<img src='./kuvat/$lajiKuvaHaku.jpg' width='50' height='25'> ";   
                        } else {
                            echo "🐟";
                        }
                        echo $rivi["laji"]. " ".$rivi["viehe"]. " ".$rivi["maara"]." kpl"."<br/>";
                    }
                } 
            }
            ?>
        </div>
    </div>
</body>
</html>