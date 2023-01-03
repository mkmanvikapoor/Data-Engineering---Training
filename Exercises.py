data = {}

for i in range(3):
    name = input("Enter name")
    phoneNumber = input("Enter the phone number")
    email = input("Enter email")

    data[name] = {phoneNumber, email}
print(data)