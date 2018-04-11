"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import xadmin

from django.conf import settings
from django.conf.urls.static import static
# xadmin.autodiscover()

# from xadmin.plugins import xversion
# xversion.register_models()
from app import views as app
from about import views as about
from single import views as single
from contact import views as contact
urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('', app.index),
    path('about/', about.index),
    path('single/<int:id>', single.index),
    path('contact/', contact.index)
] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
