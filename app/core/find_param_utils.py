def validate_order_by(order_by: str, options: dict) -> bool:
    return order_by is None or order_by in options.keys()


def get_queries(params: dict) -> dict:
    return {
        key: value
        for (key, value) in params.items()
        if key not in ["limit", "offset", "order_by"]
    }
