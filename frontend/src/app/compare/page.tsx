"use client"

import { useState } from "react"

import Navbar from "@/shared/components/layout/Navbar"
import Container from "@/shared/components/layout/Container"
import Button from "@/shared/components/ui/Button"

import {
scanBarcode,
} from "@/lib/scan"



export default function ComparePage(){


const[left,setLeft]=useState("")
const[right,setRight]=useState("")

const[a,setA]=useState<any>(null)
const[b,setB]=useState<any>(null)

const[loading,setLoading]=useState(false)



function getScore(
product:any,
){

return Number(

product
?.tags
?.find(
(x:string)=>
x.startsWith(
"scanix:"
)
)
?.replace(
"scanix:",
"")

)

||
0

}



function finalScore(
p:any,
){

if(
!p
)
return 0

const scanix=
getScore(
p
)

const sugar=
Number(
p?.nutrition?.sugars
)
||
0

const fat=
Number(
p?.nutrition?.fat
)
||
0

const calories=
Number(
p?.nutrition?.energy_kcal
)
||
0

const protein=
Number(
p?.nutrition?.proteins
)
||
0


return(

scanix

-

sugar*0.4

-

fat*0.3

-

calories*0.02

+

protein*3

)

}



function buildReason(
winner:any,
loser:any,
){

const reasons=[]


if(

winner?.nutrition?.energy_kcal

<

loser?.nutrition?.energy_kcal

){

reasons.push(
"Lower calories"
)

}



if(

winner?.nutrition?.sugars

<

loser?.nutrition?.sugars

){

reasons.push(
"Better sugar profile"
)

}



if(

winner?.nutrition?.proteins

>

loser?.nutrition?.proteins

){

reasons.push(
"Higher protein"
)

}



if(

finalScore(
winner
)

>

finalScore(
loser
)

){

reasons.push(
"Healthier overall score"
)

}



if(
reasons.length===0
){

reasons.push(
"Similar nutrition profile"
)

}

return reasons

}



async function compare(){

try{

setLoading(
true
)

const[

leftData,

rightData,

]

=

await Promise.all([

scanBarcode(
left
),

scanBarcode(
right
),

])


setA(
leftData
)

setB(
rightData
)

}

catch{

alert(
"Compare failed"
)

}

finally{

setLoading(
false
)

}

}



const scoreA=
finalScore(
a
)

const scoreB=
finalScore(
b
)


const finalWinner=

scoreA>=scoreB
?
a
:
b


const finalReasons=

buildReason(

finalWinner,

scoreA>=scoreB
?
b
:
a

)



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

marginBottom:
12,

}}

>

Compare Products

</h1>


<p

style={{

opacity:
0.7,

marginBottom:
40,

}}

>

Compare food quality instantly

</p>



<div

style={{

display:
"grid",

gridTemplateColumns:
"1fr 1fr",

gap:
24,

marginBottom:
24,

}}

>

<input

value={
left
}

onChange={
e=>

setLeft(
e.target.value
)

}

placeholder=
"Barcode A"

style={{

padding:
20,

borderRadius:
20,

background:
"#071327",

border:
0,

color:
"white",

}}

/>



<input

value={
right
}

onChange={
e=>

setRight(
e.target.value
)

}

placeholder=
"Barcode B"

style={{

padding:
20,

borderRadius:
20,

background:
"#071327",

border:
0,

color:
"white",

}}

/>

</div>



<Button
onClick={
compare
}
>

{

loading

?

"Comparing..."

:

"Compare"

}

</Button>



{

a

&&

b

&&

<>

<div

style={{

display:
"grid",

gridTemplateColumns:
"1fr 1fr",

gap:
30,

marginTop:
50,

}}

>

{

[
a,
b,
]

.map(

(
product,
i
)=>{

const rawScore=
getScore(
product
)

const winner=

i===0

?

scoreA>scoreB

:

scoreB>=scoreA


const reasons=

buildReason(

product,

i===0
?
b
:
a

)



return(

<div

key={
i
}

style={{

padding:
32,

borderRadius:
30,

background:
"#071327",

}}

>

<img

src={
product.image_url
}

style={{

width:
220,

height:
220,

background:
"white",

padding:
20,

borderRadius:
20,

objectFit:
"contain",

}}

/>


<h2>

{
product.name
}

</h2>


<div>

{
product.brand
}

</div>


<br/>


<div

style={{

fontSize:
52,

fontWeight:
900,

}}

>

{
rawScore
}

</div>



{

winner

&&

<div

style={{

marginTop:
16,

padding:
14,

background:
"#14532d",

borderRadius:
999,

display:
"inline-block",

}}

>

🏆 Better Choice

</div>

}



<div

style={{

marginTop:
24,

padding:
24,

background:
"#08182d",

borderRadius:
20,

}}

>

<h3>

Why this wins

</h3>


{

reasons.map(

(
x:string
)=>

<div
key={
x
}
>

✓ {
x
}

</div>

)

}

</div>


<br/>


<div>

Calories:
{
product.nutrition?.energy_kcal
}

</div>

<div>

Sugar:
{
product.nutrition?.sugars
}
g

</div>

<div>

Fat:
{
product.nutrition?.fat
}
g

</div>

<div>

Protein:
{
product.nutrition?.proteins
}
g

</div>

</div>

)

}

)

}

</div>



<div

style={{

marginTop:
40,

padding:
34,

background:
"#071327",

borderRadius:
30,

}}

>

<h2>

🏆 Final Verdict

</h2>


<div

style={{

fontSize:
32,

fontWeight:
900,

color:
"#22c55e",

marginTop:
12,

}}

>

Choose:

{
finalWinner?.name
}

</div>



<div

style={{

marginTop:
20,

}}

>

{

finalReasons.map(

(
x:string
)=>

<div
key={
x
}
>

✓ {x}

</div>

)

}

</div>



<div

style={{

marginTop:
24,

opacity:
0.75,

}}

>

Recommendation:

Choose this for a stronger nutrition profile.

</div>

</div>

</>

}

</Container>

</main>

</>

)

}