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
