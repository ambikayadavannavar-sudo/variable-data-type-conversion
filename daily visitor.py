daily_visitors = [120, 150, 180, 90, 200, 170, 160]
total_visitors = sum(daily_visitors)

average_visitors = total_visitors / len(daily_visitors)

highest_traffic = max(daily_visitors)
lowest_traffic = min(daily_visitors)

print("Total Visitors:", total_visitors)
print("Average Visitors per Day:", average_visitors)
print("Highest Traffic:", highest_traffic)
print("Lowest Traffic:", lowest_traffic)