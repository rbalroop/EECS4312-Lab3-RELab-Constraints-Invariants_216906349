# Contains requirement-driven tests for the dispensing subsystem.
# TODO: create at least 3 test cases
import unittest
from src.dispense import DispenseEvent, medication_events, medication_events_counter, patient_ids
import datetime
import unittest
import src.dispense as dispense

class TestDispenseEventRequirements(unittest.TestCase):
    def setUp(self):
        dispense.medication_events.clear()
        dispense.patient_ids.clear()
        dispense.patient_ids.update({'patient_1': [], 'patient_2': []})
        dispense.medication_events_counter = 0

    def test_valid_dispense_event(self):
        event = dispense.DispenseEvent('patient_1', 'Aspirin', "500 mg", 2)
        self.assertEqual(event.dose_mg, "500 mg")   # see note below
        self.assertIn(1, dispense.medication_events)


    def test_valid_dispense_event(self):
        """Test that a valid dispense event is created successfully."""
        event = DispenseEvent('patient_1', 'Aspirin', "500 mg", 2)
        self.assertEqual(event.patient_id, 'patient_1')
        self.assertEqual(event.medication, 'Aspirin')
        self.assertEqual(event.dose_mg, '500 mg')
        self.assertEqual(event.quantity, 2)
        self.assertIn(1, medication_events)  # Check if event is recorded

    def test_invalid_dose(self):
        """Test that a dispense event with invalid dose raises ValueError."""
        with self.assertRaises(ValueError):
            DispenseEvent('patient_1', 'Aspirin', "-100 mg", 2)

    def test_invalid_quantity(self):
        """Test that a dispense event with invalid quantity raises ValueError."""
        with self.assertRaises(ValueError):
            DispenseEvent('patient_1', 'Aspirin', "500 mg", 0)