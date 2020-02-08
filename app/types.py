from .models import Car, Customer
import graphene_django


class CarType(graphene_django.DjangoObjectType):
    class Meta:
        model = Car


class CustomerType(graphene_django.DjangoObjectType):
    class Meta:
        model = Customer
