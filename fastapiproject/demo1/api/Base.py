from fastapi import APIRouter, Request

router = APIRouter()


@router.get("/")
async def home(req: Request):
    return "fastapi"

# @router.get("/items/{item_id}")
# def read_item(item_id: int, q: str | None):
#     return {"item_id": item_id, "q": q}
