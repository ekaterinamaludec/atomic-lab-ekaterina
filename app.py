import requests

def validate_email(email):
    """Validate email format"""
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
    """Process user data with validation"""
    # REFACTOR: renamed variable from result to processed_data for clarity
    if not validate_email(user_data.get('email', '')):
        return {"error": "Invalid email"}
    
    # FIX: added error handling for missing age field
    try:
        age = int(user_data.get('age', 0))
    except (ValueError, TypeError):
        return {"error": "Invalid age format"}
    
    if age < 18:
        return {"error": "Too young"}
    
    processed_data = {
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