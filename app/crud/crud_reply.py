from app.crud.crud_base import CRUDBase
from app.models.reply import Reply
from app.schemas.reply import ReplyCreate, ReplyUpdate


class CRUDReply(CRUDBase[Reply, ReplyCreate, ReplyUpdate]):
    """ Reply repository """


crud_reply = CRUDReply(Reply)
