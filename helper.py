def json_handler(data: dict, q, db) -> list:
    required_data = ["short_describtion", "lat", "long", "short_description"]
    if not check_required(required_data, data):
        return [400, {"error": "missing_field"}]
    q.lat = data["lat"]
    q.long = data["long"]
    q.short_describtion = data["short_describtion"] or data["short_description"]
    q.long_describtion = data["long_describtion"] or data["long_description"]
    db.session.add(q)
    db.session.commit()
    return [200, {"response": "ok"}]


def check_required(fields: list, data: dict) -> bool:
    for f in fields:
        a = data.get(f, None)
        if not a:
            return False
    return True
