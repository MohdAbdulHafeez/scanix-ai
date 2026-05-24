"use client"

import {
useRouter
}
from "next/navigation"

import Navbar from "@/shared/components/layout/Navbar"

import Container from "@/shared/components/layout/Container"

import Button from "@/shared/components/ui/Button"


export default function Home() {

const router =
useRouter()

return (

<>

<Navbar />

<main

style={{

minHeight:
"100vh",

display:
"flex",

alignItems:
"center",

background:
"radial-gradient(circle at 30% 30%, #0f172a 0%, #020617 70%)",

}}

>

<Container>

<div

style={{

maxWidth:
800,

}}

>

<h1

style={{

fontSize:
96,

fontWeight:
900,

lineHeight:
1,

marginBottom:
20,

}}

>

SCANIX AI

</h1>

<p

style={{

fontSize:
28,

opacity:
0.85,

marginBottom:
40,

}}

>

Scan food.
Understand ingredients.
Trust what you eat.

</p>

<Button

onClick={()=>

router.push(
"/scan"
)

}

>

Start Scanning

</Button>

</div>

</Container>

</main>

</>

)

}