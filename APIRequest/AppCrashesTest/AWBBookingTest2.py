import requests

# Sample JSON payload (Replace with actual API response)
payload = {
    "data": {
        "orderResponse": {
            "order": {
                "orderItems": {
                    "orderItem": [
                        {
                            "productInfo": {
                                "documentDetails": {
                                    "documentInfo": {
                                          "documentNumber": "51212685",
                                        "documentType": "AWB"
                                    },
                                    "cargoInfo": {
                                        "quantityInfo": [
                                            {
                                                "piece": 1000
                                            }
                                        ]
                                    }
                                }
                            },
                            "reference": {
                                "bookingReferenceNumber": "50578770",
                                "jobReferenceNumber": "49855437"
                            }
                        }
                    ]
                },
                "orderNumber": "1740549238745"
            }
        },
        "status": "success"
    },
    "messages": [
        {
            "code": "DT_Info_00003",
            "message": "Success",
            "type": "Success"
        }
    ]
}

# Extracting required values
try:
    order_item = payload["data"]["orderResponse"]["order"]["orderItems"]["orderItem"][0]
    document_info = order_item["productInfo"]["documentDetails"]["documentInfo"]
    quantity_info = order_item["productInfo"]["documentDetails"]["cargoInfo"]["quantityInfo"][0]
    references = order_item["reference"]
    order_number = payload["data"]["orderResponse"]["order"]["orderNumber"]
    message = payload["messages"][0]["message"]

    # Validating and printing required fields
    print("documentNumber:", document_info.get("documentNumber", "Not Found"))
    print("documentType:", document_info.get("documentType", "Not Found"))
    print("Piece:", quantity_info.get("piece", "Not Found"))
    print("bookingReferenceNumber:", references.get("bookingReferenceNumber", "Not Found"))
    print("jobReferenceNumber:", references.get("jobReferenceNumber", "Not Found"))
    print("orderNumber:", order_number)
    print("message:", message)

except KeyError as e:
    print(f"Missing key in payload: {e}")