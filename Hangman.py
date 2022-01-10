import requests

def hangman(word):
    res = "_" * len(word)       #creating '_' string
    lives = 5
    
    print(res)
    print("Lives = ", lives)
    
    guessed_letters = []


    while lives > 0 and '_' in res:
        guess = input("Guess a lettter = ").lower()
        
        #if guessed letter is already guessed
        if guess in guessed_letters:
            print("Letter is already guessed")
            print(res)
            print(lives)
            continue
        
        #if guessed letter is not in word
        if guess not in word:
            lives -= 1
            guessed_letters.append(guess)   #adding guessed letter in list
            print("Incorrect Guess")
            print(res)
            print(lives)
            continue

        #letter is correctly guessed
        guessed_letters.append(guess)
        letter_list = list(res)     #converting res to a list of letters 
                                    #to ease replacement of '_' with guessed letters
        
        #enumerating over the string word to get indices where guessed letters appears
        #in random word and then itterating over that list to replace '_' at those indices
        for i in ([j for j, l in enumerate(word) if guess == l]):  
            letter_list[i] = guess      #replaceing '_' with correct guessed letter
                
        res = "".join(letter_list)      #converting list back to word
        print(res)
        print(lives)
        
    if lives == 0:
        print("Word was = ", word)
         
def main():
    
    #get random word from given link
    word = str(requests.get("https://random-word-api.herokuapp.com/word?number=1").json()[0])
    hangman(word)


if __name__ == '__main__':
    main()
