import pytest
from jsonschema import validate


schema = {
    "type": "object",
    "properties": {
        "data": {
            "type": "object",
            "properties": {
                "flight_details": {
                    "type": "object",
                    "properties": {
                        "arrival_time": {"type": "string"},
                        "departure_time": {"type": "string"},
                        "eta": {"type": "string"},
                        "etd": {"type": "string"},
                        "flight_name": {"type": "string"},
                        "flight_no": {"type": "string"},
                        "per_kg_price": {"type": "string"},
                        "total_price": {"type": "string"}
                    },
                    "required": [
                        "arrival_time",
                        "departure_time",
                        "eta",
                        "etd",
                        "flight_name",
                        "flight_no",
                        "per_kg_price",
                        "total_price"
                    ]
                },

                "milestone": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "code": {
                                "type": "object",
                                "properties": {
                                    "code": {"type": "string"},
                                    "description": {"type": "string"}
                                },
                                "required": ["code", "description"]
                            },

                            "station": {
                                "type": "object",
                                "properties": {
                                    "code": {"type": "string"}
                                },
                                "required": ["code"]
                            },

                            "status_data": {
                                "type": "object",
                                "properties": {
                                    "quantity": {
                                        "type": "object",
                                        "properties": {
                                            "piece": {"type": "integer"},
                                            "weight": {
                                                "type": "object",
                                                "properties": {
                                                    "unit": {
                                                        "type": "object",
                                                        "properties": {
                                                            "code": {"type": "string"}
                                                        },
                                                        "required": ["code"]
                                                    },
                                                    "value": {"type": "integer"}
                                                },
                                                "required": ["unit", "value"]
                                            }
                                        },
                                        "required": ["piece", "weight"]
                                    }
                                },
                                "required": ["quantity"]
                            },

                            "status_date": {
                                "type": "object",
                                "properties": {
                                    "achieved": {"type": "string"}
                                },
                                "required": ["achieved"]
                            },

                            "status_milestone": {
                                "type": "boolean"
                            }
                        },

                        "required": [
                            "code",
                            "station",
                            "status_data",
                            "status_date",
                            "status_milestone"
                        ]
                    }
                },

                "tracking_details": {
                    "type": "object",
                    "properties": {
                        "awb": {"type": "string"},
                        "destination_code": {"type": "string"},
                        "destination_name": {"type": "string"},
                        "origin_code": {"type": "string"},
                        "origin_name": {"type": "string"},
                        "product": {"type": "string"},
                        "status": {"type": "string"},
                        "total_pieces": {"type": "integer"},
                        "volume": {"type": "string"},
                        "weight": {"type": "string"}
                    },

                    "required": [
                        "awb",
                        "destination_code",
                        "destination_name",
                        "origin_code",
                        "origin_name",
                        "product",
                        "status",
                        "total_pieces",
                        "volume",
                        "weight"
                    ]
                }
            },

            "required": [
                "flight_details",
                "milestone",
                "tracking_details"
            ]
        },

        "messages": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "code": {"type": "string"},
                    "message": {"type": "string"},
                    "type": {"type": "string"}
                },

                "required": [
                    "code",
                    "message",
                    "type"
                ]
            }
        }
    },

    "required": ["data", "messages"]
}


response_data = {
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
                    "description": "Booked on Flight EK-0123"
                },

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


def test_schema_validation():
    validate(instance=response_data, schema=schema)