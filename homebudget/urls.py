from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register("category", views.CategoryViewSet, basename="category")
router.register("expenses", views.ExpensesViewSet, basename="expenses")
router.register("income", views.IncomeViewSet, basename="income")


urlpatterns = [
    path("", include(router.urls)),
    path("profile/", views.ProfileRetrieveView.as_view(), name="profile"),


]