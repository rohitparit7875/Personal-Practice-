import tkinter as tk
import random

# Game Config
WIDTH = 500
HEIGHT = 500
CELL_SIZE = 20

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("🐍 Snake Game")
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
        self.canvas.pack()

        self.snake = [(100, 100), (80, 100), (60, 100)]
        self.direction = "Right"
        self.food = None
        self.score = 0

        self.root.bind("<Key>", self.change_direction)
        self.place_food()
        self.update_game()

    def place_food(self):
        while True:
            x = random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
            y = random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
            if (x, y) not in self.snake:
                self.food = (x, y)
                break

    def change_direction(self, event):
        if event.keysym in ["Up", "Down", "Left", "Right"]:
            # Prevent snake from reversing
            if (event.keysym == "Up" and self.direction != "Down") or \
               (event.keysym == "Down" and self.direction != "Up") or \
               (event.keysym == "Left" and self.direction != "Right") or \
               (event.keysym == "Right" and self.direction != "Left"):
                self.direction = event.keysym

    def update_game(self):
        head_x, head_y = self.snake[0]
        if self.direction == "Up":
            head_y -= CELL_SIZE
        elif self.direction == "Down":
            head_y += CELL_SIZE
        elif self.direction == "Left":
            head_x -= CELL_SIZE
        elif self.direction == "Right":
            head_x += CELL_SIZE

        new_head = (head_x, head_y)

        # Check collisions
        if (head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT or new_head in self.snake):
            self.game_over()
            return

        self.snake = [new_head] + self.snake

        # Check if food eaten
        if new_head == self.food:
            self.score += 1
            self.place_food()
        else:
            self.snake.pop()

        self.draw_game()
        self.root.after(100, self.update_game)  # game speed

    def draw_game(self):
        self.canvas.delete("all")
        # Draw snake
        for x, y in self.snake:
            self.canvas.create_rectangle(x, y, x+CELL_SIZE, y+CELL_SIZE, fill="green")
        # Draw food
        fx, fy = self.food
        self.canvas.create_rectangle(fx, fy, fx+CELL_SIZE, fy+CELL_SIZE, fill="red")
        # Draw score
        self.canvas.create_text(50, 10, fill="white", text=f"Score: {self.score}", anchor="nw", font=("Arial", 14))

    def game_over(self):
        self.canvas.delete("all")
        self.canvas.create_text(WIDTH/2, HEIGHT/2, text="GAME OVER", fill="red", font=("Arial", 30))
        self.canvas.create_text(WIDTH/2, HEIGHT/2 + 40, text=f"Final Score: {self.score}", fill="white", font=("Arial", 20))

# Run the game
root = tk.Tk()
game = SnakeGame(root)
root.mainloop()
