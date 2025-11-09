import json
# Sample JSON response (replace with the actual JSON response)
response = {
    "code": "DT-00001",
    "data": {
        "values": [
            {
                "isFavourite": "N",
                "serialNo": "1",
                "serviceDisplayName": "Cut And Run Enquiry -p2",
                "serviceId": "cs-LUNGsK3mb6pHXPgaK8moRxMWtu2H-HnDEO3Yw9cadceb551dRV1FCN9w_oyLqfxeaFxDevjIZlfBd0YAe2IXnjzIj4cO1myCAAfoWQGI",
                "serviceName": "Cut And Run Enquiry -p2"
            },
            {
                "isFavourite": "N",
                "serialNo": "2",
                "serviceDisplayName": "Cut And Run Request -p2",
                "serviceId": "GvbvUTiJwMqjv55Qq4WejmoRxMWtu2H-HnDEO3Yw9cadceb551dRV1FCN9w_oyLqfxeaFxDevjIZlfBd0YAe2IXnjzIj4cO1myCAAfoWQGI",
                "serviceName": "Cut And Run Request -p2"
            },
            {
                "isFavourite": "N",
                "serialNo": "3",
                "serviceDisplayName": "Cut and Run (Process-Load)",
                "serviceId": "UX6tFq7VRSpqcnvNSI_ZJRY4K6cJecKU-UTfERSm6wXLR_RIzEX8V0I_lviiJDZQFiDRFpvahdcEm_XJeUAsB0Qq_9iLpMDPMW80xTSY2kw",
                "serviceName": "Cut and Run (Process-Load)"
            },
            {
                "isFavourite": "N",
                "serialNo": "4",
                "serviceDisplayName": "Cut and Run - Amend - p2",
                "serviceId": "NncX8z5c5eYlffrzQYgWHCgRXgiXk2irD5g0F8Tg51MTnkSQK40YDKZvpTbb4GEoWaJU5GbCDOIfRAPevxh0K_v3i966PylRRQzVbEPGHmE",
                "serviceName": "Cut and Run - Amend - p2"
            },
            {
                "isFavourite": "N",
                "serialNo": "5",
                "serviceDisplayName": "Cut and Run - Cancel- p2",
                "serviceId": "vye4xbU5vzMQGHeZdqo92xY4K6cJecKU-UTfERSm6wXLR_RIzEX8V0I_lviiJDZQFiDRFpvahdcEm_XJeUAsB0Qq_9iLpMDPMW80xTSY2kw",
                "serviceName": "Cut and Run - Cancel- p2"
            }
        ]
    },
    "message": "Request Successfully Completed",
    "status": "SUCCESS"
}
# Extract the values list from the JSON response
values = response['data']['values']
# Iterate over each item and print the serial number with serviceDisplayName
for item in values:
    print(f"{item['serialNo']}. {item['serviceDisplayName']}")
