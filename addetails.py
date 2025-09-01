import re

# Define constants and variables
MAX_ATTEMPTS = 3  # Maximum number of attempts allowed per column
attempts_used = 0  # Counter for attempts used

def check_attempts():
    """Check if maximum attempts have been reached and exit if true"""
    if attempts_used >= MAX_ATTEMPTS:
        print("\n⚠ Maximum attempts reached. Exiting program.")
        return False
    return True

def get_positive_number(prompt, dtype):
    """Get a positive number of specified datatype from user input"""
    global attempts_used
    while True:
        value = input(prompt).strip()
        if not value:
            attempts_used += 1
            if not check_attempts():
                return None
            print(f"⚠ This field cannot be empty. Attempts left: {MAX_ATTEMPTS - attempts_used}")
        else:
            try:
                number = dtype(value)
                if number > 0:
                    return number
                else:
                    attempts_used += 1
                    if not check_attempts():
                        return None
                    print(f"⚠ Please enter a number greater than 0. Attempts left: {MAX_ATTEMPTS - attempts_used}")
            except ValueError:
                attempts_used += 1
                if not check_attempts():
                    return None
                print(f"⚠ Please enter a valid {dtype.__name__}. Attempts left: {MAX_ATTEMPTS - attempts_used}")

def get_string_input(prompt):
    """Get a non-empty string containing at least one letter"""
    global attempts_used
    while True:
        value = input(prompt).strip()
        if not value:
            attempts_used += 1
            if not check_attempts():
                return None
            print(f"⚠ This field cannot be empty. Attempts left: {MAX_ATTEMPTS - attempts_used}")
        elif not re.search(r"[A-Za-z]", value):
            attempts_used += 1
            if not check_attempts():
                return None
            print(f"⚠ This field must contain at least one letter. Attempts left: {MAX_ATTEMPTS - attempts_used}")
        else:
            return value

def reset_attempts():
    """Reset the attempts counter for a new input"""
    global attempts_used
    attempts_used = 0