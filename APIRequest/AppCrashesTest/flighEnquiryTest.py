import json

# Sample response payload
response_payload = {
    "data": [
        {
            "aircraft_classification": "W",
            "aircraft_mode": "J",
            "aircraft_type": "A380",
            "airline_code": "EK",
            "end_date": "23-FEB-2025 13:25:00",
            "flight_date": "23-FEB-2025",
            "flight_destination": "IST",
            "flight_no": "0123",
            "flight_origin": "DXB",
            "flight_status": "ACT",
            "flight_type": "CO",
            "leg": [
                {
                    "aircraft_classification": "W",
                    "aircraft_type": "A380",
                    "departure_gate": "C22",
                    "departure_position": "B12",
                    "etd": "23-FEB-2025 10:15:00",
                    "leg_destination": "IST",
                    "leg_origin": "DXB",
                    "service_type": "J",
                    "sta": "23-FEB-2025 13:25:00",
                    "status": "Estimated",
                    "std": "23-FEB-2025 10:15:00",
                    "tail_number": "A6EDU"
                }
            ],
            "schedule_type": "T1",
            "start_date": "23-FEB-2025 10:15:00",
            "status": "Estimated",
            "stops": "Direct"
        }
    ],
    "messages": [
        {
            "code": "DT_INFO_1034",
            "message": "fetch successfully",
            "type": "Success"
        }
    ],
    "pagination": {
        "current_page": 1,
        "pages": 1,
        "total": 1
    }
}

# Assertion functions
def assert_flight_date(flight_data):
    assert flight_data["flight_date"] == "23-FEB-2025", "Flight date not match"
    print("✅ Flight date validation passed")

def assert_flight_origin(flight_data):
    assert flight_data["flight_origin"] == "DXB", "Flight origin mismatch"
    print("✅ Flight origin validation passed")

def assert_flight_destination(flight_data):
    assert flight_data["flight_destination"] == "IST", "Flight destination mismatch"
    print("✅ Flight destination validation passed")

def assert_status(flight_data):
    assert flight_data["status"] == "Estimated", "Flight status mismatch"
    print("✅ Flight status validation passed")

# Display functions
def display_flight_date(flight_data):
    #print("\nFlight Date:")
    print(flight_data["flight_date"])

def display_flight_origin(flight_data):
    print("\nFlight Origin:")
    print(flight_data["flight_origin"])

def display_flight_destination(flight_data):
    print("\nFlight Destination:")
    print(flight_data["flight_destination"])

def display_status(flight_data):
    print("\nFlight Status:")
    print(flight_data["status"])

# Extract the first flight data entry
flight_data = response_payload["data"][0]

# Run assertions and display output separately
assert_flight_date(flight_data)
display_flight_date(flight_data)

assert_flight_origin(flight_data)
display_flight_origin(flight_data)

assert_flight_destination(flight_data)
display_flight_destination(flight_data)

assert_status(flight_data)
display_status(flight_data)

print("\n✅ All validations passed successfully!")