def student_authentication(username, password, student_database):
    """
    Function to authenticate a student based on username and password against a student database. 

    Args:
        username (str): The student's username. 
        password (str): The student's password.
        student_database (dict): A dictionary storing student details where keys are usernames and values are passwords. 

    Returns:
        bool: True if authentication successful, False otherwise. 
    """

    if username in student_database and student_database[username] == password:
        return True
    else: 
        return False 
    

#Example usage
student_data = {
        "user1": "pass1", 
        "user2": "pass2"
    } 


print(student_authentication("user1", "pass1", student_data)) 
print(student_authentication("user12", "pass2", student_data)) 