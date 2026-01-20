// ottaa nyky ajan
let nyt = new Date();

function LaitaNykyAika() {
    // laittaa automaattisesti nykyajan aikaan
    nyt.setMinutes(nyt.getMinutes() - nyt.getTimezoneOffset());
    document.getElementById('aika').value = nyt.toISOString().slice(0,16);
    document.getElementById("aika").max = nyt.toISOString().slice(0,16)
}
LaitaNykyAika()

// jos input value on muu niin antaa teksti kentän
document.getElementsByName("laji")[0].addEventListener('change', Tee);

function Tee(){
    let arvo = document.getElementById("KalaLaji").value
    console.log(arvo)
    if (arvo == "muu") {
        document.getElementById("lajiMuu").style.display = "block";
    }
}