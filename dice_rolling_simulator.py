import random
from fastapi import FastAPI

app = FastAPI()

def roll_dice():
    """
    Simulate rolling a dice and generate a random number between 1 and 6.

    Returns:
        int: Randomly generated number representing the dice roll.
    """
    return random.randint(1, 6)

@app.get("/")
def read_root():
    """
    Root endpoint that returns a welcome message.

    Returns:
        dict: Welcome message.
    """
    return {"message": "Welcome to the Dice Rolling Simulator API!"}

@app.get("/roll")
def roll():
    """
    Simulate rolling the dice.

    Returns:
        dict: Result of the dice roll.
    """
    dice_roll = roll_dice()
    return {"result": f"You rolled a {dice_roll}!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
