
def ask_yes_no(question):
    response = None
    while response not in ("y","n"):
        response = input(question)
    return response

def main():
    answer1 = ask_yes_no("Are you over 10 years old?")
    answer2 = ask_yes_no("Do you have the permission slip?")
    if answer1 == 'y' and answer2 == 'y':
        print("You can go to the field trip")
    else:
        print("You cannot go to the field trip")
    

main()
