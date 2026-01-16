<!-- luodaan yhteys tietokantaan -->
<?php
$serverinnimi = "localhost";
$kayttajannimi = "root";
$salasana = "";
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
                font-size: 3rem;
            }

            div {
                position: relative;
                padding: 20px;
                font-size: 1.5rem;
                height: 100%;
                width: auto;
                /* float: left; */
                display: none;
                border: 1px solid gray;
                border-radius: 5px;
            }

            h2 {
                font-size: 2rem;
            }

        </style>
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
            while($rivi = $tulos->fetch_assoc()) {
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
            
        // haetaan dataa tietokannasta
        $sql_hae = "SELECT viehe, COUNT(viehe) as maara FROM viehe, tarppi, kala WHERE viehe.id=tarppi.viehe_id AND tarppi.id=kala.tarppi_id GROUP BY viehe";

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
    </div>
        
    <div id="6">
        <h2>Kalalajien saanti määrät eri vieheillä</h2>
        <?php
        // haetaan dataa tietokannasta
        $sql_hae = "SELECT laji, viehe FROM viehe, tarppi, kala, laji WHERE viehe.id=tarppi.viehe_id AND tarppi.id=kala.tarppi_id AND kala.laji_id=laji.id";
            
        $tulos = $yhteys->query($sql_hae);

        // tarkistaa että tivejä on enemmän kuin nolla
        if ($tulos->num_rows > 0) {
            while($rivi = $tulos->fetch_assoc()) {
                echo $rivi["laji"]." ".$rivi["viehe"]."<br/>";
            }
        }

        ?>
    </div>

    <script>
        var nayttaa = 0;
        var div_numero = 1

        function aloitus () {
            display = setInterval(display_1, 500);
            
        }

        aloitus()
        
        function display_1() {
            nayttaa += 1
            document.getElementById(div_numero).style.display = "block";

            if (nayttaa == 10) {
                console.log(nayttaa)
                document.getElementById(div_numero).style.display = "none";
                myStopFunction()
            }
        }

        function myStopFunction() {
            div_numero += 1
            nayttaa = 0
            
            if (div_numero == 7) {
                div_numero = 1
            }
        }
    </script>
</body>
</html>