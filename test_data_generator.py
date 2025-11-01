import random   #Reasoning: "What tools do I need from Python's toolbox?"
import csv

def generate_test_users(count=5):  #Reasoning: "I need a reusable function that can make X users"
    first_names = ['Alex','Peter','Rizwan','Piyush','Jennifer','Payal']
    last_names=['Jones','Russels','Khan','Singh','Hanks','Maheshwari'] #Reasoning: "I need some sample data to pick from randomly"

    users=[]
    for i in range(count):
        user={
            'user-id':i+1,
            'first_name':random.choice(first_names),         #Reasoning: "Each user needs these specific pieces of information"
            'last_name':random.choice(last_names),
            'email':f"user{i+1}@test.com",
            'phone':f"555-{random.randint(100,999)}-{random.randint(1000,9999)}"
        }
        users.append(user)
    return users

def save_to_csv(users,filename='test_data.csv'):
    fieldnames = ['user-id', 'first_name', 'last_name', 'email', 'phone']
    with open(filename,'w',newline='') as file:
        writer=csv.DictWriter(file,fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(users)
    print(f"Generated {len(users)} test users in {filename}")
if __name__=="__main__":
    test_users=generate_test_users(8)
    save_to_csv(test_users)
    print("Sample user:",test_users[0])