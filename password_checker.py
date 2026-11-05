def password_strength(password):
    if " " in password:
        return "Invalid input!"

    # check password length

    password_length = len(password) >= 8

    if len(password) < 8:
        return"Password must be at least 8 characters"


    # check for quality
    has_upper =any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_symbol = any(not char.isalnum() for char in password)
    has_number = any(char.isnumeric() for char in password)


    # password score

    password_score = sum([password_length, has_lower, has_number, has_symbol, has_upper])

    if password_score == 5:
        return"Password strength: strong"
    elif password_score <=3:
        return"Password strength : medium"
    else:
        return"Weak Password"


