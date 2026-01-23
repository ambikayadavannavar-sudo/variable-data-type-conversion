1.def check_intern_eligibility(age, percentage):
    if age >= 18 and percentage >= 60:
        print("Reason: Candidate meets all criteria.")
        return "Eligible"
    else:
        print("Reason: Candidate does not meet the age or percentage requirements.")
        return "Not Eligible