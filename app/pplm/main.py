from fastapi import APIRouter

router = APIRouter(prefix="/pplm")


@router.get("/product")
async def get_machines():
    return {"product": "here"}
