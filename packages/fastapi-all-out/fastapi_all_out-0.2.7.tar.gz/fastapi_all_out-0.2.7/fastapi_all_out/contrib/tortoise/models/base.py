from collections.abc import Callable
from typing import Any, Type

from tortoise import Model as DefaultModel


class BaseModel(DefaultModel):
    IEXACT_FIELDS: set[str] = ()

    class Meta:
        abstract = True
    #
    # @classmethod
    # async def check_unique(cls, data: dict[str, Any]) -> list[str]:
    #     # TODO: self.__class__._meta.unique_together
    #     not_unique = []
    #     query = cls.all()
    #     for key, value in cls._meta.fields_map.items():
    #         if (
    #                 not value.generated
    #                 and value.unique
    #                 and (current_value := data.get(key)) is not None
    #         ):
    #             if await query.filter(**{key: current_value}).exists():
    #                 not_unique.append(key)
    #     return not_unique


def get_field_param(model: Type[BaseModel], field_name: str, field_param: str):
    return getattr(model._meta.fields_map[field_name], field_param)


def max_len_of(model: Type[BaseModel]) -> Callable[[str], int]:
    return lambda field_name: get_field_param(model, field_name, 'max_length')


def default_of(model: Type[BaseModel]) -> Callable[[str], Any]:
    return lambda field_name: get_field_param(model, field_name, 'default')
