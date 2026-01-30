Requirement Classification: Distinguish between different types of requirements. For each elicitation or derived rule, classiy it as one of the functional, constraint or inavariant requirements in your classification. 

1) <Can a patient receive the same medication if they requested it once immediately before the previous day ended, and once immediately after the new day began? What timezone is "day" based on?,  constraint>

Explanation: Depending on how "day" is defined, this is a rule that must be followed. For example, if "day" means "24 hours since the last request for a certain medication", this is a constraint. 

2) <Does the system validate prescriptions and link them to the dispense event?, functional>

Explanation: If the system allows prescription medications to be requested, it follows that it would require a valid prescription before dispensing. Therefore, it is a functional requirement that the dispensing event and the prescription of the medication be linked.

3) <What uniquely identifies a patient, and must a patient have an ID to request the dispensing of a medication?, invariant>

Explanation: The patient ID format must be the same for all patients during all operations of the program. This makes it an invariant.

4) <Can quantity dispensed exceed inventory, or must it be constrained?, constraint>

Explanation: Depending on whether the withdrawal requests exceed the currently-held stock for a medication, this would be an additional check to run before getting approval for medicine dispensal. Therefore, this is a constraint. 

5) <Are there any rules to prevent early refills?, constraint>

Explanation: If an additional validation step is required to prevent a patient from getting a refill of a medication before their corresponding prescription says they can get one.

6) <Does How precise are recorded timestamps?, constraint>

Explanation: Depending on how precise recorded timestamps are, there may be a constraint that timestamps reach a minimum level of precision.

7) <Does the system check for possible interactions before approving the dispensing request?, functional>

Explanation: This is a functional requirement, since checking for possible medicinational interactions would be an additional check (and feature) the system would need to do.

8) <If dispensing is tied to a prescription, what fields are required?, invariant>

Explanation: If dispensing is tied to a prescription, its representation in the system would need to be consistent across all prescriptions for all patients. This makes it an invariant.
