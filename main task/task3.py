# Get input from the user
phone_number = input("Enter a phone number: ")

# Remove spaces from the input
phone_number = phone_number.replace(" ", "")

# Check and convert the phone number
if phone_number.startswith(("+254", "254")):
    # Already in the correct format
    result = phone_number
elif phone_number.startswith(("07", "71", "01")):
    # Convert to +254 format
    result = "+254" + phone_number[1:]
else:
    # Invalid input
    result = "Invalid phone number format"

# Print the result
print(result)