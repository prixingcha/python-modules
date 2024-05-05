import sys
from rich.console import Console
from  rich import print
import os 
from new_model_123.variables import temp
from llm_selector_package.llm_selector import *
from llm_selector_package.model_setup import ModelConfigurator # type: ignore

print(os.environ.get("OPENAI_API_KEY"))
print(model_choices)
selector = LLMSelector(model_choices)

return_val = selector.run()

print(return_val)
print("before")
x = os.environ.get("GROQ_API_KEY")

print(os.environ.get("OPENAI_API_KEY"))

configurator = ModelConfigurator(return_val)
configurator.configure()

print("afteR")
x = os.environ.get("GROQ_API_KEY")
