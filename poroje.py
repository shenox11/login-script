import time

# Define the correct password
correct_password = "1234"  # Change to your desired password
max_attempts = 3
cooldown_time = 5  # Cooldown time in seconds

while True:
    attempts = 0

    while attempts < max_attempts:
        password = input("Enter your password: ")

        if password == correct_password:
            print("Access granted.")
            break  # Exit the inner loop if the password is correct
        else:
            attempts += 1
            print(f"Wrong password. You have {max_attempts - attempts} attempt(s) left.")

    if attempts >= max_attempts:
        print(f"Too many failed attempts. Please wait for {cooldown_time} seconds.")
        time.sleep(5)  # Cooldown period