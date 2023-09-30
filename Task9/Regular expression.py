import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def validate_bangladeshi_mobile(mobile):
    pattern = r'^01[3-9]\d{8}$'
    return bool(re.match(pattern, mobile))

def validate_usa_telephone(telephone):
    pattern = r'^\d{10}$'
    return bool(re.match(pattern, telephone))

def validate_password(password):
    pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%^&+=])[A-Za-z\d@#$%^&+=]{16}$'
    return bool(re.match(pattern, password))

if __name__ == "__main__":
    # Test email validation
    email = "example@email.com"
    print(f"Is {email} a valid email address? {validate_email(email)}")

    # Test Bangladeshi mobile number validation
    mobile = "01712345678"
    print(f"Is {mobile} a valid Bangladeshi mobile number? {validate_bangladeshi_mobile(mobile)}")

    # Test USA telephone number validation
    telephone = "1234567890"
    print(f"Is {telephone} a valid USA telephone number? {validate_usa_telephone(telephone)}")

    # Test password validation
    password = "Abc@1234defGh$5678"
    print(f"Is '{password}' a valid 16-character alphanumeric password? {validate_password(password)}")