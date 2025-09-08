
from .models import Expense
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.db.models import Sum, F


class ExpenseListView(ListView):
    model = Expense
    template_name = "expense_list.html"
    context_object_name = "expenses"

    def get_queryset(self):
        queryset = super().get_queryset()
        date = self.request.GET.get("date")
        if date:  # filter by selected date
            queryset = queryset.filter(create__date=date)
        return queryset

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        total = self.get_queryset().aggregate(
            total_sum=Sum(F("amount") * F("quantity"))
        )
        data["total"] = total["total_sum"]
        return data


class ExpenseCreateView(CreateView):
    model = Expense
    template_name = "add_expense.html"
    fields = "__all__"
    success_url = reverse_lazy("expense_list")