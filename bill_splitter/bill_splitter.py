# write your code here
import random
guest_dict = {}

guest_count = input ("Enter the number of friends joining (including you): ")

if int(guest_count) > 0:
    for meh in range(int(guest_count)):
        guest_name = input ("Enter the name of every friend (including you), each on a new line: ")
        guest_dict[guest_name] = 0

    total_bill = input ("Enter the total bill value: ")
    lucky_who = input ('Do you want to use the "Who is lucky?" feature? Write Yes/No: ')
    lucky_you = random.choice(list(guest_dict.keys()))
    personal_bill = round(float(total_bill) / float(guest_count), 2)
    personal_bill_lucky = round(float(total_bill) / float(int(guest_count) - 1), 2)
    
    if lucky_who.lower() == 'yes':
        print(lucky_you + " is the lucky one!")
        for guest_name in guest_dict:
          guest_dict[guest_name] = personal_bill_lucky
          guest_dict[lucky_you] = 0
        print(guest_dict)
    else:
        print("No one is going to be lucky")
        for guest_name in guest_dict:
          guest_dict[guest_name] = personal_bill
        print(guest_dict)
    
    for x in guest_dict:
        guest_dict[x] = personal_bill      
    #print(guest_dict)
else:
    print ('No one is joining for the party')  
