from django.conf.urls import url
from django.urls import path
from .views import inventory_list

app_name = "vendomaticapp"

urlpatterns = [
    # url(r'^$', home, name='home'),
    url(r'^inventory$', inventory_list, name='inventory'),
    # url(r'^inventory/<int:inventory_id>/$', inventory_detail, name='inventory_item'),
    # url(r'^book/form$', book_form, name='book_form'),
    # path('books/<int:book_id>/', book_details, name='book'),
    # url(r'^books/(?P<book_id>[0-9]+)/form$', book_edit_form, name='book_edit_form'),
]