import json
from django import forms
from django.conf import settings
from django.template.loader import render_to_string
try:
    from django.utils.encoding import force_unicode
except ImportError:
    from django.utils.encoding import force_str as force_unicode

from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe
try:
    from django.core.urlresolvers import reverse
except ImportError:
    from django.urls import reverse

from django.core.exceptions import ImproperlyConfigured
from django.forms.utils import flatatt
from cked import default_settings


class CKEditorWidget(forms.Textarea):
    """
Widget providing CKEditor for Rich Text Editing.
"""
    class Media:
        js = (settings.STATIC_URL + 'cked/ckeditor/ckeditor.js',)

    def __init__(self, *args, **kwargs):
        config_name = kwargs.pop('config_name', 'default')
        super(CKEditorWidget, self).__init__(*args, **kwargs)
        # Use default config
        self.options = default_settings.CKEDITOR_DEFAULT_OPTIONS.copy()

        # If CKEDITOR_OPTIONS presented in settings, use it!
        general_options = getattr(settings, 'CKEDITOR_OPTIONS', {})
        if general_options is None:
            general_options = {}

        if config_name in general_options:
            options = general_options[config_name]
        else:
            options = None

        if options is not None:
            if isinstance(options, dict):
                # Override defaults with CKEDITOR_OPTIONS.
                self.options.update(options)
            else:
                raise ImproperlyConfigured('CKEDITOR_OPTIONS setting must be'
                                           ' a dictionary type.')

    def render(self, name, value, attrs={}):
        if value is None:
            value = ''

        final_attrs = self.build_attrs(self.attrs, attrs, name=name)

        self.options['filebrowserBrowseUrl'] = reverse('cked_elfinder')

        return mark_safe(render_to_string('cked/ckeditor.html', {
            'final_attrs': flatatt(final_attrs),
            'value': conditional_escape(force_unicode(value)),
            'id': final_attrs['id'],
            'options': json.dumps(self.options)})
        )

    def build_attrs(self, base_attrs, extra_attrs=None, **kwargs):
        """
        Helper function for building an attribute dictionary.
        This is combination of the same method from Django<=1.10 and Django1.11+
        """
        attrs = dict(base_attrs, **kwargs)
        if extra_attrs:
            attrs.update(extra_attrs)
        return attrs

