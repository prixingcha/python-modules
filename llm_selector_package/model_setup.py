import os

class ModelConfigurator:
    _instance = None

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
            else:
                os.environ["OPENAI_API_BASE"] = env_vars_dict.get("OLLAMA_BASE_URL")
                os.environ["OPENAI_MODEL_NAME"] = env_vars_dict.get("OLLAMA_LLAMA_MODEL_NAME")
                os.environ["OPENAI_API_KEY"] = env_vars_dict.get("OLLAMA_API_KEY")

            print(f"=========================================")

            os.system("clear" if os.name == "posix" else "cls")
            print("yahoooo")

            print(
                f"""
                model chose : {self.model_choice}
                OPENAI_MODEL_NAME: {os.environ["OPENAI_MODEL_NAME"]},
                OPENAI_API_BASE : {os.environ["OPENAI_API_BASE"]},
                OPENAI_API_KEY : {os.environ["OPENAI_API_KEY"]}"""
            )
            print(f"=========================================")
        except Exception as ex:
            print(f" error occurred here: {ex}")