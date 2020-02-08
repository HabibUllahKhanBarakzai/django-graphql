from graphene import Schema, ObjectType
from app import queries as app_query
from app.mutation import MainMutation


class Query(app_query.CarQuery, ObjectType):
    pass


schema = Schema(query=Query, mutation=MainMutation)
