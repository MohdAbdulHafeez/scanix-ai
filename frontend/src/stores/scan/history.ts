type Product={

name:string

brand:string

score:number

image_url:string

time:number

}


export function saveScan(
product:Product,
){

const old =

JSON.parse(

localStorage.getItem(
"scan-history"
)

||

"[]"

)

old.unshift(
product
)

localStorage.setItem(

"scan-history",

JSON.stringify(

old.slice(
0,
20
)

)

)

}



export function getHistory(){

return JSON.parse(

localStorage.getItem(

"scan-history"

)

||

"[]"

)

}