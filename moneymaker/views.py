from models import Expense, Product, ExpenseCategory
from rest_framework import viewsets
from moneymaker.serializers import ExpenseSerializer
from moneymaker.serializers import ProductSerializer
from moneymaker.serializers import ExpenseCategorySerializer


class ExpenseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows outcome to be viewed or edited.
    """
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows outcome to be viewed or edited.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ExpenseCategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows outcome to be viewed or edited.
    """
    queryset = ExpenseCategory.objects.all()
    serializer_class = ExpenseCategorySerializer
