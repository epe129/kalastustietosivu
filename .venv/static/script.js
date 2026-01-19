// ottaa nyky ajan
let nyt = new Date();

// laittaa automaattisesti nykyajan aikaan
nyt.setMinutes(nyt.getMinutes() - nyt.getTimezoneOffset());
document.getElementById('aika').value = nyt.toISOString().slice(0,16);

// jos input value on muu niin antaa teksti kentän
document.getElementsByName("laji")[0].addEventListener('change', doThing);

function doThing(){
    let arvo = document.getElementById("KalaLaji").value
    console.log(arvo)
    if (arvo == "Muu") {
        document.getElementById("lajiMuu").style.display = "block";
    }
}