export async function explainProduct(
product_name:string,
ingredients_text:string,
nutrition_grade:string,
processing_level:number,
){

const res =
await fetch(

"http://127.0.0.1:8000/api/v1/explain",

{

method:
"POST",

headers:{

"Content-Type":
"application/json",

},

body:

JSON.stringify({

product_name,

ingredients_text,

nutrition_grade,

processing_level,

}),

}

)

if(
!res.ok
){

const error =
await res.json()

throw new Error(

JSON.stringify(
error
)

)

}

return await res.json()

}