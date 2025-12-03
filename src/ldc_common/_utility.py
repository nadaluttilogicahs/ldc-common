def to_int_safe(value):
    try:
        return int(value)
    except (ValueError, TypeError):
        return None