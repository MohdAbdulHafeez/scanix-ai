"use client"

import {
useEffect,
useState,
}
from "react"

import Navbar from "@/shared/components/layout/Navbar"

import Container from "@/shared/components/layout/Container"

import {
getHistory,
}
from "@/stores/scan/history"



export default function HistoryPage(){


const[
items,
setItems,
]
=
useState<any[]>(
[]
)



useEffect(

()=>{

setItems(

getHistory()

)

},

[]

)



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

<h1

style={{

fontSize:
58,

fontWeight:
900,

marginBottom:
30,

}}

>

Scan History

</h1>



{

items.length===0

?

<div

style={{

padding:
40,

borderRadius:
24,

background:
"#071327",

}}

>

No scans yet

</div>

:

<div

style={{

display:
"grid",

gap:
18,

}}

>

{

items.map(

(
x,
i
)=>(

<div

key={
i
}

style={{

display:
"flex",

gap:
20,

padding:
22,

background:
"#071327",

borderRadius:
24,

alignItems:
"center",

}}

>

<img

src={
x.image_url
}

alt={
x.name
}

style={{

width:
100,

height:
100,

background:
"white",

padding:
10,

borderRadius:
18,

objectFit:
"contain",

}}

/>


<div>

<h2>

{
x.name
}

</h2>

<div>

{
x.brand
}

</div>

<br/>

<div>

SCANIX Score:
{
x.score
}

</div>

<div

style={{

opacity:
0.7,

}}

>

{

new Date(
x.time
)

.toLocaleString()

}

</div>

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