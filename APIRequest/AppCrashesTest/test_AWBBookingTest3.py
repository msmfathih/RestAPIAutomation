import pytest

def validate_document_number(data):
    expected = "51212685"
    actual = data.get("data", {}).get("orderResponse", {}).get("order", {}).get("orderItems", {}).get("orderItem", [])[0].get("productInfo", {}).get("documentDetails", {}).get("documentInfo", {}).get("documentNumber", "Not Found")

    assert actual == expected, f"documentNumber mismatch: Expected {expected}, Got {actual}"


def validate_document_type(data):
    expected = "AWB"
    actual = data.get("data", {}).get("orderResponse", {}).get("order", {}).get("orderItems", {}).get("orderItem", [])[0].get("productInfo", {}).get("documentDetails", {}).get("documentInfo", {}).get("documentType", "Not Found")

    assert actual == expected, f"documentType mismatch: Expected {expected}, Got {actual}"


def validate_piece(data):
    expected = 1000
    actual = data.get("data", {}).get("orderResponse", {}).get("order", {}).get("orderItems", {}).get("orderItem", [])[0].get("productInfo", {}).get("documentDetails", {}).get("cargoInfo", {}).get("quantityInfo", [])[0].get("piece", "Not Found")

    assert actual == expected, f"Piece mismatch: Expected {expected}, Got {actual}"


def validate_booking_reference_number(data):
    expected = "50578770"
    actual = data.get("data", {}).get("orderResponse", {}).get("order", {}).get("orderItems", {}).get("orderItem", [])[0].get("reference", {}).get("bookingReferenceNumber", "Not Found")

    assert actual == expected, f"bookingReferenceNumber mismatch: Expected {expected}, Got {actual}"


def validate_job_reference_number(data):
    expected = "49855437"
    actual = data.get("data", {}).get("orderResponse", {}).get("order", {}).get("orderItems", {}).get("orderItem", [])[0].get("reference", {}).get("jobReferenceNumber", "Not Found")

    assert actual == expected, f"jobReferenceNumber mismatch: Expected {expected}, Got {actual}"


def validate_order_number(data):
    expected = "1740549238745"
    actual = data.get("data", {}).get("orderResponse", {}).get("order", {}).get("orderNumber", "Not Found")

    assert actual == expected, f"orderNumber mismatch: Expected {expected}, Got {actual}"


def validate_message(data):
    expected = "Success"
    actual = data.get("messages", [])[0].get("message", "Not Found")

    assert actual == expected, f"message mismatch: Expected {expected}, Got {actual}"


payload = {
    "data": {
        "orderResponse": {
            "order": {
                "orderItems": {
                    "orderItem": [{
                        "productInfo": {
                            "documentDetails": {
                                "documentInfo": {
                                    "documentNumber": "51212685",
                                    "documentType": "AWB"
                                },
                                "cargoInfo": {
                                    "quantityInfo": [{
                                        "piece": 1000
                                    }]
                                }
                            }
                        },
                        "reference": {
                            "bookingReferenceNumber": "50578770",
                            "jobReferenceNumber": "49855437"
                        }
                    }]
                },
                "orderNumber": "1740549238745"
            }
        },
        "status": "success"
    },
    "messages": [{
        "message": "Success"
    }]
}


def test_order_validations():
    validate_document_number(payload)
    validate_document_type(payload)
    validate_piece(payload)
    validate_booking_reference_number(payload)
    validate_job_reference_number(payload)
    validate_order_number(payload)
    validate_message(payload)