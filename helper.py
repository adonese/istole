def json_handler(data: dict, q, db) -> list:
    required_data = ["short_describtion", "long_describtion", "lat", "long"]
    if not check_required(required_data, data):
        return [400, {"error": "missing_field"}]
    q.lat = data["lat"]
    q.long = data["long"]
    q.short_describtion = data["short_describtion"]
    q.long_describtion = data["long_describtion"]
    db.session.add(q)
    db.session.commit()
    return [200, {"response": "ok"}]


def check_required(fields: list, data: dict) -> bool:
    for f in fields:
        a = data.get(f, None)
        if not a:
            return False
    return True
