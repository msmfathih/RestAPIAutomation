import json

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

def assert_and_print(condition, description):
    try:
        assert condition
        print(f"✅ Assertion passed: {description}")
    except AssertionError:
        print(f"❌ Assertion failed: {description}")

# Assertions

assert_and_print(response['messages'][0]['message'] == "Successfully fetched data", "API response message is correct")

fd = response['data']['flight_details']
assert_and_print(fd['flight_no'] == "EK-4010", "Flight number is EK-4010")
assert_and_print(fd['flight_name'] == "EK", "Flight name is EK")
assert_and_print(fd['arrival_time'] == "2025-04-09 13:15:00", "Arrival time matches")
assert_and_print(fd['departure_time'] == "2025-04-07 07:30:00", "Departure time matches")
assert_and_print(fd['no_of_stops'] == 1, "Number of stops is 1")

tracking = response['data']['tracking_details']
assert_and_print(tracking['awb'] == "176-38528976", "AWB number is correct")
assert_and_print(tracking['destination_code'] == "AMS", "Destination code is AMS")
assert_and_print(tracking['origin_code'] == "DWC", "Origin code is DWC")
assert_and_print(tracking['weight'] == "10KG", "Weight is 10KG")
assert_and_print(tracking['total_pieces'] == 1, "Total pieces is 1")

milestones = response['data']['milestone']
assert_and_print(milestones[0]['code']['code'] == "BKD", "First milestone code is BKD")
assert_and_print(milestones[0]['status_data']['quantity']['piece'] == 1, "First milestone piece count is 1")
assert_and_print(milestones[1]['status_data']['quantity']['weight']['value'] == 10, "Second milestone weight is 10 KG")
assert_and_print(milestones[0]['status_milestone'] is True, "First milestone status_milestone is True")
assert_and_print(milestones[1]['status_milestone'] == "", "Second milestone status_milestone is empty")