"use client"

import { useState } from "react"

import Navbar from "@/shared/components/layout/Navbar"
import Container from "@/shared/components/layout/Container"
import Button from "@/shared/components/ui/Button"

export default function IngredientsPage(){

const [ingredients,setIngredients]=useState("")
const [loading,setLoading]=useState(false)
const [result,setResult]=useState<any>(null)

function extractItems(data:any){

if(!data) return []

if(Array.isArray(data))
return data

if(data.ingredients)
return data.ingredients

if(data.items)
return data.items

if(data.analysis)
return data.analysis

if(data.result)
return extractItems(data.result)

if(data.data)
return extractItems(data.data)

return []

}

function getScore(data:any){

return (
data?.score
||
data?.overall_score
||
data?.result?.score
||
data?.data?.score
||
0
)

}

function getVerdict(data:any){

return (
data?.verdict
||
data?.summary
||
data?.message
||
data?.result?.verdict
||
data?.data?.verdict
||
"Analysis complete"
)

}

async function verify(){

try{

setLoading(true)

const response=

await fetch(
"http://127.0.0.1:8000/api/v1/ingredients",
{
method:"POST",

headers:{
"Content-Type":"application/json",
},

body:JSON.stringify({
ingredients
}),
}
)

const data=
await response.json()

console.log(data)

setResult(data)

}

catch(e){

console.log(e)

alert(
"Ingredient verification failed"
)

}

finally{

setLoading(false)

}

}

const items=
extractItems(result)

return(

<>

<Navbar/>

<main

style={{

minHeight:"100vh",

paddingTop:120,

background:
"radial-gradient(circle at 30% 30%, #0f172a 0%, #020617 80%)",

}}

>

<Container>

<h1

style={{

fontSize:72,

fontWeight:900,

}}

>

🧪 Ingredient Verifier

</h1>


<p

style={{

opacity:.8,

marginBottom:30,

}}

>

Paste ingredients and evaluate them instantly

</p>


<textarea

value={ingredients}

onChange={
e=>
setIngredients(
e.target.value
)
}

style={{

width:"100%",

height:240,

padding:24,

background:"#071327",

borderRadius:28,

color:"white",

fontSize:20,

}}

placeholder=
"Sugar, Palm Oil, Cocoa Powder"

>


</textarea>

<br/>
<br/>

<Button
onClick={verify}
>

{
loading
?
"Analyzing..."
:
"Verify Ingredients"
}

</Button>


{

result

&&

<div

style={{

marginTop:50,

padding:30,

background:"#071327",

borderRadius:30,

}}

>

<h2>

🧠 Ingredient Intelligence

</h2>


<br/>


{

items.map(

(item:any,index:number)=>(

<div

key={index}

style={{

padding:24,

marginBottom:20,

background:"#08192f",

borderRadius:22,

}}

>

<h2>

{

item.name

||

item.ingredient

||

`Ingredient ${index+1}`

}

</h2>


<div

style={{

fontWeight:700,

fontSize:22,

marginTop:10,

color:

(item.level==="safe")

?

"#00ff88"

:

(item.level==="medium")

?

"#ffbf00"

:

"#ff5555"

}}

>

{
item.level
}

</div>


<p

style={{

marginTop:16,

fontSize:18,

}}

>

{
item.reason
}

</p>

</div>

)

)



}


<h1>

Overall Score:

{
getScore(result)
}

/100

</h1>


<p

style={{

marginTop:20,

fontSize:22,

}}

>

{
getVerdict(result)
}

</p>

</div>

}


</Container>

</main>

</>

)

}