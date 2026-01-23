scores = [78, 85, 92, 60, 74, 88]

total_score = sum(scores)
average_score = total_score / len(scores)

above_average = 0
for score in scores:
    if score > average_score:
        above_average += 1

print("Total Score:", total_score)
print("Average Score:", average_score)
print("Scores Above Average:", above_average)