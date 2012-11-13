from django.conf.urls import patterns, include, url
from contactos.views.profile_views import twitter_login, twitter_logout, twitter_authenticated 

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'appContactoMapa.views.home', name='home'),
    # url(r'^appContactoMapa/', include('appContactoMapa.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('contactos.urls')),
    url(r'^login/?$', twitter_login),
    url(r'^logout/?$', twitter_logout),
    url(r'^login/authenticated/?$', twitter_authenticated),
)
