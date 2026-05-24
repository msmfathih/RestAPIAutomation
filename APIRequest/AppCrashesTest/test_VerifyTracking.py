import pytest

# Sample response (assume it's loaded from an API or file)
response = {
    "data": {
        "flight_details": {
            "arrival_time": "2025-04-09 13:15:00",
            "departure_time": "2025-04-07 07:30:00",
            "eta": "2025-04-09 13:15:00",
            "etd": "2025-04-09 08:05:00",
            "flight_duration": "01 Hour(s) 30 Minute(s) ",
            "flight_name": "EK",
            "flight_no": "EK-4010",
            "no_of_stops": 1,
            "per_kg_price": "",
            "total_price": ""
        },
        "milestone": [
            {
                "code": {
                    "code": "BKD",
                    "description": "Booked on Flight EK-0147, 09 Apr 2025, DXB-AMS"
                },
                "station": {
                    "code": "FRN"
                },
                "status_data": {
                    "quantity": {
                        "piece": 1,
                        "weight": {
                            "unit": {
                                "code": "KG"
                            },
                            "value": 10
                        }
                    }
                },
                "status_date": {
                    "achieved": "2025-04-07 00:58:06"
                },
                "status_milestone": True
            },
            {
                "code": {
                    "code": "BKD",
                    "description": "Booked on Flight EK-4010V, 07 Apr 2025, DWC-DXB"
                },
                "station": {
                    "code": "FRN"
                },
                "status_data": {
                    "quantity": {
                        "piece": 1,
                        "weight": {
                            "unit": {
                                "code": "KG"
                            },
                            "value": 10
                        }
                    }
                },
                "status_date": {
                    "achieved": "2025-04-07 00:58:06"
                },
                "status_milestone": ""
            }
        ],
        "tracking_details": {
            "awb": "176-38528976",
            "destination_code": "AMS",
            "destination_name": "AMSTERDAM",
            "origin_code": "DWC",
            "origin_name": "DUBAI",
            "product": "AXA",
            "status": "Your Order is waiting for Confirmation",
            "total_pieces": 1,
            "volume": "0.060002CM",
            "weight": "10KG"
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


def test_api_response_message():
    assert response['messages'][0]['message'] == "Successfully fetched data"


def test_flight_details():
    fd = response['data']['flight_details']

    assert fd['flight_no'] == "EK-4010"
    assert fd['flight_name'] == "EK"
    assert fd['arrival_time'] == "2025-04-09 13:15:00"
    assert fd['departure_time'] == "2025-04-07 07:30:00"
    assert fd['no_of_stops'] == 1


def test_tracking_details():
    tracking = response['data']['tracking_details']

    assert tracking['awb'] == "176-38528976"
    assert tracking['destination_code'] == "AMS"
    assert tracking['origin_code'] == "DWC"
    assert tracking['weight'] == "10KG"
    assert tracking['total_pieces'] == 1


def test_milestone_details():
    milestones = response['data']['milestone']

    assert milestones[0]['code']['code'] == "BKD"
    assert milestones[0]['status_data']['quantity']['piece'] == 1
    assert milestones[1]['status_data']['quantity']['weight']['value'] == 10
    assert milestones[0]['status_milestone'] is True
    assert milestones[1]['status_milestone'] == ""