correct_email = "admin@mail.com"
correct_password = "Admin@123"
max_attempts = 3
attempts_left = max_attempts

while attempts_left > 0:
    user_email = input("Enter your email: ")
    user_password = input("Enter your password: ")

    if user_email == correct_email and user_password == correct_password:
        print("Login is Successful.")
        break
    else:
        attempts_left -= 1
        print(f"Invalid username or password. {attempts_left} attempts left.")

if attempts_left == 0:
    print("You have been blocked. Too many incorrect attempts.")