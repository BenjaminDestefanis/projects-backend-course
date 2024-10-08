
/* document.addEventListener('DOMContentLoaded', () => {
    // Obtencion de datos generales
    fetch('/')
    .then(response => {
        if(!response.ok){
            throw new Error('Fallo la respuesta' + response.statusText)
        } 
        return response.json()
    })
    .then(data => {
        console.log(data)
    })
    .catch(error => {
        console.error('Problema carga de datos inciales', error)
    })


    // Obtencion de datos de localicalizacion
    fetch('/get_location')
    .then(response => {
        if(!response.ok){
            throw new Error('Network response was not of' + response.statusText)
        }
        return response.json()
    })
    .then(data => {
        console.log(data)
    })
    .catch(error => {
        console.error('Problema', error)
    })
}) */

document.getElementById('converter-form').addEventListener('submit', () => {
    event.preventDefault()

    const amount = document.getElementById('amount').value
    const fromCurrency = document.getElementById('from-currency').value.toUpperCase()
    const toCurrency = document.getElementById('to-currency').value.toUpperCase()


    fetch('/convert', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            amount: amount,
            from: fromCurrency,
            to: toCurrency
        })
    })
    .then(response => response.json())
    .then(data => {
        if(data.error) {
            document.getElementById('result').innerText = data.error
        } else {
            document.getElementById('result').innerText = `${data.original_amount} ${data.from_currency} is ${data.converted_amount} ${data.to_currency}`;
        }
    })
    .catch(error => {
        document.getElementById('result').innerText = `An error ocurred. Please try again`
        console.error('Error:', error)
    })
})