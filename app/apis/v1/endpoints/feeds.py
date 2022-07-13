from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from starlette import status
from starlette.responses import JSONResponse

from app.schemas.except_msg import ExceptMessage
from app.schemas.feed import FeedFindRes

router = APIRouter()


@router.get(
    "",
    status_code=status.HTTP_200_OK,
    response_model=FeedFindRes,
    responses={
        [status.HTTP_400_BAD_REQUEST]: {"model": ExceptMessage}
    },
)
async def get():
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder()
    )
