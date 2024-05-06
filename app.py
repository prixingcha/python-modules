from llm_selector_package.llm_selector import *
from llm_selector_package.model_setup import ModelConfigurator # type: ignore

print(model_choices)
selector = LLMSelector(model_choices)
return_val = selector.run()
print(return_val)
configurator = ModelConfigurator(return_val)
configurator.configure()
print('this is just for test')



import json

# Sample data
sample_data = {
    "name": "John Doe",
    "age": 30,
    "city": "New York",
    "email": "john@example.com",
    "is_active": True
}

# Convert data to JSON format
json_data = json.dumps(sample_data, indent=4)

# Print the JSON data
print(json_data)