from rest_framework import viewsets
from django.contrib.auth.models import User

from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView

from .models import (
    Category,
    Expenses,
    Income
)

from .serializers import (
    AdminCategorySerializer,
    CategorySerializer,
    AdminExpensesSerializer,
    AdminIncomeSerializer,
    ExpensesSerializer,
    IncomeSerializer,
    UserSerializer,
)


class AdminViewSetMixin:
    model = None
    admin_serializer_class = None
    user_serializer_class = None

    def get_queryset(self):
        if self.request.user.is_superuser:
            return self.model.objects.all()
        return self.model.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.request.user.is_superuser:
            return self.admin_serializer_class
        return self.user_serializer_class


class CategoryViewSet(AdminViewSetMixin, viewsets.ModelViewSet):
    model = Category
    admin_serializer_class = AdminCategorySerializer
    user_serializer_class = CategorySerializer

    # def get_queryset(self):
    #     if self.request.user.is_superuser:
    #         return Category.objects.all()
    #
    #     return Category.objects.filter(user=self.request.user)
    #
    # def get_serializer_class(self):
    #     if self.request.user.is_superuser:
    #         return AdminCategorySerializer
    #     return CategorySerializer


class ExpensesViewSet(AdminViewSetMixin, viewsets.ModelViewSet):
    model = Expenses
    admin_serializer_class = AdminExpensesSerializer
    user_serializer_class = ExpensesSerializer


class IncomeViewSet(AdminViewSetMixin, viewsets.ModelViewSet):
    model = Income
    admin_serializer_class = AdminIncomeSerializer
    user_serializer_class = IncomeSerializer


class ProfileRetrieveView(RetrieveAPIView):
    # retrieve==GET/object/<pk>
    def retrieve(self, request, pk=None):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)




