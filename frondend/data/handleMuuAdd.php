<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
  $laji = htmlspecialchars($_POST["laji"]);
  $viehe = htmlspecialchars($_POST["viehe"]);
  $vapa = htmlspecialchars($_POST["vapa"]);

  if (strlen($laji) != 0) {    
    $sql = "SELECT * FROM laji WHERE laji ='$laji'";
    $result = $conn->query($sql);
    if ($result->num_rows > 0) {
        header("Location: ../main/lisaa.php"); 
    } else {
        $sql = "INSERT INTO laji (id, laji) VALUES ('id', '$laji')";
        if (mysqli_query($conn, $sql)) {
            header("Location: ../main/lisaa.php"); 
        } else {
            header("Location: ../main/lisaa.php"); 
        }
    }
  }

  if (strlen($viehe) != 0) {
    echo "viehe";
  }
  
  if (strlen($vapa) != 0) {
    echo "vapa";
  }
}
?>