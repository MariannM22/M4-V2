from django.test import TestCase
from app import models
# Create your tests here.
class TestEquipment(TestCase):
    def test_can_create_equipment(self):
        equipment = models.create_office_equipment(
            "Printer",
            "OK",
            "Can only print on one side of paper at a time.",
            "jayz@office.com",
            "1-10-2021",
            70,
        )
        self.assertEqual(equipment.id, 1)
        self.assertEqual(equipment.item_type, "Printer")
        self.assertEqual(equipment.condition, "OK")
        self.assertEqual(equipment.notes, "Can only print on one side of paper at a time.")
        self.assertEqual(equipment.estimated_replacement_cost, 70)

    def test_can_view_all_equipment_at_once(self):
        equipment_data = [
            {
                "item_type": "Stapler",
                "condition": "Great",
                "notes": "It staples a lot.",
                "borrowed_by": "bigman@office.com",
                "borrowed_since": "7-03-2021",
                "estimated_replacement_cost": 10,
            },
            {
                "item_type": "Computer",
                "condition": "Good",
                "notes": "It searches stuff.",
                "borrowed_by": "mm@office.com",
                "borrowed_since": "12-25-2020",
                "estimated_replacement_cost": 400,
            },
            {
                "item_type": "Coffee Pot",
                "condition": "Heavily used",
                "notes": "Stained with coffee and handle is hanging off.",
                "borrowed_by": "bossman@office.com",
                "borrowed_since": "10-31-2019",
                "estimated_replacement_cost": 40,
            },
        ]
        for stuff in equipment_data:
            models.create_office_equipment(
                stuff["item_type"],
                stuff["condition"],
                stuff["notes"],
                stuff["borrowed_by"],
                stuff["borrowed_since"],
                stuff["estimated_replacement_cost"],
            )
        equipments = models.all_office_equipment()
        self.assertEqual(len(equipments), len(equipment_data))
        equipment_data = sorted(equipment_data, key=lambda c: c["item_type"])
        equipments = sorted(equipments, key=lambda c: c.item_type)
        for data, equipment in zip(equipment_data, equipments):
            self.assertEqual(data["item_type"], equipment.item_type)
            self.assertEqual(data["condition"], equipment.condition)
            self.assertEqual(data["notes"], equipment.notes)
            self.assertEqual(data["borrowed_by"], equipment.borrowed_by)
            self.assertEqual(data["borrowed_since"], equipment.borrowed_since)
            self.assertEqual(data["estimated_replacement_cost"],equipment.estimated_replacement_cost)

    def test_can_delete_equipment(self):
        equipment_data = [
            {
                "item_type": "Stapler",
                "condition": "Great",
                "notes": "It staples a lot.",
                "borrowed_by": "bigman@office.com",
                "borrowed_since": "7-03-2021",
                "estimated_replacement_cost": 10,
            },
            {
                "item_type": "Computer",
                "condition": "Good",
                "notes": "It searches stuff.",
                "borrowed_by": "mm@office.com",
                "borrowed_since": "12-25-2020",
                "estimated_replacement_cost": 400,
            },
            {
                "item_type": "Coffee Pot",
                "condition": "Heavily used",
                "notes": "Stained with coffee and handle is hanging off.",
                "borrowed_by": "bossman@office.com",
                "borrowed_since": "10-31-2019",
                "estimated_replacement_cost": "40",
            },
        ]
        for equipment_data in equipment_data:
            models.create_office_equipment(
                equipment_data["item_type"],
                equipment_data["condition"],
                equipment_data["notes"],
                equipment_data["borrowed_by"],
                equipment_data["borrowed_since"],
                equipment_data["estimated_replacement_cost"],
            )

        models.delete_equipment(2)
        self.assertEqual(len(models.all_office_equipment()), 2)

    def test_borrowed_by(self):
        equipment_data = [
            {
                "item_type": "Stapler",
                "condition": "Great",
                "notes": "It staples a lot.",
                "borrowed_by": "bigman@office.com",
                "borrowed_since": "7-03-2021",
                "estimated_replacement_cost": 10,
            },
            {
                "item_type": "Computer",
                "condition": "Good",
                "notes": "It searches stuff.",
                "borrowed_by": "mm@office.com",
                "borrowed_since": "12-25-2020",
                "estimated_replacement_cost": 400,
            },
            {
                "item_type": "Coffee Pot",
                "condition": "Heavily used",
                "notes": "Stained with coffee and handle is hanging off.",
                "borrowed_by": "bossman@office.com",
                "borrowed_since": "10-31-2019",
                "estimated_replacement_cost": "40",
            },
        ]
        for equipment_data in equipment_data:
            models.create_office_equipment(
                equipment_data["item_type"],
                equipment_data["condition"],
                equipment_data["notes"],
                equipment_data["borrowed_by"],
                equipment_data["borrowed_since"],
                equipment_data["estimated_replacement_cost"]
            )
        self.assertEqual(len(models.all_available_equipment()), 0)

    def test_can_borrow_equipment(self):
        equipment_data = [
            {
                "item_type": "Stapler",
                "condition": "Great",
                "notes": "It staples a lot.",
                "borrowed_by": "bigman@office.com",
                "borrowed_since": "7-03-2021",
                "estimated_replacement_cost": 10,
            },
            {
                "item_type": "Computer",
                "condition": "Good",
                "notes": "It searches stuff.",
                "borrowed_by": "mm@office.com",
                "borrowed_since": "12-25-2020",
                "estimated_replacement_cost": 400,
            },
            {
                "item_type": "Coffee Pot",
                "condition": "Heavily used",
                "notes": "Stained with coffee and handle is hanging off.",
                "borrowed_by": "bossman@office.com",
                "borrowed_since": "10-31-2019",
                "estimated_replacement_cost": "40",
            },
        ]
        for equipment_data in equipment_data:
            models.create_office_equipment(
                equipment_data["item_type"],
                equipment_data["condition"],
                equipment_data["notes"],
                equipment_data["borrowed_by"],
                equipment_data["borrowed_since"],
                equipment_data["estimated_replacement_cost"]
            )
        models.borrow_office_equipment(3, "britanny@office.com")
        self.assertEqual(
            models.find_by_item_type("Coffee Pot").borrowed_by, "britanny@office.com"
        )

    def test_can_search_by_item_type(self):
        equipment_data = [
            {
                "item_type": "Stapler",
                "condition": "Great",
                "notes": "It staples a lot.",
                "borrowed_by": "bigman@office.com",
                "borrowed_since": "7-03-2021",
                "estimated_replacement_cost": 10,
            },
            {
                "item_type": "Computer",
                "condition": "Good",
                "notes": "It searches stuff.",
                "borrowed_by": "mm@office.com",
                "borrowed_since": "12-25-2020",
                "estimated_replacement_cost": 400,
            },
            {
                "item_type": "Coffee Pot",
                "condition": "Heavily used",
                "notes": "Stained with coffee and handle is hanging off.",
                "borrowed_by": "bossman@office.com",
                "borrowed_since": "10-31-2019",
                "estimated_replacement_cost": "40",
            },
        ]
        for equipment_data in equipment_data:
            models.create_office_equipment(
                equipment_data["item_type"],
                equipment_data["condition"],
                equipment_data["notes"],
                equipment_data["borrowed_by"],
                equipment_data["borrowed_since"],
                equipment_data["estimated_replacement_cost"],
            )
        self.assertIsNone(models.find_equipment_by_id(6))
        equipment = models.find_equipment_by_id(1)
        self.assertIsNotNone(equipment)
        self.assertEqual(equipment.item_type, "Stapler")

    def test_can_return_equipment(self):
        equipment_data = [
            {
                "item_type": "Stapler",
                "condition": "Great",
                "notes": "It staples a lot.",
                "borrowed_by": "bigman@office.com",
                "borrowed_since": "7-03-2021",
                "estimated_replacement_cost": 10,
            },
            {
                "item_type": "Computer",
                "condition": "Good",
                "notes": "It searches stuff.",
                "borrowed_by": "mm@office.com",
                "borrowed_since": "12-25-2020",
                "estimated_replacement_cost": 400,
            },
            {
                "item_type": "Coffee Pot",
                "condition": "Heavily used",
                "notes": "Stained with coffee and handle is hanging off.",
                "borrowed_by": "bossman@office.com",
                "borrowed_since": "10-31-2019",
                "estimated_replacement_cost": 40,
            },
        ]
        for equipment_data in equipment_data:
            models.create_office_equipment(
                equipment_data["item_type"],
                equipment_data["condition"],
                equipment_data["notes"],
                equipment_data["borrowed_by"],
                equipment_data["borrowed_since"],
                equipment_data["estimated_replacement_cost"],
            )
        models.return_office_equipment("2", "")
        self.assertEqual(
            models.find_equipment_by_id("2").borrowed_by, ""
        )


        
        






