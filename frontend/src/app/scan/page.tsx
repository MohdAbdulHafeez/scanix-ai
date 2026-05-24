"use client"

import { useState } from "react"

import Navbar from "@/shared/components/layout/Navbar"
import Container from "@/shared/components/layout/Container"
import Button from "@/shared/components/ui/Button"

import { scanBarcode } from "@/lib/scan"
import { explainProduct } from "@/lib/explain"

import {
saveScan,
} from "@/stores/scan/history"



function normalizeIngredient(
value:string,
){

const map:Record<string,string>={

"sucre":"Sugar",
"huile de palme":"Palm Oil",
"noisettes":"Hazelnuts",
"cacao maigre":"Cocoa",
"lait écrémé en poudre":"Skim Milk Powder",
"lactoserum en poudre":"Whey Powder",
"émulsifiants: lécithines soja":"Soy Lecithin",
"vanilline":"Vanillin",

}

const lower =
value.toLowerCase()

for(
const k
of
Object.keys(map)
){

if(
lower.includes(k)
){

return map[k]

}

}

return value

}



export default function ScanPage(){


const[
barcode,
setBarcode
]
=
useState("")


const[
loading,
setLoading
]
=
useState(false)


const[
explaining,
setExplaining
]
=
useState(false)


const[
result,
setResult
]
=
useState<any>(null)


const[
explanation,
setExplanation
]
=
useState("")



async function scan(){

try{

setLoading(true)

setExplanation("")

const data =
await scanBarcode(
barcode
)

setResult(
data
)

const score =

Number(

data
?.tags

?.find(
(
x:string
)=>

x.startsWith(
"scanix:"
)

)

?.replace(
"scanix:",
""
)

)

||
0


saveScan({

name:
data.name,

brand:
data.brand,

image_url:
data.image_url,

score,

time:
Date.now(),

})

}

finally{

setLoading(false)

}

}



async function explain(){

if(
!result
)
return


try{

setExplaining(true)

const res =
await explainProduct(

result.name,

result.ingredients_text,

result.nutrition_score,

result.processing_level,

)

setExplanation(
res.explanation
)

}

finally{

setExplaining(false)

}

}



const score =

Number(

result
?.tags

?.find(
(
x:string
)=>

x.startsWith(
"scanix:"
)

)

?.replace(
"scanix:",
""
)

)

||
0



const verdict =

score>=80

?

"Excellent"

:

score>=60

?

"Good"

:

score>=40

?

"Moderate"

:

"Avoid Frequently"



const verdictColor =

score>=80

?

"#22c55e"

:

score>=60

?

"#84cc16"

:

score>=40

?

"#f59e0b"

:

"#ef4444"



return(

<>

<Navbar/>

<main

style={{

minHeight:
"100vh",

background:
"#020617",

paddingTop:
120,

}}

>

<Container>

<div

style={{

display:
"flex",

flexDirection:
"column",

gap:
28,

}}

>

<h1

style={{

fontSize:
58,

fontWeight:
900,

}}

>

Scan Product

</h1>



<input

value={
barcode
}

onChange={
(
e
)=>

setBarcode(
e.target.value
)

}

placeholder=
"Enter barcode"

style={{

padding:
22,

borderRadius:
18,

fontSize:
18,

background:
"#0f172a",

color:
"white",

border:
"1px solid #334155",

}}

/>



<Button
onClick={
scan
}
>

{

loading

?

"Scanning..."

:

"Scan"

}

</Button>



{

result

&&

<div

style={{

background:
"#071327",

padding:
40,

borderRadius:
36,

display:
"flex",

flexDirection:
"column",

gap:
40,

}}

>

<div

style={{

display:
"flex",

gap:
32,

flexWrap:
"wrap",

alignItems:
"center",

}}

>

<img

src={
result.image_url
}

alt={
result.name
}

style={{

width:
220,

height:
220,

objectFit:
"contain",

background:
"white",

padding:
20,

borderRadius:
28,

}}

/>



<div
style={{
flex:1,
}}
>

<h2
style={{
fontSize:64,
}}
>

{
result.name
}

</h2>


<div
style={{
fontSize:28,
opacity:0.8,
marginBottom:20,
}}
>

{
result.brand
}

</div>



<div

style={{

display:
"inline-block",

padding:
"14px 26px",

borderRadius:
999,

background:
verdictColor,

fontWeight:
900,

}}

>

{
verdict
}

</div>

</div>



<div

style={{

width:
170,

height:
170,

border:
`10px solid ${verdictColor}`,

borderRadius:
999,

display:
"flex",

justifyContent:
"center",

alignItems:
"center",

fontWeight:
900,

fontSize:
46,

}}

>

{
score
}

</div>

</div>



<div

style={{

display:
"grid",

gridTemplateColumns:
"repeat(auto-fit,minmax(220px,1fr))",

gap:
18,

}}

>

{

[
["Grade",result.nutrition_score],
["NOVA",result.processing_level],
["Calories",`${result.nutrition?.energy_kcal} kcal`],
["Sugar",`${result.nutrition?.sugars} g`],
["Fat",`${result.nutrition?.fat} g`],
["Protein",`${result.nutrition?.proteins} g`],

]

.map(

(
x
)=>

<div

key={
String(
x[0]
)
}

style={{

padding:
24,

background:
"#0f172a",

borderRadius:
22,

}}

>

<div>

{
x[0]
}

</div>

<h2>

{
x[1]
}

</h2>

</div>

)

}

</div>



<div>

<h3>

Ingredients Risk

</h3>

<br/>


<div

style={{

display:
"flex",

gap:
12,

flexWrap:
"wrap",

}}

>

{

result.ingredients

?.map(

(
x:any
)=>

<div

key={
x.name
}

style={{

padding:
"12px 18px",

borderRadius:
999,

background:

x.risk==="high"

?

"#7f1d1d"

:

x.risk==="medium"

?

"#78350f"

:

"#052e16",

}}

>

{

normalizeIngredient(
x.name
)

}

</div>

)

}

</div>

</div>



<Button
onClick={
explain
}
>

{

explaining

?

"Thinking..."

:

"Explain With AI"

}

</Button>



{

explanation

&&

<div

style={{

background:
"#0f172a",

padding:
34,

borderRadius:
26,

display:
"flex",

flexDirection:
"column",

gap:
24,

lineHeight:
1.9,

}}

>

<h2>

🧠 SCANIX AI

</h2>



<div>

<h3>

Summary

</h3>

<p>

{

explanation

.split(".")

.slice(0,2)

.join(".")

}

</p>

</div>



<div>

<h3>

⚠ Health Insights

</h3>

<ul>

<li>Ingredient quality reviewed</li>

<li>Nutrition profile evaluated</li>

<li>Processing level considered</li>

</ul>

</div>



<div>

<h3>

🍽 Recommendation

</h3>

<p>

{

score<40

?

"Avoid frequent consumption."

:

score<70

?

"Consume occasionally."

:

"Suitable for regular consumption."

}

</p>

</div>



<div

style={{

height:
1,

background:
"#1e293b",

}}

></div>



<div>

<h3>

Full AI Analysis

</h3>

<p>

{
explanation
}

</p>

</div>

</div>

}

</div>

}

</div>

</Container>

</main>

</>

)

}