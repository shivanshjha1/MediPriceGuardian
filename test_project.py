
import unittest

from data_manager import DataManager
from price_engine import PriceEngine
from models import Consumable, Procedure, Hospital


class TestMediPriceGuardian(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.manager = DataManager()
        cls.data = cls.manager.load_data()
        cls.engine = PriceEngine()

    def test_database_counts(self):
        self.assertEqual(len(self.data["consumables"]), 6)
        self.assertEqual(len(self.data["procedures"]), 3)
        self.assertEqual(len(self.data["hospitals"]), 8)
        self.assertEqual(len(self.data["schemes"]), 25)

    def test_price_threshold(self):
        item = Consumable("Catheter", 350)

        procedure = Procedure(
            "TEST-001",
            "Test Procedure",
            1000,
            [item]
        )

        # Test exactly at and around the 150% threshold
        for price, expected_alerts in [
            (500, 0),
            (525, 0),
            (526, 1)
        ]:
            hospital = Hospital(
                "Test Hospital",
                {"Catheter": price},
                []
            )

            alerts = self.engine.check_price_gouging(
                hospital, procedure
            )

            self.assertEqual(
                len(alerts),
                expected_alerts
            )

    def test_colonoscopy_estimate(self):
        hospital = self.data["hospitals"][0]
        procedure = self.data["procedures"][0]

        estimate = self.engine.calculate_estimate(
            hospital, procedure
        )

        self.assertEqual(estimate["total_cost"], 14730)
        self.assertEqual(estimate["surgeon_fee"], 12000)
        self.assertEqual(len(estimate["items"]), 3)
        self.assertEqual(estimate["missing_items"], [])

    def test_colonoscopy_gouging_alerts(self):
        hospital = self.data["hospitals"][0]
        procedure = self.data["procedures"][0]

        alerts = self.engine.check_price_gouging(
            hospital, procedure
        )

        self.assertEqual(len(alerts), 3)

    def test_hospital_names_exist(self):
        for hospital in self.data["hospitals"]:
            self.assertTrue(hospital.name)

    def test_procedure_names_exist(self):
        for procedure in self.data["procedures"]:
            self.assertTrue(procedure.name)


if __name__ == "__main__":
    unittest.main(verbosity=2)