// ottaa nyky ajan
let nyt = new Date();

function LaitaNykyAika() {
    // laittaa automaattisesti nykyajan aikaan
    nyt.setMinutes(nyt.getMinutes() - nyt.getTimezoneOffset());
    document.getElementById('aika').value = nyt.toISOString().slice(0,10);
    document.getElementById("aika").max = nyt.toISOString().slice(0,10);
}
LaitaNykyAika()

// jos input value on muu niin antaa teksti kentän
document.getElementsByName("laji")[0].addEventListener('change', Tee);

function Tee(){
    // saa arvon
    let arvo = document.getElementById("KalaLaji").value;
    console.log(arvo)
    // tarkistaa on muu
    if (arvo == "muu") {
        document.getElementById("laji_muu_div").style.display = "flex";
        document.getElementById("laji_muu_form").style.display = "flex";
        // jos muu valittu laittaa että arvo tarvitaan
        document.getElementById("lajiMuu").required = true;
    }
}