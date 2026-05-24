type Props = {

children:
React.ReactNode

onClick?:()=>void

}

export default function Button(
{
children,
onClick,
}:Props
){

return(

<button

onClick={
onClick
}

style={{

padding:
"16px 28px",

borderRadius:
18,

border:
"1px solid #27272a",

background:
"white",

color:
"black",

fontWeight:
700,

fontSize:
16,

cursor:
"pointer",

transition:
".2s",

}}

>

{children}

</button>

)

}