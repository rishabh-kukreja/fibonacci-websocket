import asyncio
import websockets
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit

class FibonacciClient(QWidget):
    def __init__(self):
        super().__init__()

        # Set window properties
        self.setWindowTitle("Fibonacci Client")
        self.resize(500, 300)

        # Create UI elements
        self.start_label = QLabel("Start:")
        self.start_input = QLineEdit()
        self.end_label = QLabel("End:")
        self.end_input = QLineEdit()
        self.submit_button = QPushButton("Submit")
        self.result_text = QTextEdit()
        self.error_label = QLabel()

        # Create layouts and add elements to them
        input_layout = QHBoxLayout()
        input_layout.addWidget(self.start_label)
        input_layout.addWidget(self.start_input)
        input_layout.addWidget(self.end_label)
        input_layout.addWidget(self.end_input)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.submit_button)

        main_layout = QVBoxLayout()
        main_layout.addLayout(input_layout)
        main_layout.addLayout(button_layout)
        main_layout.addWidget(self.result_text)
        main_layout.addWidget(self.error_label)

        self.setLayout(main_layout)

        # Connect event handlers
        self.submit_button.clicked.connect(self.submit)

        # Initialize event loop
        self.loop = asyncio.get_event_loop()

    def submit(self):
        # Clear any previous errors
        self.clear_errors()

        # Get user input
        start = self.start_input.text()
        end = self.end_input.text()

        # Call get_fibonacci coroutine with user input
        asyncio.run(self.get_fibonacci(start, end))

    async def get_fibonacci(self, start, end):
        async with websockets.connect("ws://localhost:8765") as websocket:
            try:
                # Send user input to server
                await websocket.send(f"{start},{end}")

                # Receive response from server
                response = await websocket.recv()

                # If response is "OK", start receiving Fibonacci numbers
                if response == "OK":
                    self.result_text.clear()  # Clear previous results
                    async for number in websocket:
                        self.result_text.append(str(number))
                        if int(number) >= int(end):
                            break
                else:
                    # If response is not "OK", raise an exception with the error message
                    raise Exception(response)
            except Exception as e:
                # If there is an exception, display the error message in the result text box
                self.result_text.clear()
                self.result_text.append(f"{str(e)}")

    def clear_errors(self):
        # Clear any previous error messages from the error label
        self.error_label.clear()

if __name__ == '__main__':
    # Create the application and window objects and run the event loop
    app = QApplication([])
    window = FibonacciClient()
    window.show()
    app.exec_()
