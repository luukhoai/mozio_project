from django.core.validators import RegexValidator


def phone_regex():
    return RegexValidator(
        regex=r'^[\+]{1}\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'")
