<?php
// tarkistetaan että käyttäjä on kirjautunut
require "../data/handleLogin.php"; 
if (!isset($_SESSION['name'])) {
    header("Location: ../index.php");
    exit();
}
// luodaan yhteys tietokantaan 
// saa configista databasen yhteyden luomiseen arvot
session_start();
$configs = include('../data/config.php');
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
    // lisää lajin arrayhyn jos lajia ei ole array:ssa
    while($rivi = $tulos->fetch_assoc()) {
        if (in_array($rivi["laji"], $lajit))
            {
                null;
            } else {
                array_push($lajit, $rivi["laji"]);
            }
    }
}
$sql_hae = "SELECT diaNopeus FROM integraatiot;";
$tulos = $yhteys->query($sql_hae);
if ($tulos->num_rows > 0) {
    while($rivi = $tulos->fetch_assoc()) {
        // asettaa nopeuden divin vaihdolle tietokannasta 
        $_SESSION["nopeus"] =  $rivi["diaNopeus"];
    }
} else {
    // jos ei ole tietokannassa nopeutta laittaa tämän divin vaihdon nopeudeksi
    $_SESSION["nopeus"] =  5000;
}
?>
<!DOCTYPE html>
<html>
    <head>
        <link rel="stylesheet" href="main.css">
    </head>
<body>
    <h1 class="title">Kalastustietoja</h1> 
    <div class="main">
        <div class="show">
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
        <div class="show">
            <h2>Kalat pituuden mukaan</h2>
            <?php
            $sql_hae = "SELECT laji, pituus FROM kala, laji WHERE kala.laji_id=laji.id ORDER BY pituus DESC";
            $rivien_maarat = 0;
            $tulos = $yhteys->query($sql_hae);
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
        <div class="show">
            <h2>Kalalajien saanti määrät</h2>
            <?php
            $sql_hae = "SELECT laji, laji_id, COUNT(laji_id) as maara FROM kala, laji WHERE kala.laji_id=laji.id GROUP BY laji_id ORDER BY maara DESC";
            $tulos = $yhteys->query($sql_hae);
            if ($tulos->num_rows > 0) {
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
        <div class="show">
            <h2>Kalalajien saanti määrät eri vieheillä</h2>
            <?php
            $rivien_maarat = 0;
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
                        $rivien_maarat += 1;
                    }
                } 
            }
            // jos tulos on nolla
            if ($rivien_maarat == 0) {
                echo "Mitään ei löytynyt";
            }
            ?>
        </div>
        <div class="show">
            <h2>Kalalajien saanti määrät eri vavoilla</h2>
            <?php
            foreach ($lajit as $x) {
                $sql_hae = "SELECT COUNT(laji) AS maara, laji, vapa FROM vapa, tarppi, kala, laji WHERE vapa.id=tarppi.vapa_id AND tarppi.id=kala.tarppi_id AND kala.laji_id=laji.id AND laji='$x' GROUP BY vapa;";
                $tulos = $yhteys->query($sql_hae);
                if ($tulos->num_rows > 0) {
                    while($rivi = $tulos->fetch_assoc()) {
                        $lajiKuvaHaku = $rivi["laji"];
                        if (in_array($rivi["laji"], array_slice($lajit, 0,25)))
                        {
                            echo "<img src='./kuvat/$lajiKuvaHaku.jpg' width='50' height='25'> ";   
                        } else {
                            echo "🐟";
                        }
                        echo $rivi["laji"]. " ".$rivi["vapa"]. " ".$rivi["maara"]." kpl"."<br/>";
                        $rivien_maarat += 1;
                    }
                } 
            }
            // jos tulos on nolla
            if ($rivien_maarat == 0) {
                echo "Mitään ei löytynyt";
            }
            ?>
        </div>
    </div>
    <script>
        // javacsript on täällä sen takia jotta pystyy ottaa php tietokannasta div nopeuden
        let dia_nopeus = "";
        // divit vaihtuu aina tietokannasta saadun nopeuden mukaan joka on millisekuntteina 
        dia_nopeus = "<?php echo $_SESSION['nopeus']; ?>";
        console.log(dia_nopeus)
        let div_numero = 0;
        Nayta();
        // tekee slide shown
        function Nayta() {
            let i;
            let slides = document.getElementsByClassName("show");
            for (i = 0; i < slides.length; i++) {
                // asettaa että muut divit ei näy
                slides[i].style.display = "none";
            }
            div_numero++;
            // jos on kaikki käyty aloittaa alusta
            if (div_numero > slides.length) {div_numero = 1}
            // asettaa aina että yksi div näkyy
            slides[div_numero-1].style.display = "block"; 
            // kutsuu aina functiota määritetyn ajan välein
            setTimeout(Nayta, parseInt(dia_nopeus));
        }
    </script>
</body>
</html>