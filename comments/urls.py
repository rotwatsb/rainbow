from django.conf.urls import patterns, url
from comments import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'comments_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index, name='index'),
    #url(r'^login/$', views.user_login, name='login'),
    #url(r'^logout/$', views.user_logout, name='logout'),
    #url(r'^register/$', views.register, name='register'),
    url(r'^restricted/$', views.restricted, name='restricted'),
    url(r'^add_conversation/$', views.add_conversation, name='add_conversation'),
    url(r'^(?P<conversation_name_slug>[\w\-]+)/$', views.conversation, name='conversation'),
    url(r'^(?P<conversation_name_slug>[\w\-]+)/add_comment/$', views.add_comment, name='add_comment'),
    url(r'^(?P<conversation_name_slug>[\w\-]+)/add_comment/(?P<reply_to_id>null)/$', views.add_comment, name='add_comment'),
    url(r'^(?P<conversation_name_slug>[\w\-]+)/add_comment/(?P<reply_to_id>[\d]+)/$', views.add_comment, name='add_comment'),
)
