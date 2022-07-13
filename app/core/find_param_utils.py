def validate_order_by(order_by: str, options: dict):
    is_valid = order_by is None or order_by in options.keys()

    if not is_valid:
        raise ValueError("올바른 정렬값이 아닙니다.")


def get_queries(params: dict) -> dict:
    return {
        key: value
        for (key, value) in params.items()
        if key not in ["limit", "offset", "order_by"]
    }
