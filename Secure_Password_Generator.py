# Secure Password Generator
import secrets
import string

print("How many passwords would you like to generate?")

while True:
    try:
        numberOfPasswords = input()
        passwordCount = int(numberOfPasswords)
        for i in range(passwordCount):
            print(
                "".join(
                    secrets.choice(
                        string.punctuation
                        + string.digits
                        + string.ascii_lowercase
                        + string.ascii_uppercase
                        )
                    # Password character length
                    for i in range(14)
                )
            )
        print("Thank you!")
        break
    except ValueError:
        print("You did not enter a number.")
        continue
