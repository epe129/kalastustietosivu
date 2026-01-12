// ottaa nyky ajan
let nyt = new Date();

// laittaa automaattisesti nykyajan aikaan
nyt.setMinutes(nyt.getMinutes() - nyt.getTimezoneOffset());
document.getElementById('aika').value = nyt.toISOString().slice(0,16);