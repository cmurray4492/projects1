"""Type Annotation Note"""
# Python does not care abput type annoations

# Basic Type Annotations
text: str = 'hello'
number: int = 10
percent: float = 0.50
connected: bool = False


def format_input(user_input: str):
    '''Prints user input with first letter capitalized'''
    print(user_input.capitalize())


format_input('hello world')
