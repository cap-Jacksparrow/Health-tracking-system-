import json
import math
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
Underweight =["Consult a healthcare professional for a thorough assessment.", "Focus on a balanced diet to gain weight in a healthy way.","Incorporate strength training exercises to build muscle mass."]
Normalweight=["Maintain a balanced diet with a variety of nutrients."," Engage in regular physical activity to stay fit."," Continue to monitor your weight and health."]
Overweight=["Aim to lose weight through a combination of diet and exercise.", "Reduce calorie intake and increase physical activity.","Consult a healthcare provider for a personalized plan."]
Obesity=["Seek professional guidance for weight management."," Focus on a well-balanced, low-calorie diet.","Incorporate regular physical activity into your routine.","Monitor your health closely for associated conditions."]

# Define the file path for storing credentials
USER_CREDENTIALS_FILE = "user_credentials1.json"
ADMIN_CREDENTIALS_FILE = "admin_credentials1.json"

# Define the dictionary to store admin credentials
admin_credentials = {
    "username": "admin",
    "password": "admin123",
    "is_signed_up": False,
    }

# Define the dictionary to store user credentials
user_credentials = {}

# Function to save admin credentials to a file
def save_admin_credentials():
    with open(ADMIN_CREDENTIALS_FILE, "w") as file:
        json.dump(admin_credentials, file)

# Function to load admin credentials from a file
def load_admin_credentials():
    global admin_credentials
    try:
        with open(ADMIN_CREDENTIALS_FILE, "r") as file:
            admin_credentials = json.load(file)
    except FileNotFoundError:
        save_admin_credentials()

# Function to save user credentials to a file
def save_user_credentials():
    with open(USER_CREDENTIALS_FILE, "w") as file:
        json.dump(user_credentials, file)

# Function to load user credentials from a file
def load_user_credentials():
    global user_credentials
    try:
        with open(USER_CREDENTIALS_FILE, "r") as file:
            user_credentials = json.load(file)
    except FileNotFoundError:
        save_user_credentials()

# Function for admin sign-up
def admin_signup():
    if not admin_credentials["is_signed_up"]:
        username = input("Enter admin username: ")
        password = input("Enter admin password: ")
        admin_credentials["username"] = username
        admin_credentials["password"] = password
        admin_credentials["is_signed_up"] = True
        print("---------------------")
        print("|sign-up successful! |")
        print("---------------------")

        save_admin_credentials()  # Save the admin credentials to a file

        return True
    else:
        print("Admin is already signed up.")
        return False
# Function for admin login
def admin_login():
    username = input("Enter admin username: ")
    password = input("Enter admin password: ")
    if (
        username == admin_credentials["username"]
        and password == admin_credentials["password"]
        and admin_credentials["is_signed_up"]
    ):
        print("----------------------------")
        print("|    login successful!     |")
        print("----------------------------")

        

        save_admin_credentials()  # Save the admin credentials to a file

        return True
    else:
        print("Invalid admin credentials.")
        return False
# Function for user sign-up
def user_signup():
    username = input("Enter a username: ")
    password = input("Enter a password: ")

    if username in user_credentials:
        print("Username already exists. Please choose a different username.")
    else:
        user_credentials[username] = password
        save_user_credentials()  # Save the user credentials to a file
        print("---------------------------")
        print("| User sign-up successful! |")
        print("--------------------- ------")

# Function for user login
def user_login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username in user_credentials and user_credentials[username] == password:
        print("----------------------------")
        print("| User login successful!   |")
        print("----------------------------")

        return True
    else:
        print("Invalid username or password.")
        return False
def update():
    print("update")
def add_recomendations():
    print("add recomendations")
    
def main():
    print("      HEALTH TRACKING SYSTEM")
    print("     _________________________")

    load_admin_credentials()

    load_user_credentials() 

    while(True):
        print("Please select an option:")
        print("1.  Doctor")
        print("2.  User")
        print("3.  Contact")
        print("4.  Exit")
        choice=input("Enter your choice(1-4):")
        if choice=="1":
            print("---------------------------")
            print("    Welcome, Doctor!")
            print("---------------------------")
            print("Please select an option:")
            print("1. Sign-up")
            print("2. Login")
            admin_choice = input("Enter your choice (1-2): ")
            if admin_choice == "1":
                print("Sign-up option selected.")
                if admin_signup():
                    print("signup successful!")
                else:
                    print("signup failed. Please try again.")
            elif admin_choice =="2":
                print("Login option selected.")
                if admin_login():
                    while True:
                        print("Please select an option:")
                        print("=========================================")
                        print("1.  Add recommendations")
                        print("_________________________________________")
                        print("2. Logout")
                        print("_________________________________________")
                        admin_action = input("Enter your choice (1-2): ")
                        if admin_action == "1":
                             print("Select a domain to add recommendation ")
                             print("1. Under weight")
                             print("2. Normal weight")
                             print("3. Over weight")
                             print("4. Obesity")
                             case=input("Enter a choice(1-4)")
                             if case =="1":
                                 print(Underweight)
                                 a=input("Enter recommendation ")
                                 Underweight.append(a)
                             elif case =="2":
                                 print(Normalweight)
                                 b=input("Enter recommendation ")
                                 Normalweight.append(b)
                                            
                             elif case == "3":
                                 print(Overweight)
                                 c=input("Enter recommendation ")
                                 Overweight.append(c)
                             elif case =="4":
                                print(Obesity)
                                d=input("Enter recommendation ")
                                Obesity.append(d)
                             else:
                                 return "Default Case"
                        elif admin_action == "2":
                            print("logout successfully")
                            break
                        else:
                            print("Invalid choice. Please try again.")
                else:
                    print("login failed. Please try again.")

        elif choice =="2":
            print("-----------------------------")
            print("Welcome, User!")
            print("-----------------------------")
            print("Please select an option:")
            print("1. User Sign-up")
            print("2. User Login")
            user_choice = input("Enter your choice (1-2): ")
            if user_choice == "1":
                print("User Sign-up option selected.")
                user_signup()
            elif user_choice == "2":
                print("User Login option selected.")
                if user_login():
                   while True:
                        print("Please select an option:")
                        print("1. Body mass index calculator")
                        print("2. Logout")

                        user_action = input("Enter your choice (1-2): ")

                        if user_action == "1":
                             def calculate_bmi(weight_kg,height_m):
                                 bmi=weight_kg/(math.pow(height_m,2))
                                 return bmi
                             weight=float(input("Enter your Weight in kg: "))
                             height=float(input("Enter your Height in m: "))
                             bmi_result=calculate_bmi(weight,height)
                             print("Your body mass index is: ",bmi_result)
                             if bmi_result<18.5:
                                 print("::Under weight::")
                                 print(Underweight)
                                 break
                             if bmi_result>=18.5 and bmi_result<=24.9:
                                  print("::Normal weight::")
                                  print(Normalweight)
                                  break
                             if bmi_result>=25 and bmi_result<=29.9:
                                 print("::Over weight::")
                                 print(Overweight)
                                 break
                             if bmi_result>30:  
                                 print(":: Obesity::")
                                 print(Obesity)
                        elif user_action == "2":
                            print("Logged out successfully!")
                            break
                        else:
                            print("Invalid choice. Please try again.")
                else:
                    print("User login failed. Please try again.")
        elif choice =="3":
            print("-----------------------------")
            print("Contact Information")
            print("-----------------------------")
            print("Please contact us at:")
           
            sender_email =input("Enter your email :")
            receiver_email = "healthtracker.bmi@gmail.com"
            password =input("Enter your app password(turn on on 2-step verification and generete an app password)")
            smtp_server = "smtp.gmail.com"
            smtp_port = 587  # Port for TLS (587 for Gmail)
            message = MIMEMultipart()
            message["From"] = sender_email
            message["To"] = receiver_email
            message["Subject"] = input("Subject of your email")
            body=input("Enter message: ")
            message.attach(MIMEText(body,"plain"))
            try: 
             server = smtplib.SMTP(smtp_server, smtp_port)
             server.starttls()  # Upgrade the connection to secure TLS
             server.login(sender_email, password)
             server.sendmail(sender_email, receiver_email, message.as_string())
             print("Email sent successfully!")
            except Exception as e:
             print(f"An error occurred: {e}")
            finally:
             server.quit()  # Close the SMTP server connection
            print("developers:Abhijith,Ihsan,Anand,Surya dev") 
        elif choice =="4":  
            print("Exiting the program....") 
            print("THANK FOR USING HEALTH TRACKING SYSTEM")
            break
        else:
            print("Invalid choice. Please try again.")

main()    