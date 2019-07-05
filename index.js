// document.querySelector("body").addEventListener("click",()=>
// {
//     document.querySelector("body").setAttribute("bgcolor","blue")
// })

fetch('https://api.exchangeratesapi.io/latest?symbols=USD,BRL')
  .then(response => response.json())
  .then(json => {
    document.querySelector("#real").textContent = json.rates.BRL
document.querySelector("#dolar").textContent = json.rates.USD
  })
// console.log(jsonV)
// document.querySelector("#real").textContent = jsonV.rates.BRL
// document.querySelector("#real").textContent = jsonV.rates.USD