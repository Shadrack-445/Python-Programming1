attempts = 0
max_attempts = 3

footballers = ["messi","ronaldo","neymar"]
sports = ["golf","lacrosse","chess"]
languages = ["french","spanish","russian"]

game_over = False

while not game_over:
    category = input("Choose a category between footballers,sports and languages:").lower()
    if category == "footballers":
        while attempts<max_attempts:
            print(f"You have {max_attempts-attempts} attempts left")
            footballer_attempt = input("Enter any footballers name:").lower()
            if footballer_attempt in footballers:
                print("That is correct.YOU WIN!")
                game_over = True
                break
            else:
                attempts += 1
                if attempts<max_attempts:
                    print("Wrong!Try again")
                else:
                    print("GAME OVER!YOU LOSE")
                    game_over = True
                
                
    elif category == "sports":
        while attempts<max_attempts:
            print(f"You have {max_attempts-attempts} attempts left")
            sport_attempt = input("Enter any sport:").lower()
            if sport_attempt in sports:
                print("That is correct.YOU WIN!")
                game_over = True
                break
            else:
                attempts += 1
                if attempts<max_attempts:
                    print("Wrong!Try again")
                else:
                    print("GAME OVER!YOU LOSE")
                    game_over = True
                
    elif category == "languages":
        while attempts<max_attempts:
            print(f"You have {max_attempts-attempts} attempts left")
            language_attempt = input("Enter any language:").lower()
            if language_attempt in languages:
                print("That is correct.YOU WIN!")
                game_over = True
                break
            else:
                attempts += 1
                if attempts<max_attempts:
                    print("Wrong!Try again")
                else:
                    print("GAME OVER!YOU LOSE")
                    game_over = True
                
    else:
        print("Invalid category!Try again")










