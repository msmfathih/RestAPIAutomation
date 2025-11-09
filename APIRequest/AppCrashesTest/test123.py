import unittest
import json

class TestApiResponse(unittest.TestCase):

    def setUp(self):
        self.response_payload_str = """
{
	"data": {
		"continue_with_warnings": true,
		"port": {
			"code": "AEJEA",
			"id": "150500000633778",
			"name": "JEBEL ALI",
			"type": "DPW_PORT"
		},
		"booking_type": "CT",
		"vessel": {
			"code": "",
			"id": "150500000644975",
			"name": "ALBERT MAERSK",
			"type": "01"
		},
		"port_eta": "2025-05-16T12:01:00",
		"port_etd": "2025-05-19T09:01:00",
		"est_port_stay_hours": 69,
		"contact_name": "",
		"contact_number": "",
		"email": "",
		"agent": {
			"code": "MSK",
			"id": "150500000644140",
			"name": "MAERSK LINE"
		},
		"operating_line": {
			"code": "MSK",
			"id": "150500000644140",
			"name": "MAERSK LINE"
		},
		"shipping_service": "150500000001464",
		"arrive_from_port": {
			"id": "150500000630364",
			"name": "COCHIN - INCOK1",
			"item": {
				"code": "INCOK1",
				"id": "150500000630364",
				"name": "COCHIN",
				"type": ""
			}
		},
		"sail_to_port": {
			"id": "150500000632322",
			"name": "LINCOLN - GBLCN",
			"item": {
				"code": "GBLCN",
				"id": "150500000632322",
				"name": "LINCOLN",
				"type": ""
			}
		},
		"inbound_voyage_number": "3453",
		"outbound_voyage_number": "3453",
		"arrival": 3,
		"sail": 3,
		"air": 3,
		"length_overall": 300,
		"charge_tonnage": 93496,
		"visits": [],
		"documents": [],
		"save_as_draft": false,
		"consent_indicator": true,
		"consent_id": "test",
		"consent_by": "dbb32cf5-386c-40fd-ac14-2d4dc6bbf78a",
		"consent_version": "test",
		"consent_date": "2019-08-24T14:15:22Z"
	},
	"auth": {
		"loggedInUser": "msk"
	}
}
"""
        self.response_data = json.loads(self.response_payload_str)
        self.data = self.response_data.get("data", {})
        self.auth = self.response_data.get("auth", {})

    def test_top_level_keys(self):
        self.assertIn("data", self.response_data)
        self.assertIn("auth", self.response_data)

    def test_data_continue_with_warnings(self):
        self.assertTrue(self.data.get("continue_with_warnings"))

    def test_data_port_details(self):
        port = self.data.get("port", {})
        self.assertEqual(port.get("code"), "AEJEA")
        self.assertEqual(port.get("id"), "150500000633778")
        self.assertEqual(port.get("name"), "JEBEL ALI")
        self.assertEqual(port.get("type"), "DPW_PORT")

    def test_data_booking_type(self):
        self.assertEqual(self.data.get("booking_type"), "CT")

    def test_data_vessel_details(self):
        vessel = self.data.get("vessel", {})
        self.assertEqual(vessel.get("code"), "")
        self.assertEqual(vessel.get("id"), "150500000644975")
        self.assertEqual(vessel.get("name"), "ALBERT MAERSK")
        self.assertEqual(vessel.get("type"), "01")

    def test_data_port_eta_etd(self):
        self.assertEqual(self.data.get("port_eta"), "2025-05-16T12:01:00")
        self.assertEqual(self.data.get("port_etd"), "2025-05-19T09:01:00")
        # More robust checks could involve parsing these to datetime objects
        # from datetime import datetime
        # self.assertIsInstance(datetime.fromisoformat(self.data.get("port_eta")), datetime)
        # self.assertIsInstance(datetime.fromisoformat(self.data.get("port_etd")), datetime)


    def test_data_est_port_stay_hours(self):
        self.assertEqual(self.data.get("est_port_stay_hours"), 69)
        self.assertIsInstance(self.data.get("est_port_stay_hours"), int)

    def test_data_contact_details_empty(self):
        self.assertEqual(self.data.get("contact_name"), "")
        self.assertEqual(self.data.get("contact_number"), "")
        self.assertEqual(self.data.get("email"), "")

    def test_data_agent_details(self):
        agent = self.data.get("agent", {})
        self.assertEqual(agent.get("code"), "MSK")
        self.assertEqual(agent.get("id"), "150500000644140")
        self.assertEqual(agent.get("name"), "MAERSK LINE")

    def test_data_operating_line_details(self):
        operating_line = self.data.get("operating_line", {})
        self.assertEqual(operating_line.get("code"), "MSK")
        self.assertEqual(operating_line.get("id"), "150500000644140")
        self.assertEqual(operating_line.get("name"), "MAERSK LINE")

    def test_data_shipping_service(self):
        self.assertEqual(self.data.get("shipping_service"), "150500000001464")

    def test_data_arrive_from_port_details(self):
        arrive_from_port = self.data.get("arrive_from_port", {})
        self.assertEqual(arrive_from_port.get("id"), "150500000630364")
        self.assertEqual(arrive_from_port.get("name"), "COCHIN - INCOK1")
        item = arrive_from_port.get("item", {})
        self.assertEqual(item.get("code"), "INCOK1")
        self.assertEqual(item.get("id"), "150500000630364")
        self.assertEqual(item.get("name"), "COCHIN")
        self.assertEqual(item.get("type"), "")

    def test_data_sail_to_port_details(self):
        sail_to_port = self.data.get("sail_to_port", {})
        self.assertEqual(sail_to_port.get("id"), "150500000632322")
        self.assertEqual(sail_to_port.get("name"), "LINCOLN - GBLCN")
        item = sail_to_port.get("item", {})
        self.assertEqual(item.get("code"), "GBLCN")
        self.assertEqual(item.get("id"), "150500000632322")
        self.assertEqual(item.get("name"), "LINCOLN")
        self.assertEqual(item.get("type"), "")

    def test_data_voyage_numbers(self):
        self.assertEqual(self.data.get("inbound_voyage_number"), "3453")
        self.assertEqual(self.data.get("outbound_voyage_number"), "3453")

    def test_data_movement_types(self):
        self.assertEqual(self.data.get("arrival"), 3)
        self.assertEqual(self.data.get("sail"), 3)
        self.assertEqual(self.data.get("air"), 3)

    def test_data_vessel_measurements(self):
        self.assertEqual(self.data.get("length_overall"), 300)
        self.assertEqual(self.data.get("charge_tonnage"), 93496)

    def test_data_visits_and_documents_empty(self):
        self.assertEqual(self.data.get("visits"), [])
        self.assertIsInstance(self.data.get("visits"), list)
        self.assertEqual(self.data.get("documents"), [])
        self.assertIsInstance(self.data.get("documents"), list)


    def test_data_flags_and_consent(self):
        self.assertFalse(self.data.get("save_as_draft"))
        self.assertTrue(self.data.get("consent_indicator"))
        self.assertEqual(self.data.get("consent_id"), "test")
        self.assertEqual(self.data.get("consent_by"), "dbb32cf5-386c-40fd-ac14-2d4dc6bbf78a")
        self.assertEqual(self.data.get("consent_version"), "test")
        self.assertEqual(self.data.get("consent_date"), "2019-08-24T14:15:22Z")

    def test_auth_details(self):
        self.assertEqual(self.auth.get("loggedInUser"), "msk")

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)