import random
import sys
from string import ascii_lowercase, ascii_uppercase, digits, punctuation

from termcolor import colored

from src.descriptors import LengthDescriptor, LevelDescriptor


class PasswordGenerator:
    """
    This class is used to generate a password with
    three different levels of soft, medium and hard.
    """
    level = LevelDescriptor()
    length = LengthDescriptor()

    def __init__(self, *, level: str = 'hard', length: int = 20):
        """
        Set level and length attributes of password

        :param level: Password strength level
        :param length: Password length
        """
        self.level = level
        self.length = length

    def soft_pass(self) -> str:
        """
        Create a password with soft level

        :return: Password string
        """
        length = self.length
        password_list = list()

        for _ in range(length):
            random_number = random.randint(1, 2)

            if random_number == 1:
                single_pass = random.choice(digits)

            else:
                single_pass = random.choice(ascii_lowercase)

            password_list.append(single_pass)

        random.shuffle(password_list)
        password_string = ''.join(password_list)

        return password_string

    def medium_pass(self) -> str:
        """
        Create a password with medium level

        :return: Password string
        """
        length = self.length
        password_list = list()

        for _ in range(length):
            random_number = random.randint(1, 3)

            if random_number == 1:
                single_pass = random.choice(digits)

            elif random_number == 2:
                single_pass = random.choice(ascii_lowercase)

            else:
                single_pass = random.choice(ascii_uppercase)

            password_list.append(single_pass)

        random.shuffle(password_list)
        password_string = ''.join(password_list)

        return password_string

    def hard_pass(self) -> str:
        """
        Create a password with hard level

        :return: Password string
        """
        length = self.length
        password_list = list()

        for _ in range(length):
            random_number = random.randint(1, 4)

            if random_number == 1:
                single_pass = random.choice(digits)

            elif random_number == 2:
                single_pass = random.choice(ascii_lowercase)

            elif random_number == 3:
                single_pass = random.choice(ascii_uppercase)

            else:
                single_pass = random.choice(punctuation)

            password_list.append(single_pass)

        random.shuffle(password_list)
        password_string = ''.join(password_list)

        return password_string

    def __call__(self) -> str:
        """
        Call one of the pass methods

        :return: Password string
        """
        if self.level == 'soft':
            password = self.soft_pass()

        elif self.level == 'medium':
            password = self.medium_pass()

        else:
            password = self.hard_pass()

        return password


if __name__ == '__main__':
    level = sys.argv[1]
    length = sys.argv[2]

    password = PasswordGenerator(level=level, length=int(length))

    print()
    print(colored('Your Password is:', 'yellow'), end='\n\n')
    print(colored(password(), 'green'), end='\n\n')
