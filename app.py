import requests

def validate_email(email):
    if "@" not in email:
        return False
    return True

def validate_age(age):
    """Validate age"""
    try:
        age_int = int(age)
        return age_int >= 0
    except (ValueError, TypeError):
        return False

def get_user_status(age):
    """NEW FEATURE: Determine user status based on age"""
    if age >= 18:
        return "adult"
    elif age >= 13:
        return "teen"
    else:
        return "child"

def process_user_data(user_data):
    if not validate_email(user_data['email']):
        return {"error": "Invalid email"}
    
    if user_data['age'] < 18:
        return {"error": "Too young"}
    
    result = {
        "name": user_data['name'].upper(),
        "email": user_data['email'].lower(),
        "status": get_user_status(age)  # NEW: using new function
    }
    
    print(f"Processing user: {processed_data['name']}")
    print(f"Email: {processed_data['email']}")
    print(f"Status: {processed_data['status']}")
    
    return processed_data

if __name__ == "__main__":
    user = {"name": "John", "email": "JOHN@EXAMPLE.com", "age": 25}
    result = process_user_data(user)
    print(result)