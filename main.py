"""
Menu for users interface
"""

from prompt_toolkit import prompt


answer = prompt('Give me some input: ')
print('You said: %s' % answer)
