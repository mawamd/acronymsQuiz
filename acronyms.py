import json

# Load existing acronyms from 'new_acronyms.json'
with open("new_acronyms.json", "r") as f:
    acronyms = json.load(f)

# Option to add a new acronym
def add_acronym():
    acronym_name = input("Enter the acronym you want to add: ").upper()
    if acronym_name in acronyms:
        print(f"{acronym_name} already exists.")
    else:
        acronyms[acronym_name] = {}
        print(f"Adding {acronym_name}.")
        more_terms = 'yes'
        while more_terms == 'yes':
            letter = input("Enter the acronym letter or term (e.g., T1 for TTTTTH): ").upper()
            meaning = input(f"What does {letter} stand for? ")
            acronyms[acronym_name][letter] = meaning
            more_terms = input("Do you want to add another term? (yes/no): ").lower()
        with open("new_acronyms.json", "w") as f:
            json.dump(acronyms, f, indent=4)
        print(f"{acronym_name} has been added.")

# Test the user on an acronym
def start_acronym_quiz():
    print("Great! Which acronym would you like to be tested on?")
    print("Available acronyms:", list(acronyms.keys()))
    acronym_choice = input("Type the acronym you want to be tested on: ").upper()
    
    if acronym_choice in acronyms:
        acronym = acronyms[acronym_choice]
        print(f"Great, let's start with {acronym_choice}: {acronym}")
        test_acronym(acronym_choice, acronym)
    else:
        print("Sorry, that acronym isn't available. Try again.")
        start_acronym_quiz()

def test_acronym(acronym_choice, acronym_terms):
    # Loop over letters in the acronym and prompt user for meaning
    for key, term in acronym_terms.items():
        user_answer = input(f"What does '{key}' stand for? ")
        if user_answer.strip().lower() == term.strip().lower():
            print(f"Correct! {key} stands for {term}")
        else:
            print(f"Oops! {key} actually stands for {term}")
    
    # Ask if the user wants to continue or end the quiz
    continue_quiz = input("Do you want to continue with another acronym? (yes/no): ").strip().lower()
    if continue_quiz == 'yes':
        main_menu()
    else:
        print("Quiz ended. Thanks for playing!")

# Main menu asking if user wants to add a term or be tested
def main_menu():
    print("Do you want to:")
    print("1. Add a new acronym")
    print("2. Be tested on an acronym")
    
    choice = input("Enter 1 or 2: ")
    
    if choice == '1':
        add_acronym()
    elif choice == '2':
        start_acronym_quiz()
    else:
        print("Invalid choice. Try again.")
        main_menu()

# Start with the main menu
main_menu()
