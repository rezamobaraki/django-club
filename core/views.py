from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from core import tasks
from permission_access.permissions import IsSuperUserMixin


class Home(View):
    def get(self, request):
        return render(request, 'core/home.html')


class BucketHome(IsSuperUserMixin, View):
    templates_name = 'core/bucket.html'

    def get(self, request):
        objects = tasks.all_bucket_objects_task()

        return render(request, self.templates_name, {'objects': objects})


class BucketDelete(IsSuperUserMixin, View):
    def get(self, request, key):
        tasks.delete_object_task.delay(key)
        messages.success(request, 'your request will done soon...', 'info')
        return redirect('core:bucket_home')


class BucketDownload(IsSuperUserMixin, View):
    def get(self, request, key):
        tasks.download_object_task.delay(key)
        messages.success(request, 'your download will done soon...', 'info')
        return redirect('core:bucket_home')
