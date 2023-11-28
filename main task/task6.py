correct_password = "admin@123"
attempts_left = 4

while attempts_left > 0:
    user_password = input("Enter the password: ")

    if user_password == correct_password:
        print("Access granted. Welcome!")
        break
    else:
        attempts_left -= 1
        print(f"Incorrect password. {attempts_left} attempts left.")

if attempts_left == 0:
    print("Account blocked. Too many incorrect attempts.")