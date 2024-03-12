from django.core.exceptions import ValidationError


def no_numbers_validator(value):
    if not value.isalpha():
        raise ValidationError(
            ("Число не должно использоваться в имени")
        )
