import Container from "./Container"

export default function Navbar(){

return(

<nav

style={{

height:
80,

position:
"fixed",

top:0,

left:0,

right:0,

backdropFilter:
"blur(20px)",

}}

>

<Container>

<div

style={{

height:
80,

display:
"flex",

justifyContent:
"space-between",

alignItems:
"center",

}}

>

<h2>

SCANIX

</h2>

<div>

Dashboard

</div>

</div>

</Container>

</nav>

)

}