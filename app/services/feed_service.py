from app.core.auth import gen_hashed_password, validate_password
from app.core.find_param_utils import validate_order_by, get_queries
from app.crud.crud_feed import crud_feed
from app.models.feed import Feed
from app.schemas.feed import FeedCreate, FeedUpdate, FeedDelete, FeedRes, FeedFindReq

sort_options = {
    "ASC_ID": Feed.id.asc(),
    "DESC_ID": Feed.id.desc(),
    "ASC_TITLE": Feed.title.asc(),
    "DESC_CREATED_AT": Feed.created_at.desc(),
    "ASC_CREATED_AT": Feed.created_at.asc(),
    "DESC_UPDATED_AT": Feed.updated_at.desc(),
    "ASC_UPDATED_AT": Feed.updated_at.asc(),
}


def find_feeds(params: FeedFindReq) -> list:
    options = params.dict()

    if not validate_order_by(options["order_by"], sort_options):
        raise ValueError("올바른 정렬값이 아닙니다.")

    order_by = (
        options["order_by"]
        if options["order_by"] is None
        else sort_options.get(options["order_by"])
    )
    parsed_queries = get_queries(options)
    feeds = crud_feed.find(
        queries=parsed_queries,
        order_by=order_by,
        limit=options["limit"],
        offset=options["offset"],
    )

    return list(map(lambda x: FeedRes(x), feeds))


def get_feed(feed_id: int) -> FeedRes:
    return FeedRes(crud_feed.get(feed_id))


def create_feed(data: FeedCreate) -> FeedRes:
    data.password = gen_hashed_password(data.password)
    return FeedRes(crud_feed.create(data))


def update_feed(feed_id: int, data: FeedUpdate) -> FeedRes:
    validate_password(data.password, crud_feed.get(feed_id).password)
    data.password = None
    return FeedRes(crud_feed.update(feed_id, data))


def soft_remove_feed(feed_id: int, data: FeedDelete) -> None:
    validate_password(data.password, crud_feed.get(feed_id).password)
    crud_feed.soft_remove(feed_id)
