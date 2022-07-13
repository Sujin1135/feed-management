from fastapi import APIRouter, Depends, Body
from fastapi.encoders import jsonable_encoder
from starlette import status
from starlette.responses import JSONResponse

from app.schemas.except_msg import PydanticExceptMessage
from app.schemas.reply import ReplyFindRes, ReplyFindReq, ReplyRes, ReplyCreate
from app.services.reply_service import find_replies, create_reply

router = APIRouter()


@router.get(
    "",
    status_code=status.HTTP_200_OK,
    response_model=ReplyFindRes,
)
async def find(feed_id: int, queries: ReplyFindReq = Depends()):
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(find_replies(feed_id, queries))
    )


@router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    response_model=ReplyRes,
    responses={
        status.HTTP_422_UNPROCESSABLE_ENTITY: {"model": PydanticExceptMessage},
    }
)
async def create(feed_id: int, data: ReplyCreate = Body(...)):
    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content=jsonable_encoder(create_reply(feed_id, data))
    )
