import random
def NameID():

    aldo_leon_art = """
    ⚫⚫⚪⚪⚫⚫⚫⚪⚪⚪⚪⚫⚫⚪⚪⚪⚫⚫⚪⚪⚪⚫⚫⚫⚪⚪⚫⚫
    ⚫⚫⚪⚪⚫⚫⚫⚪⚪⚪⚪⚫⚪⚪⚫⚪⚪⚫⚪⚪⚪⚫⚫⚫⚪⚪⚫⚫
    ⚫⚫⚪⚪⚫⚫⚫⚪⚪⚫⚫⚫⚪⚪⚫⚪⚪⚫⚪⚪⚪⚪⚫⚫⚪⚪⚫⚫
    ⚫⚫⚪⚪⚫⚫⚫⚪⚪⚪⚪⚫⚪⚪⚫⚪⚪⚫⚪⚪⚫⚪⚪⚫⚪⚪⚫⚫
    ⚫⚫⚪⚪⚫⚫⚫⚪⚪⚪⚪⚫⚪⚪⚫⚪⚪⚫⚪⚪⚫⚪⚪⚫⚪⚪⚫⚫
    ⚫⚫⚪⚪⚫⚫⚫⚪⚪⚫⚫⚫⚪⚪⚫⚪⚪⚫⚪⚪⚫⚫⚪⚪⚪⚪⚫⚫
    ⚫⚫⚪⚪⚪⚪⚫⚪⚪⚪⚪⚫⚪⚪⚫⚪⚪⚫⚪⚪⚫⚫⚫⚪⚪⚪⚫⚫
    ⚫⚫⚪⚪⚪⚪⚫⚪⚪⚪⚪⚫⚫⚪⚪⚪⚫⚫⚪⚪⚫⚫⚫⚪⚪⚪⚫⚫
    """
    print(aldo_leon_art)
# NameID()

def Hangman():
    word_list = ['apple', 'banana', 'orange', 'grape', 'cherry', 'kiwi', 'melon', 'pear', 'peach', 'plum',
                 'dog', 'cat', 'bird', 'fish', 'rabbit', 'turtle', 'hamster', 'horse', 'cow', 'sheep',
                 'house', 'car', 'tree', 'flower', 'sun', 'moon', 'star', 'cloud', 'rain', 'snow',
                 'happy', 'sad', 'angry', 'excited', 'tired', 'hungry', 'thirsty', 'hot', 'cold', 'fast',
                 'slow', 'big', 'small', 'old', 'new', 'good', 'bad', 'friend', 'family', 'love']

    chosen_word = random.choice(word_list)
    word_length = len(chosen_word)

    end_of_game = False
    lives = 6

    display = ["_" for _ in range(word_length)]

    while not end_of_game:
        guess = input("Guess a letter: ").lower()

        if guess in display:
            print(f"You've already guessed {guess}")

        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter

        if guess not in chosen_word:
            print(f"You guessed {guess}, that's not in the word. You lose a life.")
        
            lives -= 1
            if lives == 0:
                end_of_game = True
                print("You lose.")

        print(f"{' '.join(display)}")

        if "_" not in display:
            end_of_game = True
            print("You win.")

# Hangman()
            
def caesar_cipher(start_text, shift_amount, cipher_direction):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1

    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + shift_amount) % 26
            end_text += alphabet[new_position]
        else:
            end_text += char

    print(f"Here's the {cipher_direction}d result: {end_text}")

def start():
    should_end = False

    while not should_end:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))

        shift = shift % 26

        caesar_cipher(start_text=text, shift_amount=shift, cipher_direction=direction)

        restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
        if restart == "no":
            should_end = True
            print("Goodbye")
# start()
def t_leon():
    import turtle as turtle_module
    import random

    turtle_module.colormode(255)
    leo = turtle_module.Turtle()
    leo.speed("fastest")
    leo.penup()
    leo.hideturtle()
    color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]
    leo.setheading(225)
    leo.forward(300)
    leo.setheading(0)
    number_of_dots = 100

    for dot_count in range(1, number_of_dots + 1):
        leo.dot(20, random.choice(color_list))
        leo.forward(50)

        if dot_count % 10 == 0:
            leo.setheading(80)
            leo.forward(50)
            leo.setheading(180)
            leo.forward(500)
            leo.setheading(0)
    screen = turtle_module.Screen()
    screen.exitonclick()

from tkinter import *
def miles():


    def button_clicked():
        print("I got clicked")
        new_text = input.get()
        my_label.config(text=new_text)


    window = Tk()
    window.title("My First GUI Program")
    window.minsize(width=500, height=300)
    window.config(padx=100, pady=200)

    #Label
    my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
    my_label.config(text="New Text")
    my_label.grid(column=0, row=0)
    my_label.config(padx=50, pady=50)

    #Button
    button = Button(text="Click Me", command=button_clicked)
    button.grid(column=1, row=1)

    new_button = Button(text="New Button")
    new_button.grid(column=2, row=0)

    #Entry
    input = Entry(width=10)
    print(input.get())
    input.grid(column=3, row=2)









    window.mainloop()

# miles()s