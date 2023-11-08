# app/db.py
def save_operation(filename, operation):
    with open(filename, 'a') as file:
        file.write(f"{operation}\n")
