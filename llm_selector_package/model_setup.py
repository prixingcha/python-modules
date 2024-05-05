import os

class ModelConfigurator:
    _instance = None
    def __new__(cls, model_choice):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, model_choice):
        if not hasattr(self, 'model_choice'):
            self.model_choice = model_choice

    def configure(self):
        if self.model_choice == "GROQ":            
            os.environ["OPENAI_API_BASE"] = 'https://api.groq.com/openai/v1'
            os.environ["OPENAI_MODEL_NAME"] = 'llama3-70b-8192'  
            os.environ["OPENAI_API_KEY"] = os.environ.get("GROQ_API_KEY")
        elif self.model_choice == "gpt-3.5-turbo-1106":
            print("no changes just run $ renv")
        elif self.model_choice == "gpt-4.0":
            print("")
        elif self.model_choice == "mistral":
            os.environ["OPENAI_API_BASE"] = 'http://localhost:11434/v1'
            os.environ["OPENAI_MODEL_NAME"] = 'mistral'
            os.environ["OPENAI_API_KEY"] = 'sk-111111111111111111111111111111111111111111111111'
        else:
            os.environ["OPENAI_API_BASE"] = 'http://localhost:11434/v1'
            os.environ["OPENAI_MODEL_NAME"] = 'llama3:8b'
            os.environ["OPENAI_API_KEY"] = 'sk-111111111111111111111111111111111111111111111111'
        print(f"=========================================")
        print(f"""
            model chose : {self.model_choice}
            OPENAI_MODEL_NAME: {os.environ["OPENAI_MODEL_NAME"]},
            OPENAI_API_BASE : {os.environ["OPENAI_API_BASE"]},
            OPENAI_API_KEY : {os.environ["OPENAI_API_KEY"]}""")
        print(f"=========================================")
