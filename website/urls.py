from django.contrib import admin
from django.urls import path,include
from webapp import views
from django.conf import settings
from django.conf.urls.static import static

from django.views.static import serve
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('signup/',views.signfunction),
    path('signupform/', views.signupuser,name="signupForm"),
    path('login/',views.logfunction),
    path('about/',views.aboutfunction),
    path('gallary/',views.gallaryfunction),
    path('contact/',views.contactfunction),
    path('contactf/',views.contactf,name="contactf"),
    path('services/',views.services),
    path('details/<int:id>',views.details),
    path('userservice',views.userservice,name="userservice"),
    path('myaccount',views.myaccount),
    path('job/',views.job),
    path('jobform/',views.jobfunction,name="jobform"),
    path('thanku/',views.thanku),
    path('del/<int:id>',views.destroy),

    path('accounts/',include('accounts.urls')),
    path(r'^media/(?P<path>.*)$',serve,{'document_root':    settings.MEDIA_ROOT}),
    url(r'^media/(?P<path>.*)$',serve,{'document_root':settings.STATIC_ROOT}),





]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)        