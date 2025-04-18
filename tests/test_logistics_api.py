from logistics_api import ShipmentManager, Shipment, Status
import unittest

class TestShipmentManager(unittest.TestCase):

    def setUp(self):
        self.testManager=ShipmentManager()

    def test_insertion(self):
        self.assertTrue(self.testManager.create("SHIP001", "New York", 10.5))
        self.assertEqual(len(self.testManager.dict_shipments), 1)
        self.assertTrue(self.testManager.create("SHIP002", "New York", 10.5))
        self.assertEqual(len(self.testManager.dict_shipments), 2)

    def test_duplicate(self):
        self.assertTrue(self.testManager.create("SHIP001", "New York", 10.5))
        self.assertFalse(self.testManager.create("SHIP001", "New York", 10.5))

    def test_empty_string(self):
        self.assertFalse(self.testManager.create("SHIP001", "", 10.5))
        self.assertFalse(self.testManager.create("", "New York", 10.5))
        self.testManager.create("SHIP001", "New York", 10.5)
        self.assertIsNone(self.testManager.get(""))
        self.assertFalse(self.testManager.cancel(""))
        self.assertEqual(len(self.testManager.list_by_destination("")), 0)

    def test_invalid_weight(self):
        self.assertFalse(self.testManager.create("SHIP001", "New York", 0))
        self.assertFalse(self.testManager.create("SHIP001", "New York", -10.5))

    def test_get(self):
        self.assertTrue(self.testManager.create("SHIP001", "New York", 10.5))
        shipment = self.testManager.get("SHIP001")
        if shipment:
            self.assertIsInstance(shipment,Shipment)
            self.assertEqual(shipment.tracking_id, "SHIP001")
            self.assertEqual(shipment.destination, "New York")
            self.assertEqual(shipment.status, Status.PENDING)
            self.assertEqual(shipment.weight, 10.5)

    def test_update_status(self):
        self.assertTrue(self.testManager.create("SHIP001", "New York", 10.5))
        self.assertTrue(self.testManager.update_status("SHIP001",Status.IN_TRANSIT))
        shipment = self.testManager.get("SHIP001")
        if shipment:
            self.assertEqual(shipment.status, Status.IN_TRANSIT)
        self.assertTrue(self.testManager.update_status("SHIP001",Status.DELIVERED))
        shipment = self.testManager.get("SHIP001")
        if shipment:
            self.assertEqual(shipment.status, Status.DELIVERED)

    def test_cancel(self):
        self.assertTrue(self.testManager.create("SHIP001", "New York", 10.5))
        self.assertEqual(len(self.testManager.dict_shipments), 1)
        self.assertTrue(self.testManager.cancel("SHIP001"))
        self.assertEqual(len(self.testManager.dict_shipments), 0)

    def test_deletion_constraints(self):
        self.assertTrue(self.testManager.create("SHIP001", "New York", 10.5))
        self.assertTrue(self.testManager.update_status("SHIP001",Status.IN_TRANSIT))
        self.assertFalse(self.testManager.cancel("SHIP001"))
        self.assertTrue(self.testManager.create("SHIP002", "New York", 10.5))
        self.assertTrue(self.testManager.update_status("SHIP002",Status.DELIVERED))
        self.assertFalse(self.testManager.cancel("SHIP002"))

    def test_list_by_destination(self):
        self.assertTrue(self.testManager.create("SHIP001", "New York", 10.5))
        self.assertTrue(self.testManager.create("SHIP002", "new York", 10.5)) # Test case sensitive
        self.assertEqual(len(self.testManager.list_by_destination("New York")), 2)
        self.assertTrue(self.testManager.create("SHIP003", "Spain", 10.5))
        self.assertEqual(len(self.testManager.list_by_destination("Spain")), 1)  

if __name__ == "__main__": 
    unittest.main()