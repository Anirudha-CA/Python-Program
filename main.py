
username=input("Enter username ").lower()
print(username)
password=input("Enter the password ")
while(len(password)<6):
    password=input("Enter atleast min of 6 characters ")
print(password)
mobileno=input("Enter the Mobile Number ")
while((len(mobileno)!=10) or (not(mobileno.isdigit()))):
    mobileno=input("Enter the Mobile Number Correctly ")
print(mobileno)
print("Account Created Successfully,Login Now!")
for i in range(0,5):
    print("*\n")
print("Login Process\n")
usernamel=input("Enter Username ").lower()
passwordl=input("Enter the Password ")
if((usernamel==username) or (passwordl==password)):
    for i in range(5,0,-1):
        if(usernamel!=username):
            print("Entered Username is incorrect,eneter again!\n")
            usernamel=input("Enter Username ").lower()
        if(passwordl!=password):
            print("Entered Password is incorrect,enter again!\n")
            passwordl=input("Enter the Password ")
        if((usernamel==username) and (passwordl==password)):
            break;
        print("Remaining Attempts: ",i-1)
if(i==1):
    print("Account Blocked!!!")
if((usernamel==username) and (passwordl==password)):
    print("Login Successful!")