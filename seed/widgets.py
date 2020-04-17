from django import forms
from django.forms import widgets
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from django.contrib.admin.widgets import *


class CountableWidget(widgets.Textarea):
    class Media:
        js = (
            'seed/js/countable.js',
            'seed/js/countable-field.js'
        )

    def render(self, name, value, attrs=None):
        final_attrs = self.build_attrs(self.attrs, attrs)
        final_attrs['data-count'] = 'words'
        output = super(CountableWidget, self).render(name, value, final_attrs)
        output += """<span class="text-count" id="%(id)s_counter">Word count: <span class="text-count-current">0</span></span>""" % {'id': final_attrs.get('id'),
           'min_count': final_attrs.get('text_count_min' or 'false'),
           'max_count': final_attrs.get('text_count_max' or 'false')}


class ToggleWidget(forms.widgets.CheckboxInput):
    class Media:
        css = {'all': (
            "https://gitcdn.github.io/bootstrap-toggle/2.2.2/css/bootstrap-toggle.min.css", )}
        js = ("https://gitcdn.github.io/bootstrap-toggle/2.2.2/js/bootstrap-toggle.min.js",)

    def __init__(self, attrs=None, *args, **kwargs):
        attrs = attrs or {}

        default_options = {
            'toggle': 'toggle',
            'offstyle': 'danger'
        }
        options = kwargs.get('options', {})
        default_options.update(options)
        for key, val in default_options.items():
            attrs['data-' + key] = val

        super().__init__(attrs)


class Select2Mixin():
    class Media:
        css = {
            'all': ("https://cdnjs.cloudflare.com/ajax/libs/select2/4.0.6-rc.0/css/select2.min.css",)
        }
        js = ("https://cdnjs.cloudflare.com/ajax/libs/select2/4.0.6-rc.0/js/select2.min.js",
              'customselect2.js')

    def update_attrs(self, options, attrs):
        attrs = self.fix_class(attrs)
        multiple = options.pop('multiple', False)
        attrs['data-adapt-container-css-class'] = 'true'

        if multiple:
            attrs['multiple'] = 'true'

        for key, val in options.items():
            attrs['data-{}'.format(key)] = val

        return attrs

    def fix_class(self, attrs):
        class_name = attrs.pop('class', '')
        if class_name:
            attrs['class'] = '{} {}'.format(
                class_name, 'custom-select2-widget')
        else:
            attrs['class'] = 'custom-select2-widget'

        return attrs


class Select2Widget(Select2Mixin, forms.widgets.Select):
    def __init__(self, attrs=None, choices=(), *args, **kwargs):

        attrs = attrs or {}
        options = kwargs.pop('options', {})
        new_attrs = self.update_attrs(options, attrs)

        super().__init__(new_attrs)
        self.choices = list(choices)


class Select2MultipleWidget(Select2Mixin, forms.widgets.SelectMultiple):
    def __init__(self, attrs=None, choices=(), *args, **kwargs):

        attrs = attrs or {}
        options = kwargs.pop('options', {})
        new_attrs = self.update_attrs(options, attrs)

        super().__init__(new_attrs)
        self.choices = list(choices)


class DropzoneWidget(forms.widgets.FileInput):
    template_name = 'seed/dropzone.html'

    class Media:
        css = {
            'all': ("https://rawgit.com/enyo/dropzone/master/dist/dropzone.css",)
        }
        js = ("https://rawgit.com/enyo/dropzone/master/dist/dropzone.js", 'js/customdz.js')

    def __init__(self, attrs=None, options={}):
        self.options = options

        super().__init__(attrs)

    def get_context(self, name, value, attrs):
        current_class = attrs.get('class')
        custom_class = 'custom-dropzone-widget-' + name

        if current_class:
            attrs['class'] = current_class + ' ' + custom_class
        else:
            attrs['class'] = custom_class
        context = super(DropzoneWidget, self).get_context(name, value, attrs)

        self.options.update({
            'class': custom_class,
            'paramName': name
        })

        context['options'] = self.options
        return context


# class ImageWithAddWidget(forms.widgets.FileInput):
class ImageWithAddWidget(forms.ClearableFileInput):
    template_name = 'seed/image_add_widget.html'

    # class Media:
    #     css = {
    #         'all': ('materialize/css/materialize.css')
    #     }

    # def __init__(self, attrs=None, options={}):
    #     self.options = options
    #     super().__init__(attrs)
    #
    # def get_context(self, name, value, attrs):
    #     current_class = attrs.get('class')
    #     custom_class = 'my-widget-name-' + name
    #     if current_class:
    #         attrs['class'] = current_class + ' ' + custom_class
    #     else:
    #         attrs['class'] = custom_class
    #     context = super(ImageWithAddWidget, self).get_context(name, value, attrs)
    #     self.options.update({
    #         'class': custom_class,
    #         'paramName': name
    #     })
    #     context['options'] = self.options
    #     return context


class SelectWithAddWidget(forms.Select):
    template_name = 'seed/select_with_add_widget.html'

    # def __init__(self, *args, **kwargs):
    #     super(SelectWithAddWidget, self).__init__(*args, **kwargs)

class SelectWithAddContactWidget(forms.Select):
    template_name = 'seed/selectwithadd_supplier_contact.html'