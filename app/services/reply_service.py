from app.core.find_param_utils import get_queries
from app.crud.crud_reply import crud_reply
from app.models.reply import Reply
from app.schemas.feed import FeedFindRes
from app.schemas.reply import ReplyCreate, ReplyFindReq, ReplyFindRes, ReplyRes


def find_replies(feed_id: int, params: ReplyFindReq) -> FeedFindRes:
    options = params.dict()
    order_by = Reply.created_at.desc()
    parsed_queries = get_queries({
        "feed_id": feed_id,
        "parent_id": options["parent_id"],
        "depth": 1 if options["parent_id"] else 0,
    })
    replies = crud_reply.find(
        queries=parsed_queries,
        order_by=order_by,
        limit=options["limit"],
        offset=options["offset"],
    )
    result = list(map(lambda x: ReplyRes.create_by_model(x), replies))
    return ReplyFindRes(data=result, count=len(result))


def create_reply(feed_id: int, data: ReplyCreate) -> ReplyRes:
    data.feed_id = feed_id
    data.depth = 1 if data.parent_id else 0
    return ReplyRes.create_by_model(crud_reply.create(data))
