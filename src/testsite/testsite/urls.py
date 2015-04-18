from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'testsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'users.views.home'),
    url(r'^email-sent/', 'users.views.validation_sent'),
    url(r'^login/$', 'users.views.home'),
    url(r'^logout/$', 'users.views.logout'),
    url(r'^done/$', 'users.views.done', name='done'),
    url(r'^ajax-auth/(?P<backend>[^/]+)/$', 'users.views.ajax_auth',
        name='ajax-auth'),
    url(r'^email/$', 'users.views.require_email', name='require_email'),
    url(r'', include('social.apps.django_app.urls', namespace='social')),
    url(r'^admin/', include(admin.site.urls)),
]
