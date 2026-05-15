<!-- tee että tarkistaa onko sähköposti tietokannassa -->
<?php
session_start();
// yhteyden tietokantaan
$db = include('db_connection.php');
$name = $email = "";
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // ei aseta muuttujaa vasta kun jos tulee vastaan if lauseessa
    unset($_SESSION['errorMessageRegister']);
    unset($_SESSION['errorTextRegister']);
    // saa arvot
    $name = stripslashes(trim(htmlspecialchars($_POST["name"])));
    $email = stripslashes(trim(htmlspecialchars($_POST["email"])));
    $password = stripslashes(trim(htmlspecialchars($_POST["password"])));
    
    // hashaa salasanan
    $hash_password = password_hash($password, PASSWORD_DEFAULT);
    // tarkistetaan onko sähköposti tietokannassa   
    $kysely_email = $conn->prepare("SELECT email FROM kalastaja WHERE email = ?");
    $kysely_email->bind_param("s", $email);
    $kysely_email->execute();
    $kysely_email->store_result();

    if($kysely_email->num_rows > 0) {
        // jos sähköposti on jo olemassa
        $_SESSION['errorMessageRegister'] = true;
        $_SESSION['errorTextRegister'] = "Sähköposti on jo käytössä";
        header("Location: ../index.php"); 
        exit;
    }

    // tarkistaa että nimi sisältää vaan kirjaimia ja numeroita
    if (!preg_match("/^[a-zA-Z0-9äöåÄÖÅ]+$/u",$name)) {
        $_SESSION["errorMessageRegister"] = true;
        $_SESSION['errorTextRegister'] = "Nimi ei ole kelvollinen, vain numerot ja kirjaimet ovat salittuja";
        header("Location: ../index.php"); 
        exit;
    }
    
    // tarkistaa ettei salasana ole liian lyhyt
    if (strlen($password) <=  7) {
        $_SESSION["errorMessageRegister"] = true;
        $_SESSION['errorTextRegister'] = "Salasanassa pitää olla vähintää 8 merkkiä";
        header("Location: ../index.php"); 
        exit;
    }

    // tarkistaa että email on valid
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $_SESSION["errorMessageRegister"] = true;
        $_SESSION['errorTextRegister'] = "Sähköposti ei ole kelvollinen";
        header("Location: ../index.php"); 
        exit;
    }

    if (empty($name) or empty($email) or empty($password)) {
        // jos jokin arvo on tyhjä
        header("Location: ../index.php"); 
        exit;
        } else {
            // lisää arvot tietokantaan ja tarkistaa että se onnistuu
            $stmt = $conn->prepare("INSERT INTO kalastaja (nimi, email, pword) VALUES (?, ?, ?)");
            $stmt->bind_param("sss", $name, $email, $hash_password);

            if ($stmt->execute() === TRUE) {
                // luodaan uusi session id käyttäjälle
                session_regenerate_id();
                $_SESSION["email"] = "$email";
                $_SESSION["nimi"] = "$name";
                header("Location: ../main/index.php"); 
                exit;
            } else {
                // jos epäonnistuu saa viestin
                $_SESSION['errorMessageRegister'] = true;
                $_SESSION['errorTextRegister'] = "Jokin meni pieleen";
                header("Location: ../index.php"); 
                exit;
            }
        }
    } else {
        header("Location: ../index.php"); 
        exit;
    }
?>