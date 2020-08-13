"""
FormEncode is a validation and form generation package. 
The validation can be used separately from the form generation. 
The validation works on compound data structures, with all parts being nestable. 
It is separate from HTTP or any other input mechanism.
"""


import formencode
from formencode import validators

def is_valid(prompt, validator):
    while True:
        try:
            value = input(prompt)
            return validator.to_python(value)
        except formencode.Invalid as e:
            print(e)


is_valid('Email Address: ', validators.Email())
