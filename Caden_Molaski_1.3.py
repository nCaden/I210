num_seconds = int(input("Enter the number of seconds:"))
num_minutes = int(input("Enter the number of minutes:"))
num_hours = int(input("Enter the number of hours:"))
minutes = num_minutes*60
hours = num_hours*3600
total_seconds = num_seconds+minutes+hours
print(f"Total seconds: {total_seconds}")