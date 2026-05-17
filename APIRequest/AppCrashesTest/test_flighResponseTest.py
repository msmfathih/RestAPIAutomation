import json
import pytest


response_payload = {
    "data": {
        "flight_details": {
            "arrival_time": "2025-02-22 14:25:00",
            "departure_time": "2025-02-22 10:15:00",
            "eta": "2025-02-22 14:25:00",
            "etd": "2025-02-22 10:15:00",
            "flight_name": "EK",
            "flight_no": "EK-0123",
            "per_kg_price": "",
            "total_price": ""
        },

        "milestone": [
            {
                "code": {
                    "code": "BKD",
                    "description": "Booked on Flight EK-0123, 22 Feb 2025, DXB-IST"
                },

                "dimension": [],
                "special_handling": [],

                "station": {
                    "code": "FRN"
                },

                "status_data": {
                    "quantity": {
                        "piece": 90,
                        "weight": {
                            "unit": {
                                "code": "K"
                            },
                            "value": 900
                        }
                    }
                },

                "status_date": {
                    "achieved": "2025-02-18 19:58:05"
                },

                "status_milestone": True
            }
        ],

        "tracking_details": {
            "awb": "176-51212825",
            "destination_code": "IST",
            "destination_name": "ISTANBUL",
            "origin_code": "DXB",
            "origin_name": "DUBAI",
            "product": "PXD",
            "status": "Your Order is waiting for Confirmation",
            "total_pieces": 90,
            "volume": "5.400216CM",
            "weight": "900K"
        }
    },

    "messages": [
        {
            "code": "DT-INF-1101",
            "message": "Successfully fetched data",
            "type": "INF"
        }
    ]
}


def test_flight_details():

    flight_details = response_payload["data"]["flight_details"]

    print(json.dumps(flight_details, indent=4))

    assert flight_details["flight_no"] == "EK-0123"
    assert flight_details["flight_name"] == "EK"
    assert flight_details["arrival_time"] == "2025-02-22 14:25:00"
    assert flight_details["departure_time"] == "2025-02-22 10:15:00"


def test_milestone():

    milestone = response_payload["data"]["milestone"]

    print(json.dumps(milestone, indent=4))

    assert milestone[0]["code"]["code"] == "BKD"
    assert milestone[0]["station"]["code"] == "FRN"
    assert milestone[0]["status_data"]["quantity"]["piece"] == 90
    assert milestone[0]["status_data"]["quantity"]["weight"]["value"] == 900
    assert milestone[0]["status_milestone"] is True


def test_tracking_details():

    tracking_details = response_payload["data"]["tracking_details"]

    print(json.dumps(tracking_details, indent=4))

    assert tracking_details["awb"] == "176-51212825"
    assert tracking_details["destination_code"] == "IST"
    assert tracking_details["origin_code"] == "DXB"
    assert tracking_details["total_pieces"] == 90
    assert tracking_details["weight"] == "900K"

def test_messages():

    messages = response_payload["messages"]

    print(json.dumps(messages, indent=4))

    assert messages[0]["code"] == "DT-INF-1101"
    assert messages[0]["message"] == "Successfully fetched data"
    assert messages[0]["type"] == "INF"