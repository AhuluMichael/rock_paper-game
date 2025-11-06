import random
import time

print("🚀 Welcome to Rocket vs Paper!")
print("Avoid the falling papers by choosing the right move!")
print("Controls: type 'left', 'right', or 'stay'")

score = 0
positions = ["left", "center", "right"]
rocket_pos = "center"

while True:
    paper_pos = random.choice(positions)
    print(f"\nPaper is falling at: {paper_pos}")
    move = input("Move your rocket (left/right/stay): ").strip().lower()

    if move == "left":
        rocket_pos = "left"
    elif move == "right":
        rocket_pos = "right"
    elif move == "stay":
        rocket_pos = rocket_pos
    else:
        print("Invalid move! You stay where you are.")

    if rocket_pos == paper_pos:
        print("💥 Game Over! You got hit by paper!")
        print(f"Your final score: {score}")
        break
    else:
        score += 1
        print(f"✅ Safe! Current score: {score}")
        time.sleep(1)