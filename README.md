# django-hibp

This package provides a password validator for Django that validates passwords against [HIBP](https://haveibeenpwned.com/Passwords).

*django-hibp* has no dependencies other than Django and the Python standard library. All code is included in `django_hibp.py` and can be examined by the user. If anything is unclear, feel free to create an issue and I'll try to explain.

## Installation

*django-hibp* is available on [PyPi](https://pypi.org/project/django-hibp/):

```
pip install django-hibp
```

## Usage

Add `HIBPPasswordValidator` to your `AUTH_PASSWORD_VALIDATORS` settings:

```python
AUTH_PASSWORD_VALIDATORS = [
    ...
    {
        'NAME': 'django_hibp.HIBPPasswordValidator',
        'OPTIONS': {
            'fail_on_error': False,
        }
    },
]
```

Since this plugin relies on an external API, this introduces a new point of failure. If the Pwned Passwords API is inaccessible, the check will fail. To avoid breaking your application in this case, set `fail_on_error` to `False`.

## Privacy

Because of the way the HIBP API works, your password is not exposed during validation. Rather than reiterate everything, I will refer you to the [original API documentation](https://haveibeenpwned.com/API/v3#SearchingPwnedPasswordsByRange), but feel free to create an issue if anything is unclear or bothers you.
