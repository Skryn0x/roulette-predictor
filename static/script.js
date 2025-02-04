function predictNumber() {
    let num1 = document.getElementById('num1').value;
    let num2 = document.getElementById('num2').value;
    let num3 = document.getElementById('num3').value;

    fetch('/predict', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ num1: num1, num2: num2, num3: num3 })
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            document.getElementById('result').innerText = "Erreur : Données invalides";
        } else {
            document.getElementById('result').innerText = "🎯 Prédiction : " + data.prediction;
        }
    })
    .catch(error => console.log('Erreur:', error));
}
