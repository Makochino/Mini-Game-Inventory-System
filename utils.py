def get_input(prompt, cast_func, error_msg):
    while True:
        try:
            return cast_func(input(prompt))
        except ValueError:
            print(error_msg)

def get_text(prompt, error_msg):
    while True:
        value = input(prompt).strip()

        if not value:
            print("Input cannot be empty")
        elif value.isdigit():
            print(error_msg)
        else:
            return value