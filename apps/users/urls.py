from django.conf.urls import urls
from . import views

urlpatterns = [
	url(r'^/users$', views.users),
	url(r'^/new$', views.new),
	url(r'^/users/<id>$', views.display),
	url(r'^/users/<id>/edit$', views.edit),
	url(r'^/users/create$', views.create_users),
	url(r'^/users/<id>/destory$', views.destory),
	url(r'^/users/<id>/update$', views.update),

]