from unicodedata import name
from django.urls import path

from . import views

app_name = 'app'


urlpatterns = [

    path('', views.index, name='index'),
    path('login/', views.login_view, name='login_view'),

    # ADMIN
    path('admin_manager/', views.admin_manager_view, name='admin_manager'),

    # USERS
    path('users_register/', views.users_manager_view, name='users_manager'),


    # CATEGORIES
    path('category/', views.category, name='category'),
    path('new_category/', views.new_category_view, name='new_category'),
    path('edit_category/<int:id_category>/', views.edit_category_view, name='edit_category'),
    path('delete_category/<int:id_category>/', views.delete_category_view, name='delete_category'),
    
    # POSTS
    path('post/', views.post, name='post'),
    path('new_post/', views.new_post_view, name='new_post'),
    path('edit_post/<int:id_post>/', views.edit_post_view, name='edit_post'),
    path('delete_post/<int:id_post>/',views.delete_post_view, name='delete_post'),

    # COMMENTS
    path('new_comment/', views.new_comment_view, name='new_comment'),
    path('edit_comment/<int:id_post>/<int:id_comment>', views.edit_comment_view, name='edit_comment'),
    path('delete_comment/<int:id_comment>/',views.delete_comment_view, name='delete_comment'),

    # LOGOUT
    path('logout/', views.logout_view, name='logout'),
    
]