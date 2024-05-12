from groq import Groq
import os
import json
import importlib.util
from rich import print

error_val = "" 
class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ModuleNotFoundError):
            return str(obj)
        return super().default(obj)

tools = [
            {
                "type": "function",
                "function": {
                    "name": "check_package",
                    "description": "Check if the given python package is installed for the given package name",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "package_name": {
                                "type": "string",
                                "description": "The name of the python package (e.g. 'openai')",
                            }
                        },
                        "required": ["package_name"],
                    },
                },
            },
            {
                "type": "function",
                "function": {
                    "name": "check_env_variable",
                    "description": "Check if the given environment variable exists",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "variable_name": {
                                "type": "string",
                                "description": "The name of the environment variable (e.g 'OPENAI_API_KEY')",
                            }
                        },
                        "required": ["variable_name"],
                    },
                },
            },
        ]

# try:
#     val = 1/0
# except Exception as ex:
#     error_val = json.dumps({"error": str(ex)}, cls=CustomEncoder) 

class ConversationManager:
    def __init__(self, api_key, model_name):
        self.client = Groq(api_key=api_key)
        self.MODEL = model_name # "llama3-70b-8192"

    # @classmethod
    def check_package(self, package_name):
        spec = importlib.util.find_spec(package_name)
        if spec is None:
            return json.dumps(
                {
                    "python_package_page": package_name,
                    "is_package_installed": "not installed",
                    "version": None,
                }
            )
        else:
            return json.dumps(
                {
                    "python_package_page": package_name,
                    "is_package_installed": "installed",
                    "version": getattr(importlib.import_module(package_name), '__version__', None),
                }
            )

    # @classmethod
    def check_env_variable(self, variable_name):
        if variable_name in os.environ:
            return json.dumps(
                {
                    "variable_name": variable_name,
                    "is_available": "Yes",
                    "value": os.environ.get(variable_name)
                }
            )
        else:
            return json.dumps(
                {
                    "variable_name": variable_name,
                    "is_available": "No",
                    "value": None
                }
            )

    def run_conversation(self, user_prompt):
        messages = [
            {
                "role": "system",
                "content": "You are a function calling LLM that uses the data extracted from the check_package or check_env_variable function to answer questions, if the function are not relevant then just say , \"I  do not know\" ",
            },
            {
                "role": "user",
                "content": user_prompt,
            },
        ]

        
        response = self.client.chat.completions.create(
            model=self.MODEL,
            messages=messages,
            tools=tools,
            tool_choice="auto",
            max_tokens=4096,
        )

        response_message = response.choices[0].message
        tool_calls = response_message.tool_calls

        if tool_calls:
            available_functions = {
                "check_package": self.check_package,
                "check_env_variable": self.check_env_variable,
            }

            messages.append(response_message)
            for tool_call in tool_calls:
                function_name = tool_call.function.name
                function_to_call = available_functions[function_name]
                function_args = json.loads(tool_call.function.arguments)
                
                print(f"function_name {function_name}(), Arguments: {tool_call.function.arguments}")
                
                if function_name == "check_package":
                    function_response = function_to_call(
                        package_name=function_args.get("package_name")
                    )
                elif function_name == "check_env_variable":
                    function_response = function_to_call(
                        variable_name=function_args.get("variable_name")
                    )

                messages.append(
                    {
                        "tool_call_id": tool_call.id,
                        "role": "tool",
                        "name": function_name,
                        "content": function_response,
                    }
                )
            second_response = self.client.chat.completions.create(model=self.MODEL, messages=messages)
            return second_response.choices[0].message.content