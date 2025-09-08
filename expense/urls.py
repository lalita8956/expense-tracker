# urls.py
from django.urls import path
from .views import ExpenseListView, ExpenseCreateView

urlpatterns = [
    path('', ExpenseListView.as_view(), name='expense_list'),
    path('add/', ExpenseCreateView.as_view(), name='add_expense'),
]