import sys
from rich.console import Console
import os

#next put these into as a json data into json or CSV file 
model_choices = {
    "0": "Clear all Environment",
    "1": "GROQ",
    "2": "gpt-3.5-turbo-1106",
    "3": "gpt-4.0",
    "4": "mistral",
    "5": "Other",
    "Q": "QUIT"
}

class LLMSelector:
    def __init__(self, models):
        self.models = models
        self.console = Console()

    def display_models(self):
        self.console.print("Select an LLM model by entering its corresponding number:", style="bold underline")
        for key, value in self.models.items():
            self.console.print(f"[red]{key}[/red]: [green]{value}[/green]")

    def select_model(self):
        while True:
            self.console.print("Enter the number of the LLM model you want to select (press 'q' to quit): ", end='', style="bold")
            selected_key = getch()
            if selected_key.lower() == 'q':
                self.console.print("Exiting the program.")
                sys.exit()
            elif selected_key in self.models:
                self.console.print(f"Selected model: {self.models[selected_key]}")
                return selected_key
            else:
                self.console.print("\nInvalid input. Please enter a valid number corresponding to an LLM model or press 'q' to quit.", style="bold red")

    def run(self):
        self.display_models()
        selected_key = self.select_model()
        if selected_key == '0':
            os.environ.clear()
            os.system('clear')
            self.display_models()
        else:
            selected_model = self.models[selected_key]  # Retrieve the model name using the selected key
            return selected_model  # Return the selected model name

def getch():
    if sys.platform.startswith('win'):
        import msvcrt
        return msvcrt.getch().decode('utf-8')
    else:
        import tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch