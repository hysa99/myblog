from django.conf.urls.static import static
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from blogg import settings
from . import views



app_name='core_page'



urlpatterns = [
    path('financeandcrypto/', views.crypto, name="crypto"),
    path('business_page/', views.business, name="business"),
    path('entertainment/', views.entertainment, name="entertainment"),
    path('tech_page/', views.tech_page, name="tech_page"),
    path('', views.index, name="index"),
    path('success_page/', views.subscribe, name="subscribe"),
    path('error_page/', views.subscribe, name="subscribe"),
    path('success_page/', views.subscriber, name="subscriber"),
    path('error_page/', views.subscriber, name="subscriber"),
    path("<int:pk>/", views.detail, name="detail"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


