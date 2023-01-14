"""
Displaying yes/no input.

Args:
    text - text to display when asking
    default - [None, True, False] - Default value
        None - No default value
        True - Default value is "Yes"
        False - Default value is "No"

Returns:
    bool - Answer in bool format
"""
def yes_no_input(text: str, default: bool = None) -> bool:
    while True:
        answer = input(text)
        if len(answer) == 0 and default is not None:
            return default
        if answer.lower() in ["yes", "y"]:
            return True
        elif answer.lower() in ["no", "n"]:
            return False
        else:
            print("Specify correct option!")

