"use client"

import { useState } from "react"

import Navbar from "@/shared/components/layout/Navbar"
import Container from "@/shared/components/layout/Container"
import Button from "@/shared/components/ui/Button"



export default function NutritionistPage(){


const[
question,
setQuestion,
]=useState("")


const[
loading,
setLoading,
]=useState(false)


const[
answer,
setAnswer,
]=useState("")


const[
voice,
setVoice,
]=useState("")



function cleanText(
text:string,
){

return text

.replaceAll(
"**",
""
)

.replaceAll(
"###",
""
)

.replaceAll(
"##",
""
)

.replaceAll(
"#",
""
)

}



async function ask(){

if(
!question.trim()
)
return


try{

setLoading(
true
)

setAnswer(
""
)

setVoice(
""
)



const response=

await fetch(

"http://127.0.0.1:8000/api/v1/nutritionist",

{

method:
"POST",

headers:{
"Content-Type":
"application/json",
},

body:

JSON.stringify({

question,

}),

}

)



if(
!response.ok
){

throw Error()

}



const data=

await response.json()



if(
!data.success
){

throw Error()

}



setAnswer(

cleanText(

data.answer

||

""

)

)



if(
data.voice?.path
){

setVoice(

`http://127.0.0.1:8000/${

data.voice.path

.replace(
/^\//,
""
)

}`

)

}


}

catch(

e

){

console.log(
e
)

alert(
"Nutritionist failed"
)

}

finally{

setLoading(
false
)

}

}



return(

<>

<Navbar/>


<main

style={{

minHeight:
"100vh",

background:
"radial-gradient(circle at 30% 30%, #0f172a 0%, #020617 70%)",

paddingTop:
120,

}}

>

<Container>


<h1

style={{

fontSize:
72,

fontWeight:
900,

}}

>

🎤 Nutritionist

</h1>



<p

style={{

opacity:
0.7,

marginBottom:
40,

}}

>

Ask health and nutrition questions

</p>



<textarea

value={
question
}

onChange={
e=>
setQuestion(
e.target.value
)
}

placeholder=
"Can diabetics eat Nutella?"

style={{

width:
"100%",

height:
180,

padding:
24,

borderRadius:
24,

background:
"#071327",

color:
"white",

border:
0,

fontSize:
18,

resize:
"none",

}}

>



</textarea>


<br/>
<br/>


<Button

onClick={
ask
}

disabled={
loading
}

>

{

loading

?

"Thinking..."

:

"Ask AI"

}

</Button>



{

answer

&&

<div

style={{

marginTop:
40,

padding:
32,

background:
"#071327",

borderRadius:
28,

}}

>

<h2>

🤖 SCANIX Nutritionist

</h2>


<div

style={{

marginTop:
20,

lineHeight:
2,

whiteSpace:
"pre-wrap",

fontSize:
18,

}}

>

{
answer
}

</div>



{

voice

&&

<div

style={{

marginTop:
40,

}}

>

<h3>

🔊 Nutrition Voice

</h3>


<audio

key={
voice
}

controls

preload=
"auto"

style={{

width:
"100%",

marginTop:
10,

}}

>

<source

src={
voice
}

type=
"audio/mpeg"

/>

</audio>

</div>

}


</div>

}



</Container>

</main>

</>

)

}