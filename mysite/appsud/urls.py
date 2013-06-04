from django.conf.urls import patterns, url

from appsud import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^register/$',views.register, name='register'),
    url(r'^authentication/$',views.authentication,name='authentication'),
    url(r'^home/$',views.home,name='home'),
    url(r'^user_logout/$', views.user_logout,name='user_logout'),
    url(r'^upload_application/$',views.upload_application,name='upload_application'),
    url(r'^edit_profile/$',views.edit_profile,name='edit_profile')
)