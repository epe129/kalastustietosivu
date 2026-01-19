// näyttää diat aina noin 800 millisekunnin välein
let nayttaa = 0;
let div_numero = 1;
let display = setInterval(display_1, 1000);
function display_1() {
    nayttaa += 1
    document.getElementById(div_numero).style.display = "block";
    if (nayttaa == 10) {
        console.log("vaihtu")
        document.getElementById(div_numero).style.display = "none";
        myStopFunction()
    }
}
function myStopFunction() {
    div_numero += 1
    nayttaa = 0
    if (div_numero == 6) {
        div_numero = 1
    }
}