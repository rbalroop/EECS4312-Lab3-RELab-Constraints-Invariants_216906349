import datetime
# Global dictionary to track patient IDs on record and the medications they are currently taking. 
# Key: Patient_ID, Value: Medication Event IDs. 

patient_ids = {}

# Global dictionary to track medication dispensing events. 
# Key: Medication_Event_ID, Value: DispenseEvent object.
medication_events = {}

medication_events_counter = 0
class DispenseEvent:
    """
    Represents a single medication dispensing event for a patient.

    """

    # TODO Task 3: Encode and enforce input constraints (e.g., valid dose, quantity, identifiers)
    def __init__(self, patient_id, medication, dose_mg, quantity):
        """
        Initialize a new DispenseEvent.

        Args:
            patient_id: Unique identifier for the patient receiving medication.
            medication: Name or identifier of the medication being dispensed.
            dose_mg: Dose per unit in milligrams. Must be a positive number.
            quantity: Number of units dispensed. Must be a positive integer.

        """
        self.patient_id = patient_id
        self.medication = medication
        self.dose_mg = dose_mg
        self.quantity = quantity
        self.timestamp = datetime.datetime.now()
        
        if not self.invariant_holds(medication_events.values(), self):
            raise ValueError("DispenseEvent violates system invariants.")
        else:
            global medication_events_counter
            medication_events_counter += 1
            medication_events[medication_events_counter] = self
            patient_ids[patient_id].append(medication_events_counter)
        

    # TODO Task 4: Define and check system invariants 
    def invariant_holds(existing_events, new_event) -> bool:
        """
        Check whether adding a new dispense event preserves all system invariants.

        Args:
            existing_events: Iterable of previously recorded DispenseEvent objects.
            new_event: The proposed DispenseEvent to validate.

        Returns:
            bool: True if all invariants hold after adding new_event; False otherwise.
            
        """
        is_valid = True
        # if the dose is not positive
        if new_event.dose_mg <= 0:
            is_valid = False
        # if the quantity is not positive
        elif new_event.quantity <= 0:
            is_valid = False
        # if the patient ID is not recognized
        elif new_event.patient_id not in patient_ids:
            is_valid = False
        # if the timestamp is in the future
        elif new_event.timestamp > datetime.datetime.now():
            is_valid = False    
        # if the patient has already been dispensed the same medication within the last 24 hours
        elif self.has_been_dispensed_recently(new_event):
            is_valid = False
        elif self.is_medication_dose_unit_mg(new_event.medication) is False:
            is_valid = False
        return is_valid
    
    def is_medication_dose_unit_mg(medication_name) -> bool:
        """
        Check if the medication's dose unit is in milligrams (mg).

        Args:
            medication_name: Name or identifier of the medication to check.
        Returns:
            bool: True if the medication's dose unit is mg; False otherwise.
        """ 
        flag = True
        medication_name.split(" ")
        if "mg" not in medication_name:
            flag = False
        if medication_name[0].isdigit() is False:
            flag = False
        return flag
    
    def has_been_dispensed_recently(new_event) -> bool:
        """
        Check if the patient has been dispensed the same medication within the last 24 hours.

        Args:
            new_event: The proposed DispenseEvent to validate.
        Returns:
            bool: True if the patient has been dispensed the same medication within the last 24 hours; False otherwise. 
        """
        twenty_four_hours_ago = new_event.timestamp - datetime.timedelta(hours=24)
        for event_id in patient_ids[new_event.patient_id]:
            existing_event = medication_events[event_id]
            if (existing_event.medication == new_event.medication and
                existing_event.timestamp >= twenty_four_hours_ago):
                return True
        return False
