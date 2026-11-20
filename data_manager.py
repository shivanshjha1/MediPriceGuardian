
# ==========================================
# MediPrice Guardian
# File: data_manager.py
# Purpose: Read and write JSON database
# ==========================================

import json
from pathlib import Path

from models import (
    Consumable,
    Procedure,
    Hospital,
    GovernmentScheme
)


class DataManager:

    def __init__(self, file_name="hospital_data.json"):
        self.file_path = Path(file_name)
        self.data_notice = ""

    # --------------------------------------
    # 1. READ JSON DATABASE
    # --------------------------------------

    def _read_json(self):

        if not self.file_path.exists():
            raise FileNotFoundError(
                f"Database file not found: {self.file_path}"
            )

        try:
            with self.file_path.open("r", encoding="utf-8") as file:
                return json.load(file)

        except json.JSONDecodeError as error:
            raise ValueError(
                "Database contains invalid JSON."
            ) from error

    # --------------------------------------
    # 2. LOAD CONSUMABLES
    # --------------------------------------

    def load_consumables(self, records):

        consumables = []

        for record in records:
            item = Consumable(
                record["name"],
                record["market_price"]
            )

            consumables.append(item)

        return consumables

    # --------------------------------------
    # 3. LOAD PROCEDURES
    # --------------------------------------

    def load_procedures(self, records, consumables):

        consumable_map = {
            item.name: item for item in consumables
        }

        procedures = []

        for record in records:

            procedure_items = []

            for item_name in record["consumables"]:

                if item_name not in consumable_map:
                    raise ValueError(
                        f"Unknown consumable: {item_name}"
                    )

                procedure_items.append(
                    consumable_map[item_name]
                )

            procedure = Procedure(
                record["code"],
                record["name"],
                record["surgeon_fee"],
                procedure_items
            )

            procedures.append(procedure)

        return procedures

    # --------------------------------------
    # 4. LOAD HOSPITALS
    # --------------------------------------

    def load_hospitals(self, records):

        hospitals = []

        for record in records:

            hospital = Hospital(
                record["name"],
                record["pricing"],
                record["accepted_schemes"]
            )

            hospitals.append(hospital)

        return hospitals

    # --------------------------------------
    # 5. LOAD GOVERNMENT SCHEMES
    # --------------------------------------

    
    def load_schemes(self, records):
        schemes = []

        for record in records:
            scheme = GovernmentScheme(
                code=record["code"],
                name=record["name"],
                description=record.get("description", ""),
                benefits=record.get("benefits", ""),
                eligibility=record.get("eligibility", ""),
                coverage_amount=record.get("coverage_amount"),
                category=record.get(
                    "category", "Healthcare Programme"
                ),
                official_url=record.get("official_url", "")
            )

            schemes.append(scheme)

        return schemes


    # --------------------------------------
    # 6. LOAD COMPLETE DATABASE
    # --------------------------------------

    def load_data(self):

        raw_data = self._read_json()

        required_keys = [
            "consumables",
            "procedures",
            "hospitals",
            "schemes"
        ]

        for key in required_keys:

            if key not in raw_data:
                raise ValueError(
                    f"Missing database section: {key}"
                )

        self.data_notice = raw_data.get(
            "data_notice", ""
        )

        consumables = self.load_consumables(
            raw_data["consumables"]
        )

        procedures = self.load_procedures(
            raw_data["procedures"],
            consumables
        )

        hospitals = self.load_hospitals(
            raw_data["hospitals"]
        )

        schemes = self.load_schemes(
            raw_data["schemes"]
        )

        return {
            "consumables": consumables,
            "procedures": procedures,
            "hospitals": hospitals,
            "schemes": schemes
        }

    # --------------------------------------
    # 7. SAVE COMPLETE DATABASE
    # --------------------------------------

    def save_data(self, data):

        raw_data = {
            "data_notice": self.data_notice,

            "consumables": [
                {
                    "name": item.name,
                    "market_price": item.market_price
                }
                for item in data["consumables"]
            ],

            "procedures": [
                {
                    "code": item.code,
                    "name": item.name,
                    "surgeon_fee": item.surgeon_fee,
                    "consumables": [
                        consumable.name
                        for consumable in item.consumables
                    ]
                }
                for item in data["procedures"]
            ],

            "hospitals": [
                {
                    "name": item.name,
                    "pricing": item.pricing,
                    "accepted_schemes": item.accepted_schemes
                }
                for item in data["hospitals"]
            ],

            
            "schemes": [
                {
                    "code": item.code,
                    "name": item.name,
                    "coverage_amount": item.coverage_amount,
                    "description": item.description,
                    "benefits": item.benefits,
                    "eligibility": item.eligibility,
                    "category": item.category,
                    "official_url": item.official_url
                }
                for item in data["schemes"]
            ]

        }

        with self.file_path.open("w", encoding="utf-8") as file:

            json.dump(
                raw_data,
                file,
                indent=4,
                ensure_ascii=False
            )

        print("Database saved successfully!")


# ==========================================
# END OF DATA MANAGER
# ==========================================