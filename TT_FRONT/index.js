
async function getData(){

    data = await fetch('http://ip172-18-0-16-bmdjd2mdo98g00fti14g-5000.direct.labs.play-with-docker.com/getData')
    .then(response => response.json())
    .then(json => {
        let data = json.content 
        console.log( data.length)
        for (let i = 0; i < data.length; i++){
            console.log(data[i])
            let html = `<tr>
            <td>${data[i][1]}</td>
            <td>${data[i][2]}</td>
            <td>${data[i][3]}</td>
          </tr>`
          console.log(document.querySelector("#table").querySelector("tbody"))
            document.querySelector("#table").querySelector("tbody").innerHTML +=html
       
        }
     
    })
   
}
 getData()