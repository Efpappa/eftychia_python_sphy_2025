import random

def guess_the_number():
    print("Καλώς ήρθες στο Guess the Number Game!")
    print("Επίλεξε επίπεδο δυσκολίας:")
    print("1. Εύκολο (1-10)")
    print("2. Μεσαίο (1-50)")
    print("3. Δύσκολο (1-100)")

    level = input("Επίλεξε 1, 2 ή 3: ")

    if level == "1":
        number = random.randint(1, 10)
        max_attempts = 5
    elif level == "2":
        number = random.randint(1, 50)
        max_attempts = 7
    elif level == "3":
        number = random.randint(1, 100)
        max_attempts = 10
    else:
        print("Μη έγκυρη επιλογή, ξεκινάμε στο Εύκολο επίπεδο.")
        number = random.randint(1, 10)
        max_attempts = 5

    attempts = 0
    while attempts < max_attempts:
        guess = int(input("Μάντεψε τον αριθμό: "))
        attempts += 1

        if guess < number:
            print("Ο αριθμός είναι μεγαλύτερος!")
        elif guess > number:
            print("Ο αριθμός είναι μικρότερος!")
        else:
            print(f"Συγχαρητήρια! Μάντεψες σωστά τον αριθμό {number} σε {attempts} προσπάθειες!")
            break
    else:
        print(f"Δυστυχώς, δεν τα κατάφερες. Ο αριθμός ήταν {number}.")

guess_the_number()
