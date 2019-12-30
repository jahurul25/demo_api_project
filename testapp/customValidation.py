def chkUserValidation(user_name, user_password):
    if len(user_name.strip()) > 3 and len(user_password.strip()) > 3:
        return True
    elif len(user_name.strip()) < 3 and len(user_password.strip()) < 3:
        return "Username and password must required"    
    elif len(user_name.strip()) < 3 and len(user_password.strip()) > 3:
        return "Username must required and minimum length 3"    
    elif len(user_name.strip()) > 3 and len(user_password.strip()) < 3:
        return "User password must required and minimum length 3"    