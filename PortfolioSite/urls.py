from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='homepage'),  
    path('account/', include('accounts.urls')),  
    path('first_app/', include('first_app.urls')),  
    path('second_app/', include('second_app.urls')),  
    path('category/', include('categories.urls')), 
    path('category/<slug:category_slug>/', views.home, name='category_wise_project'),
    path('blog/', include('Blogs.urls')),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
