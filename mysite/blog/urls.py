from django.urls import path
from . import views

app_name = 'blog'    # This lets us create a namespace for urls

urlpatterns = [
    # Post views
    path('', views.PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
        views.post_detail,
        name='post_detail')
]