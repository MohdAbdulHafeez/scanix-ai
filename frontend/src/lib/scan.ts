export async function scanBarcode(
barcode:string,
){

const response=

await fetch(

`http://127.0.0.1:8000/api/v1/barcode/${barcode.trim()}`,

{

method:
"GET",

}

)



if(
!response.ok
){

const text=
await response.text()

console.log(
text
)

throw new Error(
"Scan failed"
)

}



return await response.json()

}