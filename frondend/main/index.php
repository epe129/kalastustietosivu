<?php
session_start();
// Saadaan yhteys tietokantaan 
$configs = include('../data/db_connection.php');
// tarkistetaan että käyttäjä on kirjautunut
if (!isset($_SESSION['email'])) {
    header("Location: ../index.php");
    exit();
}
$lajit = array("ahven", "harjus", "hauki", "jokirapu", "kiiski", "kirjolohi", "kolmipiikki", "kuha", "kuore", "lahna", "lohi", "made", "muikku", "pasuri", "rautu", "ruutana", "salakka", "särki", "säyne", "siika", "silakka", "sorva", "suutari", "taimen", "täplärapu");
$sql_hae = "SELECT laji, COUNT(laji) as maara FROM laji GROUP BY laji ORDER BY maara DESC";
$tulos = $conn->query($sql_hae);
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
$tulos = $conn->query($sql_hae);
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
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Kalastustiedot</title>
        <style>
            /* html css */
            html {
                background-image: url('../kuvat/tausta.jpg'); 
                background-repeat: no-repeat; 
                background-size: 100% 100%; 
                height: 100%;
            }
            /* otsikon css */
            .title {
                text-align: center;
                margin: auto;
                font-size: 3rem;
                color: black;
                background-color: white;
                border-radius: 5px;
                width: 350px;
                margin-top: 50px;
                margin-bottom: 55px;
            }
            /* main div css */
            .main {
                margin: 0 auto;
                position: relative;
                height: 100%;
                width: 100%;
            }
            /* show css */
            .show {
                margin: 0 auto;
                position: relative;
                padding: 20px;
                font-size: 1.5rem;
                height: 100%;
                width: 450px;
                border: 1px solid gray;
                border-radius: 5px;
                box-shadow: 2px 2px 5px black;
                background-color: white;
            }
            /* navbar css */
            ul {
                list-style-type: none;
                margin: 0;
                padding: 0;
                background-color: #333333;
                display: flex;
                border-radius: 5px;
                width: 100%;
            }
            ul li a {
                display: block;
                color: white;
                padding: 14px 16px;
                text-decoration: none;
            }
            ul li a:hover {
                background-color: #111111;
            }
        </style>
    </head>
<body>
    <!-- navbar -->
    <ul>
        <li><a href="index.php">Kalastustiedot</a></li>
        <li><a href="lisaa.php">Lisää kalastustietoja</a></li>
        <li>
            <?php
            echo $_SESSION["nimi"];
            ?>
        </li>
    </ul>
    <h1 class="title">Kalastustietoja</h1> 
    <div class="main">
        <div class="show">
            <h2 style="font-size: 2rem;">Kalat painon mukaan</h2>
            <?php
            // haetaan dataa tietokannasta
            $sql_hae = "SELECT laji, paino FROM kala, laji WHERE kala.laji_id=laji.id ORDER BY paino DESC";
            $rivien_maarat = 0;
            $tulos = $conn->query($sql_hae);
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
            $tulos = $conn->query($sql_hae);
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
            $tulos = $conn->query($sql_hae);
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
                $tulos = $conn->query("SELECT COUNT(laji) AS maara, laji, viehe FROM viehe, tarppi, kala, laji WHERE viehe.id=tarppi.viehe_id AND tarppi.id=kala.tarppi_id AND kala.laji_id=laji.id AND laji='$x' GROUP BY viehe;");
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
                $tulos = $conn->query($sql_hae);
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