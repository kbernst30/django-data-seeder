from django.contrib import admin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import path

from .base import DataSeeder


class DataGeneratorAdmin(admin.ModelAdmin):
    change_list_template = "admin/data_generator/change_list.html"

    def get_urls(self):
        urls = super().get_urls()
        info = self.model._meta.app_label, self.model._meta.model_name

        return [
            path('generate/', self.admin_site.admin_view(self.generate),
                 name="%s_%s_generate" % info)
        ] + urls

    def generate(self, request):
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

    class DataGeneratorRegisterdCls(DataGeneratorAdmin):

        def __init__(self, *args, **kwargs):
            self.oInstance = Cls(*args, **kwargs)

        def __getattribute__(self, name):
            try:
                return super(DataGeneratorRegisterdCls,
                             self).__getattribute__(name)

            except AttributeError:
                return self.oInstance.__getattribute__(name)

    return DataGeneratorRegisterdCls
