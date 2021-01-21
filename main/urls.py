from rest_framework.routers import DefaultRouter
from django.urls import path,include
from . import views
router = DefaultRouter()
router.register('branches',views.BranchViewSet)

urlpatterns = [
path('',include(router.urls)),
path('all/',views.BankBranchView.as_view()),


]
