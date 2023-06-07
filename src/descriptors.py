class LevelDescriptor:
    def __init__(self, level: str = 'hard'):
        self.__level = level

    def __get__(self, obj, owner) -> str:
        return self.__level

    def __set__(self, obj, value):
        if value in {'hard', 'medium', 'soft'}:
            self.__level = value
        else:
            raise ValueError(f'{value} is not a valid value. It can be hard, medium or soft.')


class LengthDescriptor:
    def __init__(self, length: int = 20):
        self.__length = length

    def __get__(self, obj, owner) -> int:
        return self.__length

    def __set__(self, obj, value):
        if obj.level == 'soft' and value >= 8:
            self.__length = value

        elif obj.level == 'medium' and value >= 12:
            self.__length = value

        elif obj.level == 'hard' and value >= 16:
            self.__length = value

        else:
            raise ValueError(f'Password Length must be greater.')
