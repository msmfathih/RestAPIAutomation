import pytest

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


def test_order_details():

    order_item = payload["data"]["orderResponse"]["order"]["orderItems"]["orderItem"][0]

    document_info = order_item["productInfo"]["documentDetails"]["documentInfo"]

    quantity_info = order_item["productInfo"]["documentDetails"]["cargoInfo"]["quantityInfo"][0]

    references = order_item["reference"]

    order_number = payload["data"]["orderResponse"]["order"]["orderNumber"]

    message = payload["messages"][0]["message"]

    assert document_info.get("documentNumber") == "51212685"
    assert document_info.get("documentType") == "AWB"
    assert quantity_info.get("piece") == 1000
    assert references.get("bookingReferenceNumber") == "50578770"
    assert references.get("jobReferenceNumber") == "49855437"
    assert order_number == "1740549238745"
    assert message == "Success"