import json

response_json = """PASTE_YOUR_JSON_HERE"""

response_data = json.loads(response_json)


def test_flight_details():
    flight_details = response_data.get("data", {}).get("flight_details", {})

    assert flight_details.get("arrival_time") == "2025-04-09 13:15:00"
    assert flight_details.get("flight_name") == "EK"
    assert flight_details.get("flight_no") == "EK-4010"
    assert flight_details.get("no_of_stops") == 1
    assert flight_details.get("per_kg_price") == ""


def test_milestone():
    milestone = response_data.get("data", {}).get("milestone", [])[0]

    assert milestone.get("code", {}).get("code") == "BKD"
    assert milestone.get("station", {}).get("code") == "FRN"
    assert milestone.get("status_data", {}).get("quantity", {}).get("piece") == 1
    assert milestone.get("status_data", {}).get("quantity", {}).get("weight", {}).get("value") == 10
    assert milestone.get("status_data", {}).get("quantity", {}).get("weight", {}).get("unit", {}).get("code") == "KG"
    assert milestone.get("status_milestone") is True


def test_offer_itinerary():
    itinerary = response_data.get("data", {}).get("offer_itinerary", {}).get("itinerary", [])[0]

    assert itinerary.get("legNumber") == 1
    assert itinerary.get("boardPoint", {}).get("code") == "DWC"
    assert itinerary.get("offPoint", {}).get("code") == "DXB"
    assert itinerary.get("quantity", {}).get("piece") == 1
    assert itinerary.get("quantity", {}).get("weight", {}).get("value") == 10
    assert itinerary.get("transportInfo", {}).get("carrier") == "EK"
    assert itinerary.get("transportInfo", {}).get("number") == "4010"
    assert itinerary.get("transportInfo", {}).get("vehicle", {}).get("mode", {}).get("code") == "T"


def test_tracking_details():
    tracking = response_data.get("data", {}).get("tracking_details", {})

    assert tracking.get("awb") == "176-38528976"
    assert tracking.get("destination_code") == "AMS"
    assert tracking.get("origin_code") == "DWC"
    assert tracking.get("product") == "AXA"
    assert tracking.get("total_pieces") == 1
    assert tracking.get("weight") == "10KG"


def test_messages():
    message = response_data.get("messages", [])[0]

    assert message.get("code") == "DT-INF-1101"
    assert message.get("message") == "Successfully fetched data"
    assert message.get("type") == "INF"