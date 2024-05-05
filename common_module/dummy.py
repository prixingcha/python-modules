import os

def clear_screen():
    os.system('clear')

clear_screen()

# Get all environment variables as a dictionary
env_vars = os.environ

# Convert dictionary to a list of tuples (key, value)
env_vars_list = list(env_vars.items())

print(env_vars_list[0])
