from django.urls import path,include
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from astro import views


urlpatterns = [
    path('', views.home, name='home'), 
    path('about', views.about, name='about'), 
    path('addevent', views.addevent, name='addevent'), 
    path('showevent', views.showevent, name='showevent'),
    path('event<int:eid>', views.eventDetail, name='eventDetail'),
    path('addblog', views.addblog, name='addblog'),
    path('addmember', views.addmember, name='addmember'),
    path('blog', views.blogs, name='blogs'),
    path('team', views.team, name='team'),
    path('team', views.team, name='team'),
    path('workspace', views.workspace, name='workspace'),
    path('loginall', views.loginall, name='loginall'),
    path('logoutall', views.logoutall, name='logoutall'),
    path('publications', views.Publications, name='Publications'),
    path('addpublications', views.addpublications, name='addpublications'),
    path('interview', views.interview, name='interview'),
    path('addinterview', views.addinterview, name='addinterview'),
    path('gallery', views.gallery, name='gallery'),
    path('addimage', views.addimage, name='addimage'),
    path('readblog<int:bid>', views.readblog, name='readblog'),
    path('profile<int:mid>', views.profile, name='profile'),

    # delete section

    path('deleve<int:eid>', views.deleve, name='deleve'),
    path('delblog<int:bid>', views.delblog, name='delblog'),
    path('delprof<int:pid>', views.delprof, name='delprof'),
    path('delpub<int:puid>', views.delpub, name='delpub'),
    path('delmember<str:mid>', views.delmember, name='delmember'),
    path('delphoto<int:Photo_id>', views.delphoto, name='delmember'),
    # path('delphoto<int:Photo_id>', views.delphoto, name='delmember'),



]
