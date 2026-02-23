# from pathlib import Path
# import json
# import random
# import string

# class Bank:
#     database='data.json'
#     data=[] # yeh data json mei add hoga

#     try:
#         if Path(database).exists():
#             print("database exists.....")
#             with open(database) as fs:
#                 data=json.loads(fs.read())
#                 print(data)
#         else:
#             print("no such file exists")
    
#     except Exception as err:
#         print(f"Error occured {err}")
    
#     @classmethod
#     def __update(cls):
#         with open(cls.database,"w") as file:
#             file.write(json.dumps(cls.data))

#     @staticmethod
#     def __generateacc():
#         digits=random.choices(string.digits,k=4)
#         alpha=random.choices(string.ascii_letters,k=4)
#         id=digits+alpha
#         random.shuffle(id)
#         return "".join(id)

#     def createaccount(self):
#         info={"name":input("enter your name:"),
#           "age":int(input("enter your age: ")),
#           "mail":input("enter your email: "),
#           "mobile":int(input("enter your mobile number: ")),
#           "pin":int(input("enter your pin")),
#           "accountno":Bank.__generateacc(),
#           "balance":0}
#         if info["age"]>18 and len(str((info["pin"])))==4 and len(str((info["mobile"])))==10:
#             Bank.data.append(info)
#             Bank.update()
#             print("data is added to the list")
#             print(Bank.data)
#         else:
#             print("credential are not valid")

#     def depositmoney(self):
#         accountno=input("enter your account no: ")
#         pin=int(input("enter your pin: "))
#         user_data=[i for i in Bank.data if i ["accountno"]==accountno and i ["pin"]==pin]# this kind of loop is known as list comprehension
#         print(user_data)
#         if user_data==False:
#             print("user not found")
#         else:
#             amount=int(input("enter your amount: "))
#             if amount<=0:
#                 print("invalid amount")
#             elif amount>10000:
#                 print("amount limit exceeded")
#             else:
#                 user_data[0]["balance"] += amount
#                 Bank.update()
#                 print("amount credited")

#     def withdrawmoney():
#         accountno=input("enter your accountno: ")
#         pin=int(input("enter your pin: "))
#         user_data=[i for i in Bank.data if i["accountno"]==accountno and i["pin"]==pin]
#         if user_data==False:
#             print("user not found")
#             amount=int(input("enter your amount: "))
#             if amount<=0:
#                 print("invalid amount")
#             elif amount>10000:
#                 print("amount limit exceeded")
#         else:
#                 user_data[0]["balance"]-=amount
#                 Bank.update()
#                 print("amount debited")

#     def delete(self):
#         accountno=input("enter your account number:  ")
#         pin=int(input("enter your pin: "))
#         user_data=[i for i in Bank.data if i ["accountno"]==accountno and i ["pin"]==pin]
#         if user_data==False:
#             print("user not found")
#         else:
#             print("are you sure you want to delete your account")
#             choice=input("enter your choice: ")
#             if choice=="yes":
#                 ind=Bank.data.index(user_data[0])
#                 Bank.data.pop(ind)
#                 Bank.__update()
#                 print("account has been deleted successfully")
#             else:
#                 print("operation terminated")

#     def details(self):
#         accountno=input("enter your accountno: ")
#         pin=int(input("enter your pin: "))
#         user_data=[i for i in Bank.data if i ["accountno"]==accountno and i ["pin"]==pin]
#         if user_data==False:
#             print("user not found")
#         else:     
#             print(user_data)

#     def updatedetails(self):
#         accountno=input("enter your account number:  ")
#         pin=int(input("enter your pin: "))
#         user_data=[i for i in Bank.data if i ["accountno"]==accountno and i ["pin"]==pin]
#         if user_data==False:
#             print("user not found")
#         else:
#             print("aap account number change nhi karskete ho")
#             print("enter your delatils to be updated or just press enter")

#             newdata={
#                 "name":input("enter your new name or just press enter"),
#                 "mail":input("enter your new email"),
#                 "mobile":input("enter your new mobile number"),
#                 "pin":input("enter your new pin")
#             }
#             if newdata["name"]=="":
#                 newdata["name"]=user_data[0]["name"]
#             if newdata["mail"]=="":
#                 newdata["mail"]==user_data[0]["mail"]
#             if newdata["mobile"]=="":
#                 newdata["mobile"]=user_data[0]["mobile"]
#             else: 
#                 newdata["mobile"]=int(newdata["mobile"])
#             if newdata["pin"]=="":
#                 newdata["pin"]=user_data[0]["pin"]
#             else:
#                 newdata["pin"]=int(newdata["pin"])
#             newdata["accountno"]=user_data[0]["accountno"]
#             newdata["balance"]=user_data[0]["balance"]
#             user_data[0].update(newdata)
#             Bank.update()
            
# obj=Bank()
# print("press 1 for creating account")
# print("press 2 for depositing money")
# print("press 3 for withdrawing money")
# print("press 4 for account details")
# print("press 5 for updating account details")
# print("press 6 for deleting account")
# choice=int(input("enter your choice"))
# if choice==1:
#     obj.createaccount()
# elif choice==2:
#     obj.depositmoney()
# elif choice==3:
#     obj.withdrawmoney()
# elif choice==4:
#     obj.details()
# elif choice==5:
#     obj.update()
# elif choice==6:
#     obj.deleteaccount()
# else:
#     print("invalid entry")


import streamlit as st
import json
import random
import string
from pathlib import Path

class Bank:
    database = 'data.json'
    
    @classmethod
    def load_data(cls):
        if Path(cls.database).exists():
            with open(cls.database, "r") as fs:
                try:
                    return json.load(fs)
                except json.JSONDecodeError:
                    return []
        return []

    @classmethod
    def save_data(cls, data):
        with open(cls.database, "w") as file:
            json.dump(data, file, indent=4)

    @staticmethod
    def generate_acc():
        digits = random.choices(string.digits, k=4)
        alpha = random.choices(string.ascii_letters, k=4)
        acc_id = digits + alpha
        random.shuffle(acc_id)
        return "".join(acc_id)

# --- Streamlit UI Setup ---
st.set_page_config(page_title="Python Digital Bank", page_icon="🏦")
st.title("🏦 Digital Banking System")

# Initialize data in session state for persistence within the app
if 'bank_data' not in st.session_state:
    st.session_state.bank_data = Bank.load_data()

data = st.session_state.bank_data

# Sidebar Navigation
menu = ["Create Account", "Deposit Money", "Withdraw Money", "Account Details", "Update Details", "Delete Account"]
choice = st.sidebar.selectbox("Select Action", menu)

# --- Functionalities ---

if choice == "Create Account":
    st.subheader("📝 Open a New Account")
    name = st.text_input("Full Name")
    age = st.number_input("Age", min_value=0, max_value=120, step=1)
    email = st.text_input("Email")
    mobile = st.text_input("Mobile Number (10 digits)")
    pin = st.text_input("Set 4-Digit PIN", type="password")

    if st.button("Register"):
        if age >= 18 and len(pin) == 4 and len(mobile) == 10:
            new_acc = {
                "name": name,
                "age": age,
                "mail": email,
                "mobile": int(mobile),
                "pin": int(pin),
                "accountno": Bank.generate_acc(),
                "balance": 0
            }
            data.append(new_acc)
            Bank.save_data(data)
            st.success(f"Account Created! Your Account No is: {new_acc['accountno']}")
        else:
            st.error("Invalid details. Ensure age is 18+, PIN is 4 digits, and mobile is 10 digits.")

elif choice == "Deposit Money":
    st.subheader("💰 Deposit Funds")
    acc_no = st.text_input("Enter Account Number")
    pin = st.text_input("Enter PIN", type="password")
    amount = st.number_input("Amount to Deposit", min_value=0)

    if st.button("Deposit"):
        user = [i for i in data if i["accountno"] == acc_no and i["pin"] == int(pin or 0)]
        if user:
            if 0 < amount <= 10000:
                user[0]["balance"] += amount
                Bank.save_data(data)
                st.success(f"Successfully deposited ₹{amount}. New Balance: ₹{user[0]['balance']}")
            else:
                st.warning("Amount must be between 1 and 10,000")
        else:
            st.error("Invalid Account Number or PIN")

elif choice == "Withdraw Money":
    st.subheader("💸 Withdraw Funds")
    acc_no = st.text_input("Enter Account Number")
    pin = st.text_input("Enter PIN", type="password")
    amount = st.number_input("Amount to Withdraw", min_value=0)

    if st.button("Withdraw"):
        user = [i for i in data if i["accountno"] == acc_no and i["pin"] == int(pin or 0)]
        if user:
            if amount > user[0]["balance"]:
                st.error("Insufficient Balance!")
            elif 0 < amount <= 10000:
                user[0]["balance"] -= amount
                Bank.save_data(data)
                st.success(f"Successfully withdrawn ₹{amount}. Remaining Balance: ₹{user[0]['balance']}")
            else:
                st.warning("Limit: Max ₹10,000 per transaction")
        else:
            st.error("Invalid Credentials")

elif choice == "Account Details":
    st.subheader("🔍 Check Balance & Details")
    acc_no = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("View Details"):
        user = [i for i in data if i["accountno"] == acc_no and i["pin"] == int(pin or 0)]
        if user:
            st.json(user[0])
        else:
            st.error("User not found")

elif choice == "Update Details":
    st.subheader("🔄 Update Profile")
    acc_no = st.text_input("Account Number")
    pin = st.text_input("Current PIN", type="password")
    
    user = [i for i in data if i["accountno"] == acc_no and i["pin"] == int(pin or 0)]
    
    if user:
        st.info("Leave blank to keep current information")
        new_name = st.text_input("New Name", value=user[0]["name"])
        new_mail = st.text_input("New Email", value=user[0]["mail"])
        
        if st.button("Update Profile"):
            user[0]["name"] = new_name
            user[0]["mail"] = new_mail
            Bank.save_data(data)
            st.success("Profile Updated Successfully!")

elif choice == "Delete Account":
    st.subheader("❌ Close Account")
    acc_no = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    confirm = st.checkbox("I understand this action is permanent")

    if st.button("Delete Account"):
        if confirm:
            user = [i for i in data if i["accountno"] == acc_no and i["pin"] == int(pin or 0)]
            if user:
                data.remove(user[0])
                Bank.save_data(data)
                st.success("Account deleted successfully.")
            else:
                st.error("Invalid credentials")
        else:
            st.warning("Please check the confirmation box.")