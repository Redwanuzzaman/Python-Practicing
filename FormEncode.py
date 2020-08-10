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
