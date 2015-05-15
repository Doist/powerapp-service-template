# -*- coding: utf-8 -*-
from powerapp.core import django_forms, generic_views

# We define two classes here:
#
# 1. The form to create and modify integrations. It's managed from the
#    controller
#
# 2. The class-based controller to handle GET and POST requests
#
# Current implementation just provides a form to create a simple integration
# without any settings and should work out of the box. Feel free to populate
# your form with regular Django fields and corresponding values will be
# automatically saved as integration properties.
#
# See here for the list of fields you can add to the form
# https://docs.djangoproject.com/en/1.8/ref/forms/fields/#built-in-field-classes
#
# The EditIntegrationView pre-supposes that there's a template
# {{ app_name }}/edit_integration.html accepting a form object, and it's used
# to display integration add / modify form.


class IntegrationForm(django_forms.IntegrationForm):
    service_label = '{{ app_name }}'


class EditIntegrationView(generic_views.EditIntegrationView):
    service_label = '{{ app_name }}'
    form = IntegrationForm
