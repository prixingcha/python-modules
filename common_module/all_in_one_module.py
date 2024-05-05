import sys
from rich.console import Console
from  rich import print
import os 

from new_model_123.variables import temp
from llm_selector_package.llm_selector import *
#LLMSelector, model_choices #, print # type: ignore
from llm_selector_package.model_setup import ModelConfigurator # type: ignore



print(os.environ.get("OPENAI_API_KEY"))


import os
os.environ.clear()

print('after')
print(os.environ.get("OPENAI_API_KEY"))

exit()
print(model_choices)
selector = LLMSelector(model_choices)
return_val = selector.run()
print(return_val)
configurator = ModelConfigurator(return_val)
configurator.configure()
print('this is just for test')



print("all_in_one_module.py")