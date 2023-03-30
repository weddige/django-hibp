# django-hibp

This package provides a password validator for Django that validates passwords against [HIBP](https://haveibeenpwned.com/Passwords).

## Getting started

Install using pip:

```
pip install django-hibp
```

Add `HIBPPasswordValidator` to your `AUTH_PASSWORD_VALIDATORS` setting:

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
