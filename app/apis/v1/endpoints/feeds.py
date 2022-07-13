from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from starlette import status
from starlette.responses import JSONResponse

from app.schemas.except_msg import ExceptMessage
from app.schemas.feed import FeedFindRes, FeedFindReq
from app.services.feed_service import find_feeds

router = APIRouter()


@router.get(
    "",
    status_code=status.HTTP_200_OK,
    response_model=FeedFindRes,
    responses={
        status.HTTP_400_BAD_REQUEST: {"model": ExceptMessage}
    },
)
async def find(queries: FeedFindReq = Depends()):
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(find_feeds(queries))
    )
