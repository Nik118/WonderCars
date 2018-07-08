from django.conf.urls import url
from todolist import views
urlpatterns = [
    url(r'^$', views.todo.as_view(),name='Todolist'),
    url(r'^add/$',views.add,name='add'),
    url(r'^delete/(?P<pk>\d+)/$',views.TodoDeleteView.as_view(),name='remove'),
]
