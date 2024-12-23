# Create a function called save_emails. This function takes no
# arguments but asks the user to input email, and it saves the
# emails in a CSV file. The user can input as many emails as they
# want. Once they hit ‘done’ the function saves the emails and
# closes the file. Create another function called open_emails.
# This function opens and reads the content of the CSV file. Each
# email must be in its line. Here is an example of how the emails
# must be saved:
# jj@gmail.com
# kate@yahoo.com
# and not like this:
# jj@gmail.comkate@yahoo.com

mail_list = []
choice = input("""please enter your choice:
1- enter mail
2- display mail lists
: """)

def save_emails():
    while True:
        email = input("please enter your email (to exit hit 'done'): ")
        if email != "done":
            with open("email.csv", mode='a', encoding="utf-8") as file:
                file.write(email+" "+"\n")
                #mail_list.append(file)
                #print(mail_list)
                file.close()

        else:
            break
    open_emails()

def open_emails():
    with open("email.csv", mode='r', encoding="utf-8") as file:
        files = file.read().split()
        for i in files:
            print(i)
        file.close()

if choice == "1":
    save_emails()
elif choice == "2":
    open_emails()
