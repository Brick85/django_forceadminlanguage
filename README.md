Force Admin Language Middleware
===============================

Force Django Admin to show in one selected language.

Installation
------------

```bash
pip install django-forceadminlanguage
```

or

```bash
pip install git+git://github.com/Brick85/django_forceadminlanguage.git
```



Usage
-----

```python
MIDDLEWARE_CLASSES = (
    ...
    'forceadminlanguage.middleware.ForceAdminLanguageMiddleware',
    ...
)
ADMIN_LANGUAGE_CODE = 'en'
```

Additional Settings
-------------------

ADMIN_LANGUAGE_IGNORE_PATH
^^^^^^^^^^^^^^^^^^^^^^^^^^

If requests starts with this path admin language shouldn't be forced. Example:

```python

# won't force English if French is manually requested.
ADMIN_LANGUAGE_IGNORE_PATH = '/fr/'
```