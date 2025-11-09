import json
from memory_profiler import memory_usage

def process_json(json_data):
    # Your code to process the JSON data goes here.
    # For example:
    data = json.loads(json_data)
    # create some objects from the data.
    return data

def test_memory_leak():
    json_data = """
    {
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
    """
    initial_memory = memory_usage()[0]
    process_json(json_data)
    final_memory = memory_usage()[0]

    memory_difference = final_memory - initial_memory
    print(f"Memory difference: {memory_difference} MB")

    # Assert that the memory usage is within an acceptable range.
    assert memory_difference < 10, "Memory usage exceeded acceptable threshold." # Adjust the threshold as needed.

test_memory_leak()