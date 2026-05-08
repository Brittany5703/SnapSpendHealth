
def categorize_expense(provider):
    provider = provider.lower()

    if "cvs" in provider or "walgreens" in provider or "pharmacy" in provider:
        return "Prescriptions"

    elif "hospital" in provider or "clinic" in provider or "doctor" in provider:
        return "Doctor Visits"

    elif "insurance" in provider:
        return "Insurance"

    elif "therapy" in provider:
        return "Therapy"

    elif "urgent care" in provider or "emergency" in provider:
        return "Emergency Care"

    else:
        return "Medical Supplies"
