<?php
session_start();
$db= include('db_connection.php');
$laji = $viehe = $vapa = "";
if ($_SERVER["REQUEST_METHOD"] == "POST") {
  unset( $_SESSION['SuccesfullAddMuu'] );
  unset( $_SESSION['ErrorAddMuu'] );
  unset( $_SESSION['TextMuu'] );
  unset( $_SESSION['AlreadyExistMuu'] );
  $array_arvot = array("laji", "viehe", "vapa");
  foreach ($array_arvot as $x) {
    $get_arvo = htmlspecialchars($_POST["$x"]);  
    if (strlen($get_arvo) != 0) {
      $_SESSION["TextMuu"] = "$x";
      $sql = "SELECT * FROM $x WHERE $x ='$get_arvo'";
      $result = $conn->query($sql);
      if ($result->num_rows > 0) {
        $_SESSION['AlreadyExistMuu'] = true;
        header("Location: ../main/lisaa.php");
        exit; 
        } else {
          $sql = "INSERT INTO $x ($x) VALUES ('$get_arvo')";
          if (mysqli_query($conn, $sql)) {
            $_SESSION["SuccesfullAddMuu"] = true;
            header("Location: ../main/lisaa.php"); 
            exit;
            } else {
              $_SESSION["ErrorAddMuu"] = true;
              header("Location: ../main/lisaa.php"); 
              exit;
              }
        }
        } else {
        continue;
      }
    }
  }
?>