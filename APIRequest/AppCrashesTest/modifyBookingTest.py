import json


def assert_order_data(actual_json, expected_data):
    """
    Asserts order data against expected values and prints the comparison.

    Args:
        actual_json (dict): The actual JSON response.
        expected_data (dict): A dictionary containing expected values.
    """

    try:
        order_item = actual_json["data"]["orderdata"]["orderItems"]["orderItem"][0]
        itinerary = order_item["productInfo"]["offerItinerary"]["itinerary"][0]["transportInfo"]
        reference = order_item["reference"]

        actual_results = {
            "date": itinerary.get("date"),
            "destination": itinerary.get("destination"),
            "origin": itinerary.get("origin"),
            "carrier": itinerary.get("carrier"),
            "bookingReferenceNumber": reference.get("bookingReferenceNumber"),
            "jobReferenceNumber": reference.get("jobReferenceNumber"),
            "orderNumber": reference.get("orderNumber"),
        }

        print("\nActual Results:")
        for key, value in actual_results.items():
            print(f"{key}: {value}")

        print("\nExpected Results:")
        for key, value in expected_data.items():
            print(f"{key}: {value}")

        print("\nComparison:")
        for key, expected_value in expected_data.items():
            actual_value = actual_results.get(key)
            if actual_value == expected_value:
                print(f"{key}: PASS - Actual '{actual_value}' matches Expected '{expected_value}'")
            else:
                print(f"{key}: FAIL - Actual '{actual_value}' does not match Expected '{expected_value}'")

    except (KeyError, IndexError, TypeError) as e:
        print(f"Error accessing JSON data: {e}")
        print(f"Actual JSON:\n{json.dumps(actual_json, indent=4)}")


# Example Usage:
actual_json_data = {
    "data": {
        "orderdata": {
            "orderItems": {
                "orderItem": [
                    {
                        "productInfo": {
                            "offerItinerary": {
                                "itinerary": [
                                    {
                                        "transportInfo": {
                                            "date": "2025-03-05 00:00:00",
                                            "destination": "SFO",
                                            "origin": "DXB",
                                            "carrier": "EK"
                                        }
                                    }
                                ]
                            }
                        },
                        "reference": {
                            "bookingReferenceNumber": "50578819",
                            "jobReferenceNumber": "49855486",
                            "orderNumber": "1740645314863"
                        }
                    }
                ]
            },
            "orderNumber": "1740645314863",
            "orderStatus": {
                "code": None,
                "description": None
            },
            "referenceContacts": []
        }
    },
    "status": "success",
    "messages": [
        {
            "code": "DT_Info_00003",
            "message": "Success",
            "type": "Success"
        }
    ]
}

expected_data = {
    "date": "2025-03-05 00:00:00",
    "destination": "SFO",
    "origin": "DXB",
    "carrier": "EK",
    "bookingReferenceNumber": "50578819",
    "jobReferenceNumber": "49855486",
    "orderNumber": "1740645314863",
}

assert_order_data(actual_json_data, expected_data)