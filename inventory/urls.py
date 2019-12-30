from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'items', views.ItemViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'vendors', views.VendorViewSet)
# router.register(r'groups', views.GroupViewSet)

app_name = "inventory"
urlpatterns = [
    path("main/", views.main.as_view(), name="main"),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include(router.urls)),

    # path("~update/", view=user_update_view, name="update"),
    # path("<str:username>/", view=user_detail_view, name="detail"),
]
