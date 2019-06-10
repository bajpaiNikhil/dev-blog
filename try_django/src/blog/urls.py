
from .views import (
    blog_post_detail_view,
    blog_post_list_view,
    blog_post_delete_view,
    blog_post_update_view

)

from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('', blog_post_list_view),
    path('<str:slug>', blog_post_detail_view),
    path('<str:slug>/edit/', blog_post_update_view),
    path('<str:slug>/delete', blog_post_delete_view),

]