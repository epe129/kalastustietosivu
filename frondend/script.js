// näyttää diat aina noin 1000 millisekunnin välein
let nayttaa = 0;
let div_numero = 1;
let display = setInterval(Nayta, 1000);
function Nayta() {
    nayttaa += 1
    document.getElementById(div_numero).style.display = "block";
    document.getElementById("main").style.display = "block";
    if (nayttaa == 12) {
        console.log("vaihtu")
        document.getElementById(div_numero).style.display = "none";
        document.getElementById("main").style.display = "none";
        VaihdaDiv()
    }
}
function VaihdaDiv() {
    div_numero += 1
    nayttaa = 0
    if (div_numero == 6) {
        div_numero = 1
    }
}