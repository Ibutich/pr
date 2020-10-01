from django.conf.urls import url
from django.urls import path
from django.contrib import admin
from .views import SearchResultsView
from . import views

admin.site.site_header = 'Suvey App admin'
admin.site.site_title = 'Suvey App admin'
admin.site.site_url = 'http://surveyapp.com/'
admin.site.index_title = 'Suvey App Administration'
admin.empty_value_display = '**Empty**'

app_name = "Pr"

urlpatterns = [
    # ex: /
    url(r'^reviews$', views.review_list, name='review_list'),
    # ex: /review/5/
    url(r'^review/(?P<review_id>[0-9]+)/$', views.review_detail, name='review_detail'),
    # ex: /company/
    url(r'^$', views.company_list, name='company_list'),
    # ex: /company/5/
    url(r'^company/(?P<company_id>[0-9]+)/$', views.company_detail, name='company_detail'),
    url(r'^company/(?P<company_id>[0-9]+)/add_review/$', views.add_review, name='add_review'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
]