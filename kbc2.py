print("\'Welcome to Kaun Banega Crorpati\'\n")
user=input("Do you want to play the game(y/n)?:-")
if user=="y":
    print("\nHere are your questions:")
else:
    quit("You chose not to play the game")
qts=[
[
    "Who is the 51st Chief Justie of India?",
     "D.Y Chandrachud","Sanjiv Khanna","Hema Kohli","Girish Murmu",
     "None",2
],

[
    "Which is the tallest statue in the world?",
     "Statue of Unity","Christ the Redeemer","Statue of Liberty","Spring Temple Buddha",
     "None",1
],

[
    "Who was the 2nd Prime Minister of India?",
     "Pandit Jawaharlal Nehru","Sardar Vallabhbhai Patel","Sarvepallai Radhakrishna","Lal Bahadur Shastri",
     "None",4
],

[
    "Who founded the Indian National Army in 1942?",
     "Subhas Chandra Bose","Mohan Singh","ChandraShekhar Azad","Rash Bihari Bose",
     "None",2
],

[
    "Which is the tallest peak in Indai?",
     "K2","Kanchenjunga","Mount Everest","Nanda Devi Peak",
     "None",2
],

[
    "Which Indian state is known as Valley of Flowers?",
     "Jammu & Kashmir","Kerala","Uttarakhand","Assam",
     "None",3
],

[
    "Which animal is desiganted as the national aqautic animal of India?",
     "Gangetic River Dolphin","Dugongs","Sea Horse","Piranha",
     "None",1
],
[
    "Who is the current Director of CBI(Crime Bureau of Investigation)?",
     "Tapan Deka","Pravin Sood","Ashok Kumar","Amit Lodha",
     "None",2
],
[
    "Who was Barbarik in Mahabharata?",
     "Son of Arjun","Son of Bheem","Son of Ghatotkacha","Son of Balram",
     "None",3
],
[
    "From the following which is the largest freshwater lake in India?",
     "Dal Lake","Lonar Lake","Didwana Lake","Wular lake",
     "None",4
],
[
    "How many biodiversity hotspots are there in India?",
     "One","Two","Four","Zero",
     "None",3
],
[
    "Which among the following is the largest river in the world?",
     "Amazon River","River Nile","Congo River","Brahmaputra River",
     "None",1
],
[
    "Which country is known as the \'Land of the Midnight Sun\'?",
     "Sweden","Norway","Greenland","Ireland",
     "None",2
],
[
    "Who was the first Indian to win a Nobel Prize?",
     "Dr.Bhimrao Ambedkar","Lala Lajpat Rai","Dr. A P J Abdul Kalam","Rabindranath Tagore",
     "None",4
],
[
    "Who was the first women in space?",
     "Kalpana Chawla","Sally Ride","Valentina Tereshkova","Anna Fisher",
     "None",3
],

]
levels=[1000, 2000, 3000, 5000, 10000,
         20000, 40000, 80000, 160000,320000,640000,1280000,2560000,5000000,10000000]
money=0
i=0
for i in range(0,len(qts)):
    qt=qts[i]
    print(f"\n\nQuestion for Rs.{levels[i]}")
    print(f"\n{qt[0]}")
    print(f"1.{qt[1]}      2.{qt[2]}")
    print(f"3.{qt[3]}      4.{qt[4]}")
    res=int(input("enter answer from (1-4):-"))
    if (res==qt[-1]):
        print(f"correct answer! \nyou have won Rs.{levels[i]}")
        if(i==2):
            money=1000
        elif(i==4):
            money=10000
        elif(i==9):
            money=320000
        elif(i==11):
            money=1280000
        elif(i==14):
            money=10000000
            print("Congratulations!\nYou are now a \'crorepati\'")
    else:
        print("\nwrong answer!")
        print("\nYou can no longer continue,\n Thank You for playing")
        break
print(f"\nYour take home money is {money}")