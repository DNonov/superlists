from django.conf.urls import url
from lists import views

urlpatterns = [
    url('^new$', views.new_list, name='view_list'),
    url('^(\d+)/$', views.view_list, name='view_list'),
    url('^(\d+)/add-item$', views.add_item, name='add_item'),
]
