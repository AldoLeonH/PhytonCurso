# def colgado():
#     import random

#     word_list = ["dog", "continental", "camell"]
#     chosen_word = random.choice(word_list)
#     blanks = ["_"] * len(chosen_word)
#     print(blanks)

#     while "_" in blanks:
#         guess = input("Guess a letter: ").lower()
#         correct_guess = False

#         for i in range(len(chosen_word)):
#             if chosen_word[i] == guess:
#                 blanks[i] = guess
#                 correct_guess = True

#         if not correct_guess:
#             print("Try Again")

#         print(blanks)

#     print("You won")

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
NameID()

def greetings():
    name=input("Hola, ¿cuál es tu nombre? ")
    lastname=input("Y qué tal tu apellido? ")
    codification(name,lastname)

def codification():
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    action=input("Type 'A' to encode and type 'B' to decode: ")
    message=input("Type your message: ")
    shift_number=int(input("Type the shift number"))
    end_text=""
    print(f"The messagethat is goint to be encipted is '{message}'")
    if action== "A":
        shift_number*=-1
        for letter in message:
            position= alphabet.index(letter)
            new_position = position + shift_number
            end_text += alphabet[new_position]
        print(f"Here's the {action}d result: {end_text}")

def calculator():
    def add(n1,n2):
        return n1+n2
    def substract(n1,n2):
        return n1-n2
    def multiply(n1,n2):
        return n1*n2
    def divide(n1,n2):
        return n1/n2
    operators={"+":add,
               "-":substract,
               "*":multiply,
               "/":divide}
    n1 = int(input("What's the first number?: "))
    n2 = int(input("What's the second number?: "))
    for op in operators:
        print(op)
    operation_symbol=input("Pick an operation from the list above: ")
    calculation=operators[operation_symbol]
    print(calculation (n1,n2))
def higherOrLower():
    import random
    num=0
    won=1
    high_score=0
    while won==1:
        new_num= random.randint(1,99)
        new_num2= random.randint(1,99)
        print(new_num,new_num2)
        print(f"Is {new_num} higher or lower? than the second number")
        response=input()
        if response=="higher" and new_num>new_num2:
            print("You're right! keep going...")
            high_score=high_score+1

        elif response=="higher" and new_num<new_num2:
            won=0
            print(f"Sorry your high score was {high_score}")
        elif response=="lower" and new_num<new_num2:
            print("You're right! keep going...")
            high_score=high_score+1
        elif response=="lower" and new_num>new_num2:
            won=0
            print(f"Sorry your high score was {high_score}")
def OOP():
    # import turtle
    # timmy=turtle.Turle()
    # Or
    from turtle import Turtle
    timmy=Turtle()
    print(timmy)

OOP()
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
           all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        print_board(board)
        row = int(input(f"Player {current_player}, enter row (0, 1, or 2): "))
        col = int(input(f"Player {current_player}, enter column (0, 1, or 2): "))

        if board[row][col] == ' ':
            board[row][col] = current_player
            if check_winner(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                break
            elif is_board_full(board):
                print_board(board)
                print("It's a tie!")
                break
            else:
                current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("Cell already taken. Try again.")

if __name__ == "__main__":
    tic_tac_toe()
import turtle

# Set up the screen
wn = turtle.Screen()
wn.title("Breakout")
wn.bgcolor("black")
wn.setup(width=600, height=600)

# Create the paddle
paddle = turtle.Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -250)

# Create the ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = -2

# Create bricks
bricks = []

def create_bricks():
    for i in range(-150, 200, 50):
        for j in range(100, 250, 25):
            brick = turtle.Turtle()
            brick.shape("square")
            brick.color("white")
            brick.penup()
            brick.goto(i, j)
            bricks.append(brick)

create_bricks()

# Move the paddle left
def paddle_left():
    x = paddle.xcor()
    x -= 20
    if x < -290:
        x = -290
    paddle.setx(x)

# Move the paddle right
def paddle_right():
    x = paddle.xcor()
    x += 20
    if x > 290:
        x = 290
    paddle.setx(x)

# Keyboard bindings
wn.listen()
wn.onkey(paddle_left, "Left")
wn.onkey(paddle_right, "Right")

# Main game loop
while True:
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.xcor() > 290 or ball.xcor() < -290:
        ball.dx *= -1

    if ball.ycor() > 290:
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.goto(0, 0)
        ball.dy *= -1

    # Paddle and ball collisions
    if (ball.ycor() > -240) and (ball.ycor() < -230) and (paddle.xcor() + 50 > ball.xcor() > paddle.xcor() - 50):
        ball.dy *= -1

    # Brick collisions
    for brick in bricks:
        if (brick.distance(ball) < 20):
            brick.goto(1000, 1000)  # Move the brick out of the screen
            ball.dy *= -1

    wn.update()
