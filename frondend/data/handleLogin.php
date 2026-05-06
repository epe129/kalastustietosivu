<?php
session_start();
$configs = include('db_connection.php');
$name = $email = "";
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    unset( $_SESSION['errorMessageUser'] );
    $email = htmlspecialchars($_POST["email"]);
    $password = htmlspecialchars($_POST["password"]);
    if (empty($email) or empty($password)) {
        header("Location: ../login/index.php"); 
        exit;
        } else {
            $stmt = $conn->prepare("SELECT pword FROM kalastaja WHERE email=?");
            $stmt->bind_param("s", $email);
            $stmt->execute();
            $stmt->store_result();
            if ($stmt->num_rows > 0) {
                $stmt->bind_result($db_password);
                $stmt->fetch();
                if(password_verify($password, $db_password)) {
                    $sql = "SELECT nimi FROM kalastaja WHERE email='$email'";
                    $tulos = $conn->query($sql);
                    if ($tulos->num_rows > 0) {
                        while($rivi = $tulos->fetch_assoc()) {
                            $_SESSION["nimi"] = $rivi["nimi"];
                        }
                    }                    
                    $_SESSION["email"] = "$email";
                    header("Location: ../main/index.php"); 
                    exit;
                }
                else {
                    $_SESSION['errorMessageUser'] = true;
                    header("Location: ../login/index.php"); 
                    exit;
                }
            }
            else {
                $_SESSION['errorMessageUser'] = true;
                header("Location: ../login/index.php"); 
                exit;
            }
        }
    }
?>