from django.conf import settings
from django.utils import translation
from django.core.urlresolvers import reverse


class ForceAdminLanguageMiddleware:

    def process_request(self, request):
        if request.path.startswith(reverse('admin:index')):
            request.LANGUAGE_CODE = getattr(settings, 'ADMIN_LANGUAGE_CODE', settings.LANGUAGE_CODE)
            translation.activate(request.LANGUAGE_CODE)
            request.LANG = request.LANGUAGE_CODE
