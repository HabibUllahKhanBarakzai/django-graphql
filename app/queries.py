import graphene
from .models import Car, Customer
from .types import CarType


class CarQuery(graphene.ObjectType):
    all_cars = graphene.List(CarType)

    def resolve_all_cars(self, info: dict) -> list:
        return Car.objects.all()
