# basic URL Configurations
from django.urls import include, path
# import routers
from rest_framework import routers
from django.contrib import admin
# import everything from views
from apis.views import *

# define the router
router = routers.DefaultRouter()

# define the router path and viewset to be used
router.register(r'brand', brandViewSets)
router.register(r'category', categoryViewSets)
router.register(r'attributes', attributeViewSets)
router.register(r'products', productsViewSets)

# specify URL Path for rest_framework
urlpatterns = [
	path('', include(router.urls)),
	path('api/', include('rest_framework.urls')),
	path('admin/', admin.site.urls)
]
