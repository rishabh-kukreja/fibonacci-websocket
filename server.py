import asyncio
import websockets

# Function to generate fibonacci numbers in a given range
async def fibonacci(start, end):
    a, b = 0, 1
    while a < end:
        if a >= start:
            yield a
        a, b = b, a+b

# Websocket handler function to process incoming requests and send responses
async def handler(websocket, path):
    try:
        # Receive message from client
        msg = await websocket.recv()
        # Extract start and end values from message
        try:
            start, end = msg.split(",")
            start = int(start)
            end = int(end)
        except ValueError:
            raise ValueError("START and END must be valid integer values")
        # Validate start and end values
        if start < 0 or end < 0:
            raise ValueError("START and END must be positive integers")
        elif start >= end:
            raise ValueError("START must be less than END")
        print(f"Received start={start} end={end}")
        # Send "OK" response to client
        await websocket.send("OK")
        # Generate fibonacci numbers and send them to client
        async for number in fibonacci(start, end + 1):
            await websocket.send(str(number))
    except Exception as e:
        # Handle errors by sending an error message to the client
        print(f"Error: {str(e)}")
        await websocket.send(f"Error: {str(e)}")

# Main function to start the websocket server
async def main():
    try:
        # Start the websocket server
        async with websockets.serve(handler, "localhost", 8765):
            await asyncio.Future()  # run forever
    except Exception as e:
        print(f"Error: {str(e)}")

# Run the main function to start the websocket server
asyncio.run(main())
