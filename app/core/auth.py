import bcrypt

from app.exceptions.unauthorized_error import UnauthorizedError

ENCODE_TYPE = "utf-8"


def gen_hashed_password(password: str) -> str:
    return bcrypt.hashpw(password.encode(ENCODE_TYPE), bcrypt.gensalt()).decode(
        ENCODE_TYPE
    )


def validate_password(password: str, hashed_password: str) -> None:
    is_valid = bcrypt.checkpw(
        password.encode(ENCODE_TYPE),
        hashed_password.encode(ENCODE_TYPE),
    )

    if is_valid is False:
        raise UnauthorizedError()
