import json

# Sample response payload
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

# Assertion functions
def assert_flight_details(flight_details):
    assert flight_details["flight_no"] == "EK-0123", "Flight number not matched"
    assert flight_details["flight_name"] == "EK", "Flight name mismatch"
    assert flight_details["arrival_time"] == "2025-02-22 14:25:00", "Arrival time mismatch"
    assert flight_details["departure_time"] == "2025-02-22 10:15:00", "Departure time mismatch"
    print("✅ Flight details validation passed")

def assert_milestone(milestone):
    assert milestone[0]["code"]["code"] == "BKD", "Milestone code mismatch"
    assert milestone[0]["station"]["code"] == "FRN", "Station code mismatch"
    assert milestone[0]["status_data"]["quantity"]["piece"] == 90, "Piece quantity mismatch"
    assert milestone[0]["status_data"]["quantity"]["weight"]["value"] == 900, "Weight value mismatch"
    assert milestone[0]["status_milestone"] is True, "Milestone status mismatch"
    print("✅ Milestone validation passed")

def assert_tracking_details(tracking_details):
    assert tracking_details["awb"] == "176-51212825", "AWB mismatch"
    assert tracking_details["destination_code"] == "IST", "Destination code mismatch"
    assert tracking_details["origin_code"] == "DXB", "Origin code mismatch"
    assert tracking_details["total_pieces"] == 90, "Total pieces mismatch"
    assert tracking_details["weight"] == "900K", "Weight mismatch"
    print("✅ Tracking details validation passed")

def assert_messages(messages):
    assert messages[0]["code"] == "DT-INF-1101", "Message code mismatch"
    assert messages[0]["message"] == "Successfully fetched data", "Message content mismatch"
    assert messages[0]["type"] == "INF", "Message type mismatch"
    print("✅ Messages validation passed")

# Display functions
def display_flight_details(flight_details):
    print("\nFlight Details:")
    print(json.dumps(flight_details, indent=4))

def display_milestone(milestone):
    print("\nMilestone Details:")
    print(json.dumps(milestone, indent=4))

def display_tracking_details(tracking_details):
    print("\nTracking Details:")
    print(json.dumps(tracking_details, indent=4))

def display_messages(messages):
    print("\nMessages:")
    print(json.dumps(messages, indent=4))

# Run assertions and display output
assert_flight_details(response_payload["data"]["flight_details"])
display_flight_details(response_payload["data"]["flight_details"])

assert_milestone(response_payload["data"]["milestone"])
display_milestone(response_payload["data"]["milestone"])

assert_tracking_details(response_payload["data"]["tracking_details"])
display_tracking_details(response_payload["data"]["tracking_details"])

assert_messages(response_payload["messages"])
display_messages(response_payload["messages"])

print("\n✅ All validations passed successfully!")