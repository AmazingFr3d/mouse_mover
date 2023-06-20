import pyautogui
import random
import threading
import PySimpleGUI as sg


class MouseMoverGUI:
    def __init__(self):
        self.is_running = False
        self.window = None

    def move_mouse_randomly(self):
        while self.is_running:
            # Generate random coordinates within the screen boundaries
            x = random.randint(0, pyautogui.size().width)
            y = random.randint(0, pyautogui.size().height)

            # Move the mouse cursor to the random coordinates
            pyautogui.moveTo(x, y, duration=0.5)

            # Pause for 5 seconds before moving again
            pyautogui.PAUSE = 15

    def start_mouse_movement(self):
        self.is_running = True

        # Start a new thread to handle mouse movement
        threading.Thread(target=self.move_mouse_randomly).start()

    def stop_mouse_movement(self):
        self.is_running = False

    def create_gui(self):
        layout = [
            [sg.Button('Start', key='-START-', pad=((10, 10), (10, 10)), size=(15, 2)),
             sg.Button('Stop', key='-STOP-', pad=((10, 10), (10, 10)), size=(15, 2), disabled=True)]
        ]

        self.window = sg.Window('Mouse Mover v1.0', layout)

        while True:
            event, _ = self.window.read()

            if event == sg.WINDOW_CLOSED:
                break
            elif event == '-START-':
                self.start_mouse_movement()
                self.window['-START-'].update(disabled=True)
                self.window['-STOP-'].update(disabled=False)
            elif event == '-STOP-':
                self.stop_mouse_movement()
                self.window['-START-'].update(disabled=False)
                self.window['-STOP-'].update(disabled=True)

        self.window.close()


# Create an instance of the MouseMoverGUI class
gui = MouseMoverGUI()

# Create the GUI
gui.create_gui()
