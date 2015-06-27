from django.conf.urls import patterns, include, url
from django.contrib import admin
from comments import views
from registration.backends.simple.views import RegistrationView

class MyRegistrationView(RegistrationView):
    def get_success_url(self, request, user):
        return '/comments/'

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'comments_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^$', views.index, name='index'),                       
    url(r'^admin/', include(admin.site.urls)),
    url(r'^comments/', include('comments.urls')),
    url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
)
