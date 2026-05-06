<!-- tee että tarkistaa onko sähköposti tietokannassa -->
<?php
session_start();
$configs = include('db_connection.php');
$name = $email = "";
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    unset( $_SESSION['errorMessage'] );
    unset( $_SESSION['AlreadyExist'] );
    $name = htmlspecialchars($_POST["name"]);
    $email = htmlspecialchars($_POST["email"]);
    $hash_password = password_hash(htmlspecialchars($_POST["password"]), PASSWORD_DEFAULT);
    // tarkistetaan onko sähköposti tietokannassa   
    $sql = "SELECT email FROM kalastaja WHERE email='$email'";
    $result = $conn->query($sql);
    if($result->num_rows > 0) {
        $_SESSION['AlreadyExist'] = true;
        header("Location: ../index.php"); 
        exit;
    }
    if (empty($name) or empty($email) or empty(htmlspecialchars($_POST["password"]))) {
        header("Location: ../index.php"); 
        exit;
        } else {
            $stmt = $conn->prepare("INSERT INTO kalastaja (nimi, email, pword) VALUES (?, ?, ?)");
            $stmt->bind_param("sss", $name, $email, $hash_password);

            if ($stmt->execute()) {
                $_SESSION["email"] = "$email";
                $_SESSION["nimi"] = "$name";
                header("Location: ../main/index.php"); 
                exit;
            } else {
                $_SESSION['errorMessage'] = true;
                header("Location: ../index.php"); 
                exit;
            }
        }
    }
?>