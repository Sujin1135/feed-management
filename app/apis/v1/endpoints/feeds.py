from fastapi import APIRouter, Depends, Body
from fastapi.encoders import jsonable_encoder
from starlette import status
from starlette.responses import JSONResponse

from app.schemas.except_msg import ExceptMessage, PydanticExceptMessage
from app.schemas.feed import FeedFindRes, FeedFindReq, FeedRes, FeedCreate, FeedUpdate, FeedDelete
from app.services.feed_service import find_feeds, create_feed, update_feed, soft_remove_feed

router = APIRouter()


@router.get(
    "",
    status_code=status.HTTP_200_OK,
    response_model=FeedFindRes,
)
async def find(queries: FeedFindReq = Depends()):
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(find_feeds(queries))
    )


@router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    response_model=FeedRes,
    responses={
        status.HTTP_422_UNPROCESSABLE_ENTITY: {"model": PydanticExceptMessage}
    },
)
async def create(data: FeedCreate = Body(...)):
    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content=jsonable_encoder(create_feed(data))
    )


@router.patch(
    "/{feed_id}",
    status_code=status.HTTP_200_OK,
    response_model=FeedRes,
    responses={
        status.HTTP_422_UNPROCESSABLE_ENTITY: {"model": PydanticExceptMessage},
        status.HTTP_401_UNAUTHORIZED: {"model": ExceptMessage},
    }
)
async def update(feed_id: int, data: FeedUpdate = Body(...)):
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(update_feed(feed_id, data))
    )


@router.patch(
    "/{feed_id}/remove",
    status_code=status.HTTP_200_OK,
    responses={status.HTTP_401_UNAUTHORIZED: {"model": ExceptMessage}},
)
async def delete(feed_id: int, data: FeedDelete = Body(...)):
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(soft_remove_feed(feed_id, data))
    )
