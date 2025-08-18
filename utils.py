from tkinter import messagebox
import datetime

def validate_date(date_str):
    try:
        datetime.datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def validate_required_fields(fields):
    for field_name, field_value in fields.items():
        if not field_value.get():
            messagebox.showerror("Error", f"{field_name} is required")
            return False
    return True

def format_prescription(data):
    prescription = []
    prescription.append("=" * 60)
    prescription.append("HOSPITAL PRESCRIPTION")
    prescription.append("=" * 60)
    prescription.append("")
    
    # Patient Information Section
    prescription.append("PATIENT INFORMATION")
    prescription.append("-" * 30)
    prescription.append(f"Patient Name:\t\t{data['PatientName']}")
    prescription.append(f"Patient ID:\t\t{data['PatientId']}")
    prescription.append(f"NHS Number:\t\t{data['nhsNumber']}")
    prescription.append(f"Date of Birth:\t\t{data['DateOfBirth']}")
    prescription.append(f"Address:\t\t{data['PatientAddress']}")
    prescription.append("")
    
    # Medication Information Section
    prescription.append("MEDICATION DETAILS")
    prescription.append("-" * 30)
    prescription.append(f"Medication:\t\t{data['NameofTablets']}")
    prescription.append(f"Reference No:\t\t{data['ref']}")
    prescription.append(f"Dose:\t\t\t{data['Dose']}")
    prescription.append(f"Quantity:\t\t{data['NumberofTablets']} tablets")
    prescription.append(f"Lot Number:\t\t{data['Lot']}")
    prescription.append(f"Daily Dose:\t\t{data['DailyDose']}")
    prescription.append("")
    
    # Dates Section
    prescription.append("IMPORTANT DATES")
    prescription.append("-" * 30)
    prescription.append(f"Issue Date:\t\t{data['IssueDate']}")
    prescription.append(f"Expiry Date:\t\t{data['ExpDate']}")
    prescription.append("")
    
    # Additional Information Section
    prescription.append("ADDITIONAL INFORMATION")
    prescription.append("-" * 30)
    prescription.append(f"Side Effects:\t\t{data['sideEffects']}")
    prescription.append(f"Further Info:\t\t{data['FurtherInformation']}")
    prescription.append(f"Storage Advice:\t\t{data['StorageAdvice']}")
    prescription.append(f"Blood Pressure:\t\t{data['DrivingUsingMachine']}")
    prescription.append("")
    
    prescription.append("=" * 60)
    prescription.append("Generated on: " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    prescription.append("=" * 60)
    
    return "\n".join(prescription)

def clear_fields(fields):
    for field in fields.values():
        field.set("") 