"use client"

import { useState } from "react"

import Navbar from "@/shared/components/layout/Navbar"
import Container from "@/shared/components/layout/Container"
import Button from "@/shared/components/ui/Button"

export default function IngredientsPage(){

const [ingredients,setIngredients]=useState("")
const [image,setImage]=useState<File|null>(null)
const [loading,setLoading]=useState(false)
const [result,setResult]=useState<any>(null)

async function uploadImage(){

if(!image) return

try{

setLoading(true)

const form=
new FormData()

form.append(
"image",
image
)

const res=

await fetch(

"http://127.0.0.1:8000/api/v1/ingredients/image",

{

method:"POST",

body:form,

}

)

const data=
await res.json()

setIngredients(

data.ingredients_text

||

""

)

alert(
"Ingredients extracted"
)

}

catch(e){

console.log(e)

alert(
"OCR failed"
)

}

finally{

setLoading(false)

}

}



async function verify(){

try{

setLoading(true)

const res=

await fetch(

"http://127.0.0.1:8000/api/v1/ingredients",

{

method:"POST",

headers:{

"Content-Type":
"application/json",

},

body:

JSON.stringify({

ingredients,

}),

}

)

const data=

await res.json()

setResult(
data
)

}

catch{

alert(
"Verification failed"
)

}

finally{

setLoading(false)

}

}



return(

<>

<Navbar/>


<main

style={{

minHeight:
"100vh",

paddingTop:
120,

background:
"radial-gradient(circle at 30% 30%, #0f172a 0%, #020617 80%)",

}}

>

<Container>

<h1

style={{

fontSize:
70,

fontWeight:
900,

}}

>

📸 OCR Ingredient Verifier

</h1>


<br/>


<input

type="file"

accept="image/*"

onChange={

e=>

setImage(

e.target.files?.[0]

||

null

)

}

/>


<br/>
<br/>


<Button

onClick={
uploadImage
}

>

{

loading

?

"Extracting..."

:

"Upload & Extract"

}

</Button>


<br/>
<br/>


<textarea

value={
ingredients
}

onChange={

e=>

setIngredients(
e.target.value
)

}

style={{

width:
"100%",

height:
250,

padding:
24,

background:
"#071327",

color:
"white",

borderRadius:
24,

}}

>


</textarea>


<br/>
<br/>


<Button

onClick={
verify
}

>

Verify Ingredients

</Button>



{

result

&&

<div

style={{

marginTop:
40,

padding:
30,

background:
"#071327",

borderRadius:
24,

}}

>

<h2>

🧠 Result

</h2>


<br/>


<div>

Score:

{
result.score
}

</div>


<br/>


<div>

{
result.summary
}

</div>


<br/>


{

result.ingredients

?.map(

(

x:any,

i:number

)=>(

<div

key={i}

style={{

padding:
20,

marginTop:
16,

background:
"#08192f",

borderRadius:
18,

}}

>

<h3>

{
x.name
}

</h3>


<div>

{
x.level
}

</div>


<div>

{
x.reason
}

</div>

</div>

)

)

}


</div>

}


</Container>

</main>

</>

)

}