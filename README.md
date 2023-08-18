# Dice-Rolling-Simulator
Dice Rolling Simulator: Simulate rolling a dice, and have the computer generate a random number between 1 and 6. The player can keep rolling until they choose to stop.

Here's a README.md file that you can use for your FastAPI Dice Rolling Simulator project:

```markdown
# FastAPI Dice Rolling Simulator

Welcome to the FastAPI Dice Rolling Simulator! This project provides a web API for simulating rolling a dice and generating random numbers between 1 and 6.

## How to Run

1. Clone this repository to your local machine.

2. Install the required dependencies using the following command:
   ```
   pip install -r requirements.txt
   ```

3. Run the FastAPI application using Uvicorn:
   ```
   uvicorn main:app --reload
   ```

4. Open a web browser or use an API client (e.g., curl, Postman) to access the Dice Rolling Simulator API at `http://localhost:8000`.

## API Endpoints

- **GET `/`**: Returns a welcome message.

- **GET `/roll`**: Simulate rolling the dice and get the result.

## Usage

1. Access the welcome message by visiting the root URL: `http://localhost:8000/`.

2. Roll the dice by making a GET request to `http://localhost:8000/roll`.

3. The API will respond with a result indicating the outcome of the dice roll.

## Dependencies

- [FastAPI](https://fastapi.tiangolo.com/): A modern, fast, web framework for building APIs with Python.
- [Uvicorn](https://www.uvicorn.org/): An ASGI server that serves FastAPI applications.

## Docker Support

You can also run the Dice Rolling Simulator in a Docker container. See the `Dockerfile` for instructions on how to build and run the container.

Feel free to customize and extend the simulator as you like. Enjoy rolling the virtual dice!
```
