from llm_selector_package.llm_selector import *
from llm_selector_package.model_setup import ModelConfigurator # type: ignore
from rich.console import Console
import os 
import sys
import json
from rich import print

# selector = LLMSelector(model_choices)
# return_val = selector.run()
# configurator = ModelConfigurator(return_val)
# configurator.configure()