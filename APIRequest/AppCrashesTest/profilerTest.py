import json

data = {
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

def assert_test(condition, message):
    try:
        assert condition, message
        print(f"✅ {message} - PASSED")
    except AssertionError as e:
        print(f"❌ {e} - FAILED")

# Assertions
assert_test(data["data"]["flight_details"]["flight_name"] == "EK", "Flight name should be 'EK'")
assert_test(data["data"]["flight_details"]["flight_no"] == "EK-0123", "Flight number should be 'EK-0123'")
assert_test(data["data"]["tracking_details"]["destination_code"] == "IST", "Destination code should be 'IST'")
assert_test(data["data"]["tracking_details"]["origin_code"] == "DXB", "Origin code should be 'DXB'")
assert_test(data["data"]["tracking_details"]["total_pieces"] == 90, "Total pieces should be 90")
assert_test(data["data"]["milestone"][0]["status_data"]["quantity"]["weight"]["value"] == 900, "Weight value should be 900")
assert_test(data["data"]["milestone"][0]["code"]["code"] == "BKD", "Milestone code should be 'BKD'")
assert_test(data["messages"][0]["message"] == "Successfully fetched data", "Message should be 'Successfully fetched data'")
