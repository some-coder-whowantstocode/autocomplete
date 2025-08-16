add.addEventListener("click",()=>{
    const data = word.value
    const xhr = new XMLHttpRequest;
    xhr.open("POST",'/addWord')
    xhr.setRequestHeader("Content-Type","application/json")
    xhr.onload = (data)=>{
        console.log(data)
    }
    xhr.send(JSON.stringify({word:data}))
})

autocomplete.addEventListener("input",function(){
    console.log(this.value)
    const xhr = new XMLHttpRequest;
    xhr.open("POST",'/completeWord')
    xhr.setRequestHeader("Content-Type","application/json")
    xhr.onreadystatechange = function(){
        console.log(this)
    }
    xhr.send(JSON.stringify({word:this.value}))
})