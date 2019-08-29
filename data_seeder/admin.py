'''
Classes and functions that are necessary for the Django Admin Site
'''

from django.contrib import admin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import path

from .base import DataSeeder


class DataGeneratorAdmin(admin.ModelAdmin):
    '''
    A subclass of django.contrib.admin.ModelAdmin

    This class adds functionality to generate data seeds
    right from the Django Admin site

    Attributes
    ----------

    change_list_template : str
        A path to the overriden change_list template


    Methods
    -------

    get_urls : list
        returns a list of valid URLs for the Admin site

    generate : django.http.HttpResponse
        returns a valid HttpResponse for generate action
    '''

    change_list_template = "admin/data_generator/change_list.html"

    def get_urls(self):
        '''
        Returns a list of valid URLs for the Admin site

        Returns
        -------
        list
            a list of valid URLs for the Admin site. We add
            the 'generate/' path to the URLs already valid
            from the superclass
        '''

        urls = super().get_urls()
        info = self.model._meta.app_label, self.model._meta.model_name

        return [
            path('generate/', self.admin_site.admin_view(self.generate),
                 name="%s_%s_generate" % info)
        ] + urls

    def generate(self, request):
        '''
        Performs the generate action

        If the action is a GET request, the function will process
        and return a valid form to the user to generate seeds.

        If the action is a POST request, this will properly process
        the seeds, generate them, and redirect back to the change_list

        Parameters
        ----------

        request : django.http.request
            the request object


        Returns
        -------

        django.http.HttpResponse
            Either a response object containing the generate form and options
            or a redirect response
        '''

        if request.method == 'POST':
            num_to_generate = int(request.POST.get('generate_num', 1))
            DataSeeder(self.model, seeds=num_to_generate).seed()
            return HttpResponseRedirect('../')

        page_title = self.model._meta.verbose_name_plural.title()

        return render(request, 'admin/data_generator/generate_form.html', {
            'opts': self.model._meta,
            'title': 'Generate %s' % page_title,
            'has_view_permission': self.has_view_permission(request),
            'has_change_permission': self.has_change_permission(request)
        })


def data_generator_register(Cls):
    '''
    A class decorator to register a ModelAdmin with the data
    seeder for the Admin Site

    Parameters
    ----------

    Cls : type
        A type of django.contrib.admin.ModelAdmin


    Returns
    -------

    type
        type DataGeneratorRegisterdCls to wrap the original Cls
    '''

    class DataGeneratorRegisterdCls(DataGeneratorAdmin):
        '''
        This class wraps a ModelAdmin so an instance of
        that class gets the functionality of DataGeneratorAdmin

        Attributes
        ----------

        oInstance : object
            an instance of ModelAdmin to wrap
        '''

        def __init__(self, *args, **kwargs):
            self.oInstance = Cls(*args, **kwargs)

        def __getattribute__(self, name):
            try:
                return super(DataGeneratorRegisterdCls,
                             self).__getattribute__(name)

            except AttributeError:
                return self.oInstance.__getattribute__(name)

    return DataGeneratorRegisterdCls
