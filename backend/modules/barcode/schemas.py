from pydantic import BaseModel


class BarcodeRequest(BaseModel):

    barcode: str


class BarcodeResponse(BaseModel):

    found: bool

    barcode: str

    product: dict | None