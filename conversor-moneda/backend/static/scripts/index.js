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