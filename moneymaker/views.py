from models import Outcome, Product, OutcomeCategory
from rest_framework import viewsets
from moneymaker.serializers import OutcomeSerializer, ProductSerializer, OutcomeCategorySerializer


class OutcomeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows outcome to be viewed or edited.
    """
    queryset = Outcome.objects.all()
    serializer_class = OutcomeSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows outcome to be viewed or edited.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OutcomeCategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows outcome to be viewed or edited.
    """
    queryset = OutcomeCategory.objects.all()
    serializer_class = OutcomeCategorySerializer
