from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('organizerhome/',views.organizerhome,name="organizerhome"),
    path('organizerhome/eventdata',views.datadb,name="eventdata"),
    path('showevents/',views.showevents,name="showevents"),
    path('showevents/proceedtopay',views.proceedtopay,name="proceedtopay"),
    path('showevents/register/',views.register,name="register"),
    path('',views.home,name="home")
]

'''if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)'''