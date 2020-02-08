from graphene import Mutation, Field, String, Int
from graphene import ObjectType
from .models import Car
from .types import CarType
from graphql import GraphQLError


class CreateCar(Mutation):
    car = Field(CarType)

    class Arguments:
        make = String(required=True)
        model = String(required=False)
        body_type = String(required=True)

    def mutate(self, info, **kwargs):
        car = Car.objects.create(**kwargs)
        return CreateCar(car=car)


class DeleteCar(Mutation):
    car_id = Int()

    class Arguments:
        id = Int(required=True)

    def mutate(self, info, id):
        try:
            car = Car.objects.get(id=id)
        except Car.DoesNotExist:
            raise GraphQLError("Car Does not exists")
        else:
            car_id = car.id
            car.delete()
            return DeleteCar(car_id=car_id)


class UpdateCar(Mutation):
    car = Field(CarType)

    class Arguments:
        id = Int(required=True)
        make = String(required=False)
        model = String(required=False)
        body_type = String(required=False)

    def mutate(self, info, **kwargs):

        try:
            car = Car.objects.get(id=kwargs['id'])
        except Car.DoesNotExist:
            raise GraphQLError("Car Does not exists")
        else:
            car.model = kwargs.get('model', car.model)
            car.make = kwargs.get('make', car.make)
            car.body_type = kwargs.get('body_type', car.body_type)
            car.save()
        return UpdateCar(car=car)


class MainMutation(ObjectType):
    create_car = CreateCar.Field()
    delete_car = DeleteCar.Field()
    update_car = UpdateCar.Field()
