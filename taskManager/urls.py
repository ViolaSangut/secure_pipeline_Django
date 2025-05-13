#     _  _                        __   __
#  __| |(_)__ _ _ _  __ _ ___   _ \ \ / /
# / _` || / _` | ' \/ _` / _ \_| ' \ V /
# \__,_|/ \__,_|_||_\__, \___(_)_||_\_/
#     |__/          |___/
#
#			INSECURE APPLICATION WARNING
#
# django.nV is a PURPOSELY INSECURE web-application
# meant to demonstrate Django security problems
# UNDER NO CIRCUMSTANCES should you take any code
# from django.nV for use in another web application!
#

from django.contrib import admin
from django.urls import path, include
from taskManager import views

urlpatterns = [
    path('', views.index, name='index'),
    path('taskManager/', include(('taskManager.taskManager_urls', 'taskManager'), namespace='taskManager')),
    path('admin/', admin.site.urls),
]


