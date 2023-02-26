# Fibonacci WebSocket Server and Client

This project consists of a server-side script that generates Fibonacci numbers in a given range and a client-side GUI application that allows the user to input a range and receive the corresponding Fibonacci numbers via a WebSocket connection.

## Requirements

- Python 3.7 or higher
- PyQt5==5.14.2
- PyQt5-sip==12.7.2
- websockets==10.4

## Installation

1. Clone the repository: 
  ```
  git clone https://github.com/rishabh-kukreja/fibonacci-websocket.git
  ```
2. Open a terminal window and navigate to the project directory.
3. Create a new virtual environment: 
  ```
  python -m venv env 
  ```
4. Activate the virtual environment: 
  ```
  # Linus/Unix
  source env/bin/activate

  # Windows
  env\Scripts\activate 
  ```
5. Install the required packages: 
 
  ```
  pip install -r requirements.txt
  ```

## Usage

1. Start the WebSocket server by running the following command in terminal in the virtual environment: 
  ```
  python server.py
  ```
2. For client, In a separate terminal window navigate to project directory, activate the virtual environment to run the client as well
  ```
  # Linux/MacOS
  source env/bin/activate 
  
  # Windows
  env\Scripts\activate 
  ```
3. Start the Fibonacci client by running the following command: 
  ```
  python client.py
  ```
4. Enter the start and end values for the range of Fibonacci numbers you want to generate and click the "Submit" button.
5. The Fibonacci numbers will be displayed in the text box below the button.

## Images
##### Valid Input
![Valid Input](https://github.com/rishabh-kukreja/fibonacci-websocket/blob/main/imgs/fibonacci-valid-input.png)

##### Invalid Input
![Invalid Input](https://github.com/rishabh-kukreja/fibonacci-websocket/blob/main/imgs/fibonacci-invalid-input.png)

