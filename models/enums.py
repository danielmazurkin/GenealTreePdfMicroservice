import enum


class UserRoleEnum(enum.Enum):
    """Роли пользователей в генеалогическом древе."""

    viewer = 'Зритель'
    admin = 'Администратор'
