from django.conf.urls import patterns, include, url

from django.contrib import admin

from My.views import *

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:s
    # url(r'^$', 'DjangoApp_Py33.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    ('^hello/$', hello),
    ('^time/$', current_datetime),
    (r'^time/plus/(\d{1,2})/$', hours_ahead),
    (r'^athlete_list/$', athlete_list),
    (r'^country_city_list/$', country_city_list),
    (r'^url_meta/$', display_meta),
    (r'^search/$', search),

)
