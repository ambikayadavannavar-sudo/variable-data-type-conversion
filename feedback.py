feedback = {
    "Excellent": 12,
    "Good": 8,
    "Average": 5,
    "Poor": 2
}
for key, value in feedback.items():
    print(key, ":", value)
total_feedback = sum(feedback.values())
print("Total Feedbacks:", total_feedback)