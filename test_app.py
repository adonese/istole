from app import get_location, get_address


def test_get_location():
    address = get_location("15.5622056666667", "32.5655843333333")
    assert address.raw["address"]["city"] == "الخرطوم"
    assert address.raw["address"]["neighbourhood"] == "الطائف"


def test_get_address():
    address = get_address("15.5622056666667", "32.5655843333333")
    assert address == "الطائف, الخرطوم, ولاية الخرطوم, 11114, السودان \u200eal-Sūdān"
