print("Time Converter")

seconds = int(input("Enter seconds: "))

hours = seconds // 3600
minutes = (seconds % 3600) // 60
remaining = seconds % 60

print("Hours:", hours)
print("Minutes:", minutes)
print("Seconds:", remaining)

if hours > 24:
    print("More than a day")
elif hours == 24:
    print("Exactly one day")
else:
    print("Less than a day")

total_minutes = hours * 60 + minutes
print("Total minutes:", total_minutes)
