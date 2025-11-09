import json

# Sample JSON response (replace with the actual JSON response)
response = {
    "code": "DT-00001",
    "data": {
        "values": [
            {
                "isFavourite": "N",
                "serialNo": "1",
                "serviceDisplayName": "Amend Berth Booking",
                "serviceId": "vRfASrv6jPK-nN4PU_n6DJXvXjxZK3c7_rTxdeySzusTnkSQK40YDKZvpTbb4GEow0pRehQVxlxlc6W03E7fofv3i966PylRRQzVbEPGHmE",
                "serviceName": "Amend Berth Booking"
            },
            {
                "isFavourite": "N",
                "serialNo": "2",
                "serviceDisplayName": "Berth Booking - CBBS",
                "serviceId": "tBFJKRnzFX4LVeBxDfcwG2oRxMWtu2H-HnDEO3Yw9cYPrQrV04OSEGs8k1eI0zPA4GJ6HZL49gmUIvuIBzOgSoXnjzIj4cO1myCAAfoWQGI",
                "serviceName": "Berth Booking - CBBS"
            },
            {
                "isFavourite": "N",
                "serialNo": "3",
                "serviceDisplayName": "Berth Booking - CBBS - Amend",
                "serviceId": "BpubGO0wCq3VIbO1xq_SIygRXgiXk2irD5g0F8Tg51MTnkSQK40YDKZvpTbb4GEow0pRehQVxlxlc6W03E7fofv3i966PylRRQzVbEPGHmE",
                "serviceName": "Berth Booking - CBBS - Amend"
            },
            {
                "isFavourite": "N",
                "serialNo": "4",
                "serviceDisplayName": "Berth Booking - CBBS - Cancel",
                "serviceId": "GYKl57BB4848zN4DKBn97moRxMWtu2H-HnDEO3Yw9cYPrQrV04OSEGs8k1eI0zPA4GJ6HZL49gmUIvuIBzOgSoXnjzIj4cO1myCAAfoWQGI",
                "serviceName": "Berth Booking - CBBS - Cancel"
            },
            {
                "isFavourite": "N",
                "serialNo": "5",
                "serviceDisplayName": "Berth Booking - CBBS - Enquire",
                "serviceId": "zdWiTh_bp1XC4WgI4qApJWoRxMWtu2H-HnDEO3Yw9cYPrQrV04OSEGs8k1eI0zPA4GJ6HZL49gmUIvuIBzOgSoXnjzIj4cO1myCAAfoWQGI",
                "serviceName": "Berth Booking - CBBS - Enquire"
            },
            {
                "isFavourite": "N",
                "serialNo": "6",
                "serviceDisplayName": "Berth Booking Amend (GC)",
                "serviceId": "4POzBlnl_IyzF-7kXoKQ5O07o8kX7oO7CvOziPyUZL0wXTkJ2yG4Kjv5q0iovf301yeze_PP7o02aNO-29c2f6HYYSAy5naLBG1G-3kffgM",
                "serviceName": "Berth Booking Amend (GC)"
            },
            {
                "isFavourite": "N",
                "serialNo": "7",
                "serviceDisplayName": "Berth Booking Amend (GC)_s",
                "serviceId": "7j0IdJ48vpMzP8dKLAVKAGoRxMWtu2H-HnDEO3Yw9cYPrQrV04OSEGs8k1eI0zPA4GJ6HZL49gmUIvuIBzOgSoXnjzIj4cO1myCAAfoWQGI",
                "serviceName": "Berth Booking Amend (GC)_s"
            },
            {
                "isFavourite": "N",
                "serialNo": "8",
                "serviceDisplayName": "Berth Booking Amend CT",
                "serviceId": "23-9Q8naBKNo4ZTb-30DvRY4K6cJecKU-UTfERSm6wXLR_RIzEX8V0I_lviiJDZQO_deaRTipsZ1oddusWjFiUQq_9iLpMDPMW80xTSY2kw",
                "serviceName": "Berth Booking Amend CT"
            },
            {
                "isFavourite": "N",
                "serialNo": "9",
                "serviceDisplayName": "Berth Booking Amend CT_s",
                "serviceId": "wb6RUlOccmcRDHazOqroNzSvc5yABHFUBUHBMW68ALP9wzYpUtul4aPOpC1A-_gsGa21BvawfwRV1O7D9A3X3qjq5bS4EJhdD8DXANB1BEE",
                "serviceName": "Berth Booking Amend CT_s"
            },
            {
                "isFavourite": "N",
                "serialNo": "10",
                "serviceDisplayName": "Berth Booking Amend PROMIS R3",
                "serviceId": "RhfMxfn7PMGiiXnjS0FiTQ-tCtXTg5IQazyTV4jTM8DgYnodkvj2CZQi-4gHM6BKheePMiPhw7WbIIAB-hZAYg",
                "serviceName": "Berth Booking Amend PROMIS R3"
            },
            {
                "isFavourite": "N",
                "serialNo": "11",
                "serviceDisplayName": "Berth Booking Cancel (GC)",
                "serviceId": "c-eJ0PbUlYxOLRmt49xeCDfXZwljdgBLQ6tx97RxDLNi7etAiSEYJIqnofM8GY9nh4jpeN3KUcHVZVHeQ_PJDPQtcE_VZSq5tNLdVPeYllM",
                "serviceName": "Berth Booking Cancel (GC)"
            },
            {
                "isFavourite": "N",
                "serialNo": "12",
                "serviceDisplayName": "Berth Booking Cancel (GC)_s",
                "serviceId": "1Jl_44dZ-CjLrcejDth42zSvc5yABHFUBUHBMW68ALP9wzYpUtul4aPOpC1A-_gsGa21BvawfwRV1O7D9A3X3qjq5bS4EJhdD8DXANB1BEE",
                "serviceName": "Berth Booking Cancel (GC)_s"
            },
            {
                "isFavourite": "N",
                "serialNo": "13",
                "serviceDisplayName": "Berth Booking Cancel CT",
                "serviceId": "xK9JtTgcjJdVEnb32q03sJXvXjxZK3c7_rTxdeySzusTnkSQK40YDKZvpTbb4GEow0pRehQVxlxlc6W03E7fofv3i966PylRRQzVbEPGHmE",
                "serviceName": "Berth Booking Cancel CT"
            },
            {
                "isFavourite": "N",
                "serialNo": "14",
                "serviceDisplayName": "Berth Booking Cancel CT_s",
                "serviceId": "euUlQNqQlGBlovQKved-dxY4K6cJecKU-UTfERSm6wXLR_RIzEX8V0I_lviiJDZQO_deaRTipsZ1oddusWjFiUQq_9iLpMDPMW80xTSY2kw",
                "serviceName": "Berth Booking Cancel CT_s"
            },
            {
                "isFavourite": "N",
                "serialNo": "15",
                "serviceDisplayName": "Berth Booking Cancel PROMIS R3",
                "serviceId": "AF7D-D7q9yUBWwUgtJoCkWoRxMWtu2H-HnDEO3Yw9cYPrQrV04OSEGs8k1eI0zPA4GJ6HZL49gmUIvuIBzOgSoXnjzIj4cO1myCAAfoWQGI",
                "serviceName": "Berth Booking Cancel PROMIS R3"
            },
            {
                "isFavourite": "N",
                "serialNo": "16",
                "serviceDisplayName": "Berth Booking Enquiry (GC)",
                "serviceId": "HJsJHMkQNOPdf1CP6LgC3ORJ55Y4qHH0EL0nQN1qaE04v5CQwD0laqNYNuceAgbRQ2uf24zIi3Sj6BMe5dWOCA",
                "serviceName": "Berth Booking Enquiry (GC)"
            },
            {
                "isFavourite": "N",
                "serialNo": "17",
                "serviceDisplayName": "Berth Booking Enquiry (GC)_s",
                "serviceId": "12l99qvdvAUM7f3EtFCbyWoRxMWtu2H-HnDEO3Yw9cYPrQrV04OSEGs8k1eI0zPA4GJ6HZL49gmUIvuIBzOgSoXnjzIj4cO1myCAAfoWQGI",
                "serviceName": "Berth Booking Enquiry (GC)_s"
            },
            {
                "isFavourite": "N",
                "serialNo": "18",
                "serviceDisplayName": "Berth Booking Enquiry CT",
                "serviceId": "5kdXz60PU12VK8x04Ts8ZygRXgiXk2irD5g0F8Tg51MTnkSQK40YDKZvpTbb4GEow0pRehQVxlxlc6W03E7fofv3i966PylRRQzVbEPGHmE",
                "serviceName": "Berth Booking Enquiry CT"
            },
            {
                "isFavourite": "N",
                "serialNo": "19",
                "serviceDisplayName": "Berth Booking Enquiry CT_s",
                "serviceId": "dN7wj1XhIUT84wK6V6Mh9w-tCtXTg5IQazyTV4jTM8DgYnodkvj2CZQi-4gHM6BKheePMiPhw7WbIIAB-hZAYg",
                "serviceName": "Berth Booking Enquiry CT_s"
            },
            {
                "isFavourite": "N",
                "serialNo": "20",
                "serviceDisplayName": "Berth Booking Enquiry PROMIS R3",
                "serviceId": "8HM96gn05pTl95fEmxl9UmoRxMWtu2H-HnDEO3Yw9cYPrQrV04OSEGs8k1eI0zPA4GJ6HZL49gmUIvuIBzOgSoXnjzIj4cO1myCAAfoWQGI",
                "serviceName": "Berth Booking Enquiry PROMIS R3"
            },
            {
                "isFavourite": "N",
                "serialNo": "21",
                "serviceDisplayName": "Berth Booking Request (GC)",
                "serviceId": "3RiAkyOEMyOc7LVn5cNq8-07o8kX7oO7CvOziPyUZL0wXTkJ2yG4Kjv5q0iovf301yeze_PP7o02aNO-29c2f6HYYSAy5naLBG1G-3kffgM",
                "serviceName": "Berth Booking Request (GC)"
            },
            {
                "isFavourite": "N",
                "serialNo": "22",
                "serviceDisplayName": "Berth Booking Request (GC)_s",
                "serviceId": "laGtKPmtd9UP4Wbnm6kb_JXvXjxZK3c7_rTxdeySzusTnkSQK40YDKZvpTbb4GEow0pRehQVxlxlc6W03E7fofv3i966PylRRQzVbEPGHmE",
                "serviceName": "Berth Booking Request (GC)_s"
            },
            {
                "isFavourite": "N",
                "serialNo": "23",
                "serviceDisplayName": "Berth Booking Request CT",
                "serviceId": "DsS7rzL6IYR62625vp4IwWoRxMWtu2H-HnDEO3Yw9cYPrQrV04OSEGs8k1eI0zPA4GJ6HZL49gmUIvuIBzOgSoXnjzIj4cO1myCAAfoWQGI",
                "serviceName": "Berth Booking Request CT"
            },
            {
                "isFavourite": "N",
                "serialNo": "24",
                "serviceDisplayName": "Berth Booking Request CT_s",
                "serviceId": "4WLD2pTnF7f82dF55o0ybZXvXjxZK3c7_rTxdeySzusTnkSQK40YDKZvpTbb4GEow0pRehQVxlxlc6W03E7fofv3i966PylRRQzVbEPGHmE",
                "serviceName": "Berth Booking Request CT_s"
            },
            {
                "isFavourite": "N",
                "serialNo": "25",
                "serviceDisplayName": "Berth Booking Requst PROMIS R3",
                "serviceId": "GE26RByhshwn6VgZIL3DrGoRxMWtu2H-HnDEO3Yw9cYPrQrV04OSEGs8k1eI0zPA4GJ6HZL49gmUIvuIBzOgSoXnjzIj4cO1myCAAfoWQGI",
                "serviceName": "Berth Booking Requst PROMIS R3"
            },
            {
                "isFavourite": "Y",
                "serialNo": "26",
                "serviceDisplayName": "Cancel Berth Booking",
                "serviceId": "IDhF-P6ZG9cjMooLvIGkpTSvc5yABHFUBUHBMW68ALP9wzYpUtul4aPOpC1A-_gsGa21BvawfwRV1O7D9A3X3qjq5bS4EJhdD8DXANB1BEE",
                "serviceName": "Cancel Berth Booking"
            },
            {
                "isFavourite": "N",
                "serialNo": "27",
                "serviceDisplayName": "Crane Booking - Amend",
                "serviceId": "EiVwZwBV0jioymNFlFh1uEBtW0NReUW3DzcR1zvS7C04v5CQwD0laqNYNuceAgbRQ2uf24zIi3Sj6BMe5dWOCA",
                "serviceName": "Crane Booking - Amend"
            },
            {
                "isFavourite": "N",
                "serialNo": "28",
                "serviceDisplayName": "Crane Booking - Cancellation",
                "serviceId": "Zpl6rso6wK2Rn95Ln3Sb1eHPGVABop0nqJu2MjBhEY44v5CQwD0laqNYNuceAgbRQ2uf24zIi3Sj6BMe5dWOCA",
                "serviceName": "Crane Booking - Cancellation"
            },
            {
                "isFavourite": "N",
                "serialNo": "29",
                "serviceDisplayName": "Crane Booking - Enquiry",
                "serviceId": "b92gJwNCJfRivxSUKuf3yRmttQb2sH8EVdTuw_QN196o6uW0uBCYXQ_A1wDQdQRB",
                "serviceName": "Crane Booking - Enquiry"
            },
            {
                "isFavourite": "N",
                "serialNo": "30",
                "serviceDisplayName": "Crane Booking - Request",
                "serviceId": "MY49GamOreRFcHrtVHDlDOHPGVABop0nqJu2MjBhEY44v5CQwD0laqNYNuceAgbRQ2uf24zIi3Sj6BMe5dWOCA",
                "serviceName": "Crane Booking - Request"
            },
            {
                "isFavourite": "N",
                "serialNo": "31",
                "serviceDisplayName": "Create Berth Booking",
                "serviceId": "r_F06axmP01pSbLO8qFV_WoRxMWtu2H-HnDEO3Yw9cYPrQrV04OSEGs8k1eI0zPA4GJ6HZL49gmUIvuIBzOgSoXnjzIj4cO1myCAAfoWQGI",
                "serviceName": "Create Berth Booking"
            },
            {
                "isFavourite": "N",
                "serialNo": "32",
                "serviceDisplayName": "Enquire Berth Booking",
                "serviceId": "gowSJLY7defUyEuo7VoAdmoRxMWtu2H-HnDEO3Yw9cYPrQrV04OSEGs8k1eI0zPA4GJ6HZL49gmUIvuIBzOgSoXnjzIj4cO1myCAAfoWQGI",
                "serviceName": "Enquire Berth Booking"
            },
            {
                "isFavourite": "N",
                "serialNo": "33",
                "serviceDisplayName": "View Berth Status",
                "serviceId": "5aJTI_5j237QorLJQXB89RY4K6cJecKU-UTfERSm6wXLR_RIzEX8V0I_lviiJDZQO_deaRTipsZ1oddusWjFiUQq_9iLpMDPMW80xTSY2kw",
                "serviceName": "View Berth Status"
            },
            {
                "isFavourite": "N",
                "serialNo": "34",
                "serviceDisplayName": "View Berth Status_s",
                "serviceId": "VnyBIReTXODigus0o5JZKmoRxMWtu2H-HnDEO3Yw9cYPrQrV04OSEGs8k1eI0zPA4GJ6HZL49gmUIvuIBzOgSoXnjzIj4cO1myCAAfoWQGI",
                "serviceName": "View Berth Status_s"
            },
            {
                "isFavourite": "N",
                "serialNo": "35",
                "serviceDisplayName": "Voyage Enquiry",
                "serviceId": "mPhWVnYlCUy47D1fQVA4Tmsr-YBlNeNOr028npA5lv9qRvg0Jv3b6ZfI6ZYBW4Te7CI_cgeLeypR7br_bwjdjQ",
                "serviceName": "Voyage Enquiry"
            },
            {
                "isFavourite": "N",
                "serialNo": "36",
                "serviceDisplayName": "Voyage Enquiry_s",
                "serviceId": "dtPYEd9P9moBDAXO7T5oeigRXgiXk2irD5g0F8Tg51MTnkSQK40YDKZvpTbb4GEow0pRehQVxlxlc6W03E7fofv3i966PylRRQzVbEPGHmE",
                "serviceName": "Voyage Enquiry_s"
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
