import mysql.connector

mydb= mysql.connector.connect(
    host='localhost',
    username='***',
    password='***',
    database='*****'
)

MyCursor= mydb.cursor()
Cmd="CREATE DATABASE DhikaStore"
#MyCursor.execute (Cmd)
#mydb.commit()

CMD = "CREATE TABLE consument (id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(255),sex VARCHAR(255),phone INT,address VARCHAR(255),email VARCHAR(255),birthdate DATE)"
#MyCursor.execute(CMD)
#mydb.commit()

CMD = "DESCRIBE consument"
#MyCursor.execute (CMD)
#Result = MyCursor.fetchall()
#for x in Result:
#    print(x)

cmd="ALTER TABLE consument MODIFY COLUMN phone BIGINT"
#MyCursor.execute(cmd)
#mydb.commit()

def input_data_to_consument_table(mydb):
    MyCursor = mydb.cursor()

    while True:
        # Get input from user
        name = input("Enter name: ")
        while True:
            sex = input("Enter sex (Male/Female): ").strip().capitalize()
            if sex in ["Male", "Female"]:
                break
            else:
                print("Invalid input. Please enter Male or Female.")

        while True:
            phone = input("Enter phone number (12 digits): ")
            if phone.isdigit() and len(phone) == 12:
                phone = int(phone)
                break
            else:
                print("Invalid input. Please enter a 12-digit phone number.")

        address = input("Enter address: ")
        email = input("Enter email: ")
        birthdate = input("Enter birthdate (YYYY-MM-DD): ")

        # Insert data into table
        CMD = "INSERT INTO consument (name, sex, phone, address, email, birthdate) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (name, sex, phone, address, email, birthdate)
        MyCursor.execute(CMD, val)
        mydb.commit()

        print("Data inserted successfully!")

        # Ask user if they want to continue
        while True:
            choice = input("Do you want to continue? (Yes/No): ").strip().capitalize()
            if choice in ["Yes", "No"]:
                break
            else:
                print("Invalid input. Please enter Yes or No.")

        if choice == "No":
            if sex == "Male":
                names = "Mr. " + name
            else:
                names = "Ms. " + name
            print(f"Thanks for using our service, {names}! -Dhika")
            break  

    print("Input data finished.")

#Input using terminal
#input_data_to_consument_table(mydb)

#Input using form
import tkinter as tk
from tkinter import messagebox

def submit_form():
    name = name_entry.get()
    sex = sex_var.get()
    phone = phone_entry.get()
    address = address_entry.get()
    email = email_entry.get()
    birthdate = birthdate_entry.get()

    # Insert data into table
    CMD = "INSERT INTO consument (name, sex, phone, address, email, birthdate) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (name, sex, phone, address, email, birthdate)
    MyCursor.execute(CMD, val)
    mydb.commit()

    messagebox.showinfo("Success", "Data inserted successfully, thanks!")

    # Ask user if they want to continue
    choice = messagebox.askyesno("Continue?", "Do you want to continue?")
    if not choice:
        messagebox.showinfo(f"Success","Thanks for using our service! -Dhika")
        root.destroy()

root = tk.Tk()
root.title("Consument Data Entry")

# Create form fields
tk.Label(root, text="Name:").grid(row=0, column=0)
name_entry = tk.Entry(root, width=30)
name_entry.grid(row=0, column=1)

tk.Label(root, text="Sex:").grid(row=1, column=0)
sex_var = tk.StringVar()
sex_var.set("Male")
male_radio = tk.Radiobutton(root, text="Male", variable=sex_var, value="Male")
male_radio.grid(row=1, column=1)
female_radio = tk.Radiobutton(root, text="Female", variable=sex_var, value="Female")
female_radio.grid(row=1, column=2)

tk.Label(root, text="Phone:").grid(row=2, column=0)
phone_entry = tk.Entry(root, width=30)
phone_entry.grid(row=2, column=1)

tk.Label(root, text="Address:").grid(row=3, column=0)
address_entry = tk.Entry(root, width=30)
address_entry.grid(row=3, column=1)

tk.Label(root, text="Email:").grid(row=4, column=0)
email_entry = tk.Entry(root, width=30)
email_entry.grid(row=4, column=1)

tk.Label(root, text="Birthdate:").grid(row=5, column=0)
birthdate_entry = tk.Entry(root, width=30)
birthdate_entry.grid(row=5, column=1)

# Create submit button
submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.grid(row=6, column=1)

root.mainloop()

CMD = "SELECT * FROM consument"
MyResult = MyCursor.execute (CMD)
Result = MyCursor.fetchall()
for x in Result:
    print(x)
