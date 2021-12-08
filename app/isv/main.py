from fastapi import APIRouter

router = APIRouter(prefix="/isv")


@router.get("/machines")
async def get_machines():
    return {"machine": "here"}
