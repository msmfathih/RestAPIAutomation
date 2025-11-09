import json

# The JSON response provided by the user
response_json = """
{
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
                "dimension": [],
                "special_handling": [],
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
                "status_milestone": true
            },
            {
                "code": {
                    "code": "BKD",
                    "description": "Booked on Flight EK-4010V, 07 Apr 2025, DWC-DXB"
                },
                "dimension": [],
                "special_handling": [],
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
        "offer_itinerary": {
            "itinerary": [
                {
                    "addonInfo": [],
                    "arrivalDateTimeLocal": {
                        "estimated": "2025-04-07 09:00:00",
                        "schedule": "2025-04-07 09:00:00"
                    },
                    "arrivalDateTimeUTC": {
                        "estimated": "2025-04-07 05:00:00",
                        "schedule": "2025-04-07 05:00:00"
                    },
                    "boardPoint": {
                        "code": "DWC",
                        "description": "DUBAI"
                    },
                    "departureDateTimeLocal": {
                        "estimated": "2025-04-07 07:30:00",
                        "schedule": "2025-04-07 07:30:00"
                    },
                    "departureDateTimeUTC": {
                        "estimated": "2025-04-07 03:30:00",
                        "schedule": "2025-04-07 03:30:00"
                    },
                    "legNumber": 1,
                    "loadingType": "BLK",
                    "movementStatus": {
                        "code": "BKD"
                    },
                    "oalIndicator": false,
                    "offPoint": {
                        "code": "DXB",
                        "description": "DUBAI"
                    },
                    "partIndicator": false,
                    "quantity": {
                        "dimension": [],
                        "piece": 1,
                        "specialHandling": [],
                        "volume": {
                            "unit": {
                                "code": "CM"
                            },
                            "value": 0.060002
                        },
                        "weight": {
                            "unit": {
                                "code": "K"
                            },
                            "value": 10
                        }
                    },
                    "spaceStatus": {
                        "code": "NN",
                        "description": "Pending Confirmation"
                    },
                    "transportInfo": {
                        "carrier": "EK",
                        "date": "2025-04-07 00:00:00",
                        "destination": "DXB",
                        "extensionNumber": "V",
                        "number": "4010",
                        "origin": "DWC",
                        "vehicle": {
                            "mode": {
                                "code": "T"
                            },
                            "type": {
                                "code": "RFSV"
                            }
                        }
                    }
                },
                {
                    "addonInfo": [],
                    "arrivalDateTimeLocal": {
                        "estimated": "2025-04-09 13:15:00",
                        "schedule": "2025-04-09 13:15:00"
                    },
                    "arrivalDateTimeUTC": {
                        "estimated": "2025-04-09 11:15:00",
                        "schedule": "2025-04-09 11:15:00"
                    },
                    "boardPoint": {
                        "code": "DXB",
                        "description": "DUBAI"
                    },
                    "departureDateTimeLocal": {
                        "estimated": "2025-04-09 08:05:00",
                        "schedule": "2025-04-09 08:05:00"
                    },
                    "departureDateTimeUTC": {
                        "estimated": "2025-04-09 04:05:00",
                        "schedule": "2025-04-09 04:05:00"
                    },
                    "legNumber": 2,
                    "loadingType": "BLK",
                    "movementStatus": {
                        "code": "BKD"
                    },
                    "oalIndicator": false,
                    "offPoint": {
                        "code": "AMS",
                        "description": "AMSTERDAM"
                    },
                    "partIndicator": false,
                    "quantity": {
                        "dimension": [],
                        "piece": 1,
                        "specialHandling": [],
                        "volume": {
                            "unit": {
                                "code": "CM"
                            },
                            "value": 0.060002
                        },
                        "weight": {
                            "unit": {
                                "code": "K"
                            },
                            "value": 10
                        }
                    },
                    "spaceStatus": {
                        "code": "NN",
                        "description": "Pending Confirmation"
                    },
                    "transportInfo": {
                        "carrier": "EK",
                        "date": "2025-04-09 00:00:00",
                        "destination": "AMS",
                        "number": "0147",
                        "origin": "DXB",
                        "vehicle": {
                            "mode": {
                                "code": "J"
                            },
                            "registrationNumber": "A6-EOO",
                            "type": {
                                "code": "388R"
                            }
                        }
                    }
                }
            ],
            "itinerarySegments": [],
            "staffIndicator": false
        },
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
"""

# Parse the JSON string into a Python dictionary
response_data = json.loads(response_json)

# Function to perform and print assertion results
def check_assertion(description, condition):
    """Checks an assertion and prints the result."""
    try:
        assert condition
        print(f"[PASS] {description}")
    except AssertionError:
        print(f"[FAIL] {description}")

# --- Assertions ---
print("--- Running Assertions ---")

# Assertions for flight_details
print("\n--- Flight Details Assertions ---")
flight_details = response_data.get('data', {}).get('flight_details', {})
check_assertion("Flight Details: 'arrival_time' is '2025-04-09 13:15:00'", flight_details.get('arrival_time') == "2025-04-09 13:15:00")
check_assertion("Flight Details: 'flight_name' is 'EK'", flight_details.get('flight_name') == "EK")
check_assertion("Flight Details: 'flight_no' is 'EK-4010'", flight_details.get('flight_no') == "EK-4010")
check_assertion("Flight Details: 'no_of_stops' is 1", flight_details.get('no_of_stops') == 1)
check_assertion("Flight Details: 'per_kg_price' is an empty string", flight_details.get('per_kg_price') == "")

# Assertions for milestone (checking the first milestone as an example)
print("\n--- Milestone Assertions (First Item) ---")
milestones = response_data.get('data', {}).get('milestone', [])
if milestones:
    milestone_1 = milestones[0]
    check_assertion("Milestone 1: 'code.code' is 'BKD'", milestone_1.get('code', {}).get('code') == "BKD")
    check_assertion("Milestone 1: 'station.code' is 'FRN'", milestone_1.get('station', {}).get('code') == "FRN")
    check_assertion("Milestone 1: 'status_data.quantity.piece' is 1", milestone_1.get('status_data', {}).get('quantity', {}).get('piece') == 1)
    check_assertion("Milestone 1: 'status_data.quantity.weight.value' is 10", milestone_1.get('status_data', {}).get('quantity', {}).get('weight', {}).get('value') == 10)
    check_assertion("Milestone 1: 'status_data.quantity.weight.unit.code' is 'KG'", milestone_1.get('status_data', {}).get('quantity', {}).get('weight', {}).get('unit', {}).get('code') == "KG")
    check_assertion("Milestone 1: 'status_milestone' is True", milestone_1.get('status_milestone') is True)
else:
    print("[INFO] No milestones found to assert.")

# Assertions for offer_itinerary (checking the first itinerary leg)
print("\n--- Offer Itinerary Assertions (First Leg) ---")
itinerary = response_data.get('data', {}).get('offer_itinerary', {}).get('itinerary', [])
if itinerary:
    leg_1 = itinerary[0]
    check_assertion("Itinerary Leg 1: 'legNumber' is 1", leg_1.get('legNumber') == 1)
    check_assertion("Itinerary Leg 1: 'boardPoint.code' is 'DWC'", leg_1.get('boardPoint', {}).get('code') == "DWC")
    check_assertion("Itinerary Leg 1: 'offPoint.code' is 'DXB'", leg_1.get('offPoint', {}).get('code') == "DXB")
    check_assertion("Itinerary Leg 1: 'quantity.piece' is 1", leg_1.get('quantity', {}).get('piece') == 1)
    check_assertion("Itinerary Leg 1: 'quantity.weight.value' is 10", leg_1.get('quantity', {}).get('weight', {}).get('value') == 10)
    check_assertion("Itinerary Leg 1: 'transportInfo.carrier' is 'EK'", leg_1.get('transportInfo', {}).get('carrier') == "EK")
    check_assertion("Itinerary Leg 1: 'transportInfo.number' is '4010'", leg_1.get('transportInfo', {}).get('number') == "4010")
    check_assertion("Itinerary Leg 1: 'transportInfo.vehicle.mode.code' is 'T'", leg_1.get('transportInfo', {}).get('vehicle', {}).get('mode', {}).get('code') == "T")
else:
    print("[INFO] No itinerary legs found to assert.")

# Assertions for tracking_details
print("\n--- Tracking Details Assertions ---")
tracking_details = response_data.get('data', {}).get('tracking_details', {})
check_assertion("Tracking Details: 'awb' is '176-38528976'", tracking_details.get('awb') == "176-38528976")
check_assertion("Tracking Details: 'destination_code' is 'AMS'", tracking_details.get('destination_code') == "AMS")
check_assertion("Tracking Details: 'origin_code' is 'DWC'", tracking_details.get('origin_code') == "DWC")
check_assertion("Tracking Details: 'product' is 'AXA'", tracking_details.get('product') == "AXA")
check_assertion("Tracking Details: 'total_pieces' is 1", tracking_details.get('total_pieces') == 1)
check_assertion("Tracking Details: 'weight' is '10KG'", tracking_details.get('weight') == "10KG")

# Assertion for messages
print("\n--- Messages Assertions ---")
messages = response_data.get('messages', [])
if messages:
    message_1 = messages[0]
    check_assertion("Messages 1: 'code' is 'DT-INF-1101'", message_1.get('code') == "DT-INF-1101")
    check_assertion("Messages 1: 'message' is 'Successfully fetched data'", message_1.get('message') == "Successfully fetched data")
    check_assertion("Messages 1: 'type' is 'INF'", message_1.get('type') == "INF")
else:
    print("[INFO] No messages found to assert.")

print("\n--- Assertions Complete ---")