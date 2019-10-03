

fetch('https://api.exchangeratesapi.io/latest?symbols=USD,BRL')
  .then(response => response.json())
  .then(json => {
    
    document.querySelector("#real").textContent = json.rates.BRL
document.querySelector("#dolar").textContent = json.rates.USD
  })
