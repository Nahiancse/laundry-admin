"""laundry3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from service import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.welcome),

    path('load_form', views.load_form),
    path('show', views.show),

    path('add_item', views.addItem),




#     for category
# path('showCategory/<str:parent_or_child>/<int:pk>/', views.showCat),
path('load_cat_form', views.load_cat_form),
path('add_sub_item', views.addsubItem),

 path('showCategory/<str:parent_or_child>/<int:pk>/', views.showCat,name='index'),



    # for edit/update

    path('editItem/<int:id>', views.editItem),
    path('updateItem/<int:id>', views.updateItem),



]
urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
