from validator_collection import validators, checkers, errors

try:
    email_address = validators.email(input("What's your email address? "))
    print("Valid")
except errors.InvalidEmailError:
    print("Invalid")
