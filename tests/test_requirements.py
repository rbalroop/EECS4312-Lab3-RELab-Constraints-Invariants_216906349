# Contains requirement-driven tests for the dispensing subsystem.
# TODO: create at least 3 test cases
import unittest
from src.dispense import DispenseEvent, medication_events, medication_events_counter, patient_ids
import datetime
class TestDispenseEventRequirements(unittest.TestCase):
    def setUp(self):
        # Reset global state before each test
        global medication_events
        global medication_events_counter
        global patient_ids
        medication_events = {}
        medication_events_counter = 0
        patient_ids = {'patient_1': [], 'patient_2': []}

    def test_valid_dispense_event(self):
        """Test that a valid dispense event is created successfully."""
        event = DispenseEvent('patient_1', 'Aspirin', 500, 2)
        self.assertEqual(event.patient_id, 'patient_1')
        self.assertEqual(event.medication, 'Aspirin')
        self.assertEqual(event.dose_mg, 500)
        self.assertEqual(event.quantity, 2)
        self.assertIn(1, medication_events)  # Check if event is recorded

    def test_invalid_dose(self):
        """Test that a dispense event with invalid dose raises ValueError."""
        with self.assertRaises(ValueError):
            DispenseEvent('patient_1', 'Aspirin', -100, 2)

    def test_invalid_quantity(self):
        """Test that a dispense event with invalid quantity raises ValueError."""
        with self.assertRaises(ValueError):
            DispenseEvent('patient_1', 'Aspirin', 500, 0)