Force Admin Middleware
=========================

Force Django Admin to show in one selected language

Installation
------------

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
