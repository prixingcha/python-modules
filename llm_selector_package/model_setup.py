import os
from openai import OpenAI
from rich import print

class ModelConfigurator:
    _instance = None
    all_env = {}  # new public variable
    client = None

    def __new__(cls, model_choice):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, model_choice):
        if not hasattr(self, "model_choice"):
            self.model_choice = model_choice

    def configure(self):
        if not os.environ.get("OPENAI_API_KEY"):
            print("OPENAI_API_KEY is not set!!")
            return

        env_vars_dict = dict(os.environ)

        try:
            if self.model_choice == "GROQ":
                os.environ["OPENAI_API_BASE"] = env_vars_dict.get("GROQ_API_BASE")
                os.environ["OPENAI_MODEL_NAME"] = env_vars_dict.get("GROQ_MODEL_NAME")
                os.environ["OPENAI_API_KEY"] = env_vars_dict.get("GROQ_API_KEY")
            
            elif self.model_choice == "gpt-3.5-turbo-1106":
                print("no changes just run $ renv !!!")
            elif self.model_choice == "gpt-4.0":
                print("")
            elif self.model_choice == "mistral":
                os.environ["OPENAI_API_BASE"] = env_vars_dict.get("OLLAMA_BASE_URL")
                os.environ["OPENAI_MODEL_NAME"] = env_vars_dict.get("OLLAMA_MISTRAL_MODEL_NAME")
                os.environ["OPENAI_API_KEY"] = env_vars_dict.get("OLLAMA_API_KEY")
            elif self.model_choice == "LM Studio":
                os.environ["OPENAI_API_BASE"] = env_vars_dict.get("LMSTUDIO_BASE_URL")
                os.environ["OPENAI_MODEL_NAME"] = env_vars_dict.get("LMSTUDIO_MODEL_NAME")
                os.environ["OPENAI_API_KEY"] = env_vars_dict.get("LMSTUDIO_API_KEY")
                print("right away output") 
                print(
                f"""
                model chose : {self.model_choice}
                OPENAI_MODEL_NAME: {os.environ["LMSTUDIO_MODEL_NAME"]},
                OPENAI_API_BASE : {os.environ["LMSTUDIO_BASE_URL"]},
                OPENAI_API_KEY : {os.environ["LMSTUDIO_API_KEY"]}"""
            )
            else:
                os.environ["OPENAI_API_BASE"] = env_vars_dict.get("OLLAMA_BASE_URL")
                os.environ["OPENAI_MODEL_NAME"] = env_vars_dict.get("OLLAMA_LLAMA_MODEL_NAME")
                os.environ["OPENAI_API_KEY"] = env_vars_dict.get("OLLAMA_API_KEY")

            self.all_env = dict(os.environ)

            print(f"=========================================")
            # os.system("clear" if os.name == "posix" else "cls")

            print(
                f"""
                this is at the END of config method:
                model chose : {self.model_choice}
                OPENAI_MODEL_NAME: {os.environ.get("OPENAI_MODEL_NAME")},
                OPENAI_API_BASE : {os.environ.get("OPENAI_API_BASE")},
                OPENAI_API_KEY : {os.environ.get("OPENAI_API_KEY")}"""
            )
            print(f"=========================================")
        except Exception as ex:
            print(f" error occurred here: {ex}")


    def clear_screen(self):
        os.system("clear" if os.name == "posix" else "cls")
        
        
    def check_model_connection(self):
        print("check_model_connection")
        print(
                f"""
                model chose : {self.model_choice}
                OPENAI_MODEL_NAME: {os.environ["OPENAI_MODEL_NAME"]},
                OPENAI_API_BASE : {os.environ["OPENAI_API_BASE"]},
                OPENAI_API_KEY : {os.environ["OPENAI_API_KEY"]}"""
            )

        print(" after at the END: check_model_connection")
        client = OpenAI(base_url=os.environ.get("OPENAI_API_BASE"), api_key=os.environ.get("OPENAI_API_KEY"))

        try:
            response = client.chat.completions.create(
            model=os.environ.get("OPENAI_MODEL_NAME"),
            messages=[
                # {"role": "system", "content": "Always answer in rhymes"},
                {"role": "user", "content": "add 1 and 2!!"},
            ],
            temperature=0.7,
            stream=True
            )
            print("CONNECTED")
            for chunk in response:
                if chunk.choices[0].delta.content is not None:
                    print(chunk.choices[0].delta.content, end="")
        except Exception as ex:
            print(f"NO CONNECTED {ex} !!") 