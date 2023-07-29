"""This project - madlibs"""


def get_input(word_type: str):
    """Get user input for the story"""
    user_input: str = input(f"Enter a {word_type}: ")
    return user_input


noun1 = get_input("noun")
verb1 = get_input("verb")
noun2 = get_input("noun")
verb2 = get_input("verb")

story = f"""
Once upon a time, there was a {noun1} who loved to {verb1} all day.

This noun2, {noun2}, and verb2, {verb2}.
"""

print(story)
