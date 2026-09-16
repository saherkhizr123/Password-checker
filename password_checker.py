
    
        " def check_password(password) ":
score = 0
    # length check 
if len(password) >=8:
     score +=1
    else:
print("❌ Password must be at least 8 characters long. ")
    # Numbers check 
if any (char,isdigit() for char in password):
    score += 1 
else:
    print("❌ Password must contain at least 1 number.")
    # Capital letter check 
if any (char.isupper() for char in password ):
    score +=1
else:
    print("❌ Password must contain at least 1 capital letter")
    # Special character check 
    special_char = "!@#$%^&*"
if any (char in sprcial_char for char in passord):
else:
    print("❌ Password must contain special characters !@#$%^&*")
    # Final result 
    print(f"/nPassword Score: {score}/4)
if score == 4 :
    print("✅ Strong Password! Good job")
elif score >=2:
    print("⚠️ Medium Password.Improve it ")
else:
    print("🚫 Week Password.Change now.")
    # Program start
    user_password = input("Enter your password.")
    check_password(user_password)
        
    
