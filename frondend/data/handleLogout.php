<?php
session_start();
// Poista kaikki istunnon muuttujat.
$_SESSION = array();
session_unset();
// tuhoaa istunnon.
session_destroy();
// Ohjaa käyttäjän takaisin kirjautumissivulle.
header("Location: ../login/index.php");
exit;
?>