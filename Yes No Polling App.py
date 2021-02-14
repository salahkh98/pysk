print("welcome to the yes or no Issue Polling app")

polling_data = {
    "polling":"3181998",
    "voters":{

    },
}
yes = 0
no = 0

issue = input("what is the yes or no issue you will be voting on today: ")
voters_number = int(input("what is the number of voters you will allow in the issue: "))

polling_password = str(input("Enter a password for polling results: ").lower())
while polling_password != polling_data["polling"]:
    polling_password = str(input("Enter a password for polling results: ").lower())
        
for vot in range(voters_number):
    voter_name = input("\nEnter your full name: ").title()
    if voter_name in polling_data["voters"]:
        print("sorry, it seems that someone with that name has already voted.")
    else:
        print("here is the issue: "+issue)
        polling = input("what do you think......yes or no: ").lower()
        if polling == "yes":
            vote = {voter_name:polling}
            polling_data["voters"].update(vote)
            yes += 1
            print("thank you " + voter_name + "! your vote of " + polling + " has been recorded.")

        elif polling == "no":
            vote = {voter_name:polling}
            polling_data["voters"].update(vote)
            no += 1
            print("thank you " + voter_name + "! your vote of " + polling + " has been recorded.")

        else:
            vote = {voter_name:polling}
            polling_data["voters"].update(vote)
            pass


print("The following "+ str(voters_number) +" people voted:")
for u in polling_data["voters"].keys():
    print(u)


print("\non the following issue: "+ issue)
if yes > no :
    print("yes wins! "+str(yes)+" votes to "+str(no))

elif no > yes:
    print("no wins! "+str(no)+" votes to "+str(yes))

elif no == yes:
    print("it was tie! "+str(yes)+" votes to "+str(no))


results = input("to see the voting result enter the admin password")
while results != polling_data["polling"]:
    results = input("\nto see the voting result enter the admin password: ")

for k , v in polling_data["voters"].items():
    print("voter: " + str(k)+"\t\tvote: "+str(v))

