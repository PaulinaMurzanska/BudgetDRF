from django.contrib.auth.models import User
from rest_framework import serializers, fields
from django.contrib.auth import get_user_model
from .models import (Category, Expenses, Income)


class AdminCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            "id",
            "name",
            "user",
            'url',
        ]


class CategorySerializer(AdminCategorySerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())


class AdminExpensesSerializer(serializers.ModelSerializer):
    # timestamp = fields.DateField(format="%m-%d-%Y", input_formats=['%m-%d-%Y', 'iso-8601'])

    class Meta:
        model = Expenses
        fields = [
            "id",
            "name",
            'user',
            'amount',
            'category',
            'timestamp',
            'url',
        ]


class ExpensesSerializer(AdminExpensesSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())


class AdminIncomeSerializer(serializers.ModelSerializer):
    # timestamp = fields.DateField(format="%m-%d-%Y", input_formats=['%m-%d-%Y', 'iso-8601'])
    class Meta:
        model = Income
        fields = [
            'id',
            'name',
            'user',
            'amount',
            'timestamp',
            'url',
        ]


class IncomeSerializer(AdminIncomeSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",

        ]







