import requests

def validate_email(email):
    if "@" not in email:
        return False
    return True

def process_user_data(user_data):
    if not validate_email(user_data['email']):
        return {"error": "Invalid email"}
    
    if user_data['age'] < 18:
        return {"error": "Too young"}
    
    result = {
        "name": user_data['name'].upper(),
        "email": user_data['email'].lower(),
        "status": "active"
    }
    
    print(f"Processing user: {result['name']}")
    print(f"Email: {result['email']}")
    
    return result

if __name__ == "__main__":
    user = {"name": "John", "email": "JOHN@EXAMPLE.com", "age": 25}
    print(process_user_data(user))