import patient_registry as pr

if __name__ == "__main__":

    registry = pr.patient_registry()

    while True:

        print("""
Welcome to the Patient Registry System.
    
Please select an option:
    
    1. Register a new patient
    2. Retrieve a patient record by ID
    3. Update a patient's name by ID (ID cannot be changed)
    4. Delete a patient record by ID
    5. List all patient records
    6. Exit the system
    
    """)

        choice = input("Enter your choice (1-6): ")

        match(choice):

            case '1':
                print("Register a new patient, type the patient's name, or type 'exit' to return to the main menu.")
                name = input("Enter patient's name: ")

                if name.lower() == 'exit':
                    continue

                new_id = registry.register_patient(name)

                print(f"Patient {new_id} registered successfully!")

            case '2':
                print("Retrieve a patient record by ID, type the patient's ID, or type 'exit' to return to the main menu.")
                id = input("Enter patient's ID: ")

                if id.lower() == 'exit':
                    continue

                try:
                    record = registry.get_patient(int(id))
                    print(
f"""
------------------------------------------------
Patient Record ---------------------------------
Patient Name: {record[int(id)]}
Patient ID: {id}
------------------------------------------------
""")
                except KeyError as e:
                    print(e)

                continue

            case '3':
                print("Update a patient's name by ID, type the patient's ID, or type 'exit' to return to the main menu.")
                id = input("Enter patient's ID: ")

                if id.lower() == 'exit':
                    continue

                print("Type the patient's new name, or type 'exit' to return to the main menu.")
                new_name = input("Enter patient's new name: ")

                if new_name.lower() == 'exit':
                    continue

                try:
                    registry.update_patient_name(int(id), new_name)
                    print(f"Patient {id} updated successfully!")
                    print(f"New name: {new_name}")
                except KeyError as e:
                    print(e)

                continue

            case '4':

                print("Delete a patient record by ID, type the patient's ID, or type 'exit' to return to the main menu.")
                id = input("Enter patient's ID: ")

                if id.lower() == 'exit':
                    continue

                try:
                    registry.delete_patient(int(id))
                    print(f"Patient {id} deleted successfully!")
                except KeyError as e:
                    print(e)

                continue

            case '5':

                if len(registry.patients) == 0:
                    print("No patient records found.")
                    continue

                print("List of all patient records:")

                for id, name in registry.patients.items():
                    print(f"Patient ID: {id}, Patient Name: {name}")

                continue

            case '6':
                print("Exiting the system. Goodbye!")
                break
