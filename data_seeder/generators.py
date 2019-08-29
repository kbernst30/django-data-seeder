'''
Generator classes

A collections of classes that generate random data of
different types
'''

import datetime
import random
import string
import uuid

from abc import ABC, abstractmethod
from decimal import Decimal


class AbstractGenerator(ABC):
    '''
    An abstract base class for generator classes

    Methods
    -------

    generate : object
        randomly generates an object
    '''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @abstractmethod
    def generate(self):
        '''
        Generates a random object

        Returns
        -------

        object
            a randomly generated object instance
        '''

        pass


class StaticGenerator(AbstractGenerator):
    '''
    A generator that always returns the same statically
    defined value

    Attributes
    ----------

    value : object
        the value to generate


    Methods
    -------

    generate : object
        generates a static value
    '''

    def __init__(self, value=None, *args, **kwargs):
        '''
        Parameters
        ----------

        value : object
            a value that we want the generator to always return
        '''

        self.value = value
        super().__init__(*args, **kwargs)

    def generate(self):
        '''
        Always generates a statically defined value

        Returns
        -------

        object
            the value attribute of the generator
        '''

        return self.value


class NoneGenerator(AbstractGenerator):
    '''
    A generator that always returns the None

    Methods
    -------

    generate : NoneType
        generates None
    '''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def generate(self):
        '''
        Always generates None

        Returns
        -------

        NoneType
            a None value
        '''

        return None


class BooleanGenerator(AbstractGenerator):
    '''
    A generator that randomy generates a bool

    Methods
    -------

    generate : bool
        generates a boolean value
    '''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def generate(self):
        '''
        Generate a random boolean, True or False

        Returns
        -------

        bool
            a random True or False value
        '''

        return bool(random.getrandbits(1))


class IntegerGenerator(AbstractGenerator):
    '''
    A generator that always returns a random int
    value

    Attributes
    ----------

    range_min : int
        the minimum bounds of the int value

    range_max : int
        the maximum bounds of the int value


    Methods
    -------

    generate : int
        generates an int value
    '''

    range_min = -1000000000
    range_max = 1000000000

    def __init__(self, range_min=None, range_max=None, *args, **kwargs):
        '''
        Parameters
        ----------

        range_min : int, optional
            the minimum bound of the generated int (default is -1000000000)

        range_max: int, optional
            the maximum bound of the generated int (default is 1000000000)
        '''

        if range_min is not None:
            self.range_min = range_min

        if range_max is not None:
            self.range_max = range_max

        super().__init__(*args, **kwargs)

    def generate(self):
        '''
        Generates a random integer value

        Returns
        -------

        int
            a random integer
        '''

        return random.randint(self.range_min, self.range_max)


class PositiveIntegerGenerator(IntegerGenerator):
    '''
    A generator that always returns a random positive int
    value

    Attributes
    ----------

    range_max : int
        the maximum bounds of the int value


    Methods
    -------

    generate : int
        generates a positive int value
    '''

    def __init__(self, range_max=None, *args, **kwargs):
        '''
        Parameters
        ----------

        range_max: int, optional
            the maximum bound of the generated int (default is 1000000000)
        '''

        super().__init__(range_min=0, range_max=range_max, *args, **kwargs)


class NegativeIntegerGenerator(IntegerGenerator):
    '''
    A generator that always returns a random negative int
    value

    Attributes
    ----------

    range_min : int
        the minimum bounds of the int value


    Methods
    -------

    generate : int
        generates a negative int value
    '''

    def __init__(self, range_min=None, *args, **kwargs):
        '''
        Parameters
        ----------

        range_min: int, optional
            the minimum bound of the generated int (default is -1000000000)
        '''

        super().__init__(range_min=range_min, range_max=-1, *args, **kwargs)


class FloatGenerator(AbstractGenerator):
    '''
    A generator that always returns a random float
    value

    Attributes
    ----------

    range_min : int
        the minimum bounds of the float value

    range_max : int
        the maximum bounds of the float value

    precision : int
        the decimal precision for the float value


    Methods
    -------

    generate : float
        generates a float value
    '''

    range_min = -1000000000
    range_max = 1000000000
    precision = 1

    def __init__(self, range_min=None, range_max=None, precision=None, *args,
                 **kwargs):
        '''
        Parameters
        ----------

        range_min : int, optional
            the minimum bound of the generated float (default is -1000000000)

        range_max: int, optional
            the maximum bound of the generated float (default is 1000000000)

        precision: int, optional
            the decimal precision of the generated float (default is 1)
        '''

        if range_min is not None:
            self.range_min = range_min

        if range_max is not None:
            self.range_max = range_max

        if precision is not None:
            self.precision = precision

        super().__init__(*args, **kwargs)

    def generate(self):
        '''
        Generates a random float value

        Returns
        -------

        float
            a random float
        '''

        return round(random.uniform(self.range_min, self.range_max),
                     self.precision)


class PositiveFloatGenerator(FloatGenerator):
    '''
    A generator that always returns a random positive float
    value

    Attributes
    ----------

    range_max : int
        the maximum bounds of the float value

    precision : int
        the decimal precision for the float value

    Methods
    -------

    generate : float
        generates a positive float value
    '''

    def __init__(self, range_max=None, precision=None, *args, **kwargs):
        '''
        Parameters
        ----------

        range_max: int, optional
            the maximum bound of the generated float (default is 1000000000)

        precision: int, optional
            the decimal precision of the generated float (default is 1)
        '''

        super().__init__(range_min=0, range_max=range_max, precision=precision,
                         *args, **kwargs)


class NegativeFloatGenerator(FloatGenerator):
    '''
    A generator that always returns a random negative float
    value

    Attributes
    ----------

    range_min : int
        the minimum bounds of the float value

    precision : int
        the decimal precision for the float value

    Methods
    -------

    generate : float
        generates a positive float value
    '''

    def __init__(self, range_min=None, precision=None, *args, **kwargs):
        '''
        Parameters
        ----------

        range_min: int, optional
            the minimum bound of the generated float (default is -1000000000)

        precision: int, optional
            the decimal precision of the generated float (default is 1)
        '''

        super().__init__(range_min=range_min, range_max=-1,
                         precision=precision, *args, **kwargs)


class DecimalGenerator(FloatGenerator):
    '''
    A generator that always returns a random Decimal
    value

    Attributes
    ----------

    range_min : int
        the minimum bounds of the Decimal value

    range_max : int
        the maximum bounds of the Decimal value

    precision : int
        the decimal precision for the Decimal value


    Methods
    -------

    generate : Decimal
        generates a Decimal value
    '''

    def __init__(self, range_min=None, range_max=None, precision=None, *args,
                 **kwargs):
        '''
        Parameters
        ----------

        range_min : int, optional
            the minimum bound of the generated Decimal (default is -1000000000)

        range_max: int, optional
            the maximum bound of the generated Decimal (default is 1000000000)

        precision: int, optional
            the decimal precision of the generated Decimal (default is 1)
        '''

        super().__init__(range_min=range_min, range_max=range_max,
                         precision=precision, *args, **kwargs)

    def generate(self):
        '''
        Generates a random Decimal value

        Returns
        -------

        Decimal
            a random Decimal
        '''

        return round(Decimal(super().generate()), self.precision)


class PositiveDecimalGenerator(DecimalGenerator):
    '''
    A generator that always returns a random positive Decimal
    value

    Attributes
    ----------

    range_max : int
        the maximum bounds of the Decimal value

    precision : int
        the decimal precision for the Decimal value

    Methods
    -------

    generate : Decimal
        generates a positive Decimal value
    '''

    def __init__(self, range_max=None, precision=None, *args, **kwargs):
        '''
        Parameters
        ----------

        range_max: int, optional
            the maximum bound of the generated Decimal (default is 1000000000)

        precision: int, optional
            the decimal precision of the generated Decimal (default is 1)
        '''

        super().__init__(range_min=0, range_max=range_max, precision=precision,
                         *args, **kwargs)


class NegativeDecimalGenerator(DecimalGenerator):
    '''
    A generator that always returns a random negative Decimal
    value

    Attributes
    ----------

    range_min : int
        the minimum bounds of the Decimal value

    precision : int
        the decimal precision for the Decimal value

    Methods
    -------

    generate : Decimal
        generates a negative Decimal value
    '''

    def __init__(self, range_min=None, precision=None, *args, **kwargs):
        '''
        Parameters
        ----------

        range_min: int, optional
            the minimum bound of the generated Decimal (default is -1000000000)

        precision: int, optional
            the decimal precision of the generated Decimal (default is 1)
        '''

        super().__init__(range_min=range_min, range_max=-1,
                         precision=precision, *args, **kwargs)


class StringGenerator(AbstractGenerator):
    '''
    A generator that returns a randomly generated string

    Attributes
    ----------

    max_length : int
        the maximum length of the generated string

    Methods
    -------

    generate : str
        generates a random string
    '''

    max_length = 20

    def __init__(self, max_length=None, *args, **kwargs):
        '''
        Parameters
        ----------

        max_length: int, optional
            the maximum length of the generated string (default is 20)
        '''

        if max_length is not None:
            self.max_length = max_length

        super().__init__(*args, **kwargs)

    def generate(self):
        '''
        Generates a random string value

        Returns
        -------

        str
            a random string
        '''

        str_length = random.randint(1, self.max_length)
        value = u''

        for i in range(str_length):
            value += random.choice(string.ascii_letters + u' ')

        return value


class DateTimeGenerator(AbstractGenerator):
    '''
    A generator that returns a random datetime

    Attributes
    ----------

    min_date : datetime.datetime
        the lower bounds for the random datetime

    max_date : datetime.datetime
        the upper bounds for the random datetime

    Methods
    -------

    generate : datetime.datetime
        generates a random datetime
    '''

    def __init__(self, min_date=None, max_date=None, *args, **kwargs):
        '''
        Parameters
        ----------

        min_date: datetime.datetime, optional
            the lower bounds for the random datetime
            (default is 30 days before now)

        max_date: datetime.datetime, optional
            the upper bounds for the random datetime
            (default is 30 days from now)
        '''

        today = datetime.datetime.now()

        if min_date is None:
            self.min_date = today - datetime.timedelta(days=30)
        else:
            self.min_date = min_date

        if max_date is None:
            self.max_date = today + datetime.timedelta(days=30)
        else:
            self.max_date = max_date

        super().__init__(*args, **kwargs)

    def generate(self):
        '''
        Generates a random datetime value

        Returns
        -------

        datetime.datetime
            a random datetime
        '''

        timestamp = random.randint(round(self.min_date.timestamp()),
                                   round(self.max_date.timestamp()))

        return datetime.datetime.fromtimestamp(timestamp)


class DateGenerator(DateTimeGenerator):
    '''
    A generator that returns a random date

    Attributes
    ----------

    min_date : datetime.datetime
        the lower bounds for the random date

    max_date : datetime.datetime
        the upper bounds for the random date

    Methods
    -------

    generate : datetime.date
        generates a random date
    '''

    def __init__(self, min_date=None, max_date=None, *args, **kwargs):
        '''
        Parameters
        ----------

        min_date: datetime.date, optional
            the lower bounds for the random date
            (default is 30 days before now)

        max_date: datetime.date, optional
            the upper bounds for the random date
            (default is 30 days from now)
        '''

        min_datetime = None
        max_datetime = None
        min_time = datetime.datetime.min.time()

        if min_date is not None:
            min_datetime = datetime.datetime.combine(min_date, min_time)

        if max_date is not None:
            max_datetime = datetime.datetime.combine(max_date, min_time)

        super().__init__(min_date=min_datetime, max_date=max_datetime, *args,
                         **kwargs)

    def generate(self):
        '''
        Generates a random date value

        Returns
        -------

        datetime.date
            a random date
        '''

        return super().generate().date()


class TimeGenerator(AbstractGenerator):
    '''
    A generator that returns a random time

    Methods
    -------

    generate : datetime.time
        generates a random time
    '''

    def __init__(self,  *args, **kwargs):
        super().__init__(*args, **kwargs)

    def generate(self):
        '''
        Generates a random time value

        Returns
        -------

        datetime.time
            a random time
        '''

        hour = random.randint(0, 23)
        minute = random.randint(0, 59)
        second = random.randint(0, 59)

        return datetime.time(hour, minute, second)


class EmailGenerator(StringGenerator):
    '''
    A generator that returns a randomly generated email address

    Methods
    -------

    generate : str
        generates a random email address
    '''

    def __init__(self,  *args, **kwargs):
        super().__init__(*args, **kwargs)

    def generate(self):
        '''
        Generates a random email address

        Returns
        -------

        str
            a string representing a valid email address
        '''

        return "%s@%s.com" % (super().generate(), super().generate())


class UrlGenerator(StringGenerator):
    '''
    A generator that returns a randomly generated URL

    Methods
    -------

    generate : str
        generates a random URL
    '''

    def __init__(self,  *args, **kwargs):
        super().__init__(*args, **kwargs)

    def generate(self):
        '''
        Generates a random URL

        Returns
        -------

        str
            a string representing a valid URL
        '''

        return "http://%s.com" % super().generate()


class IpAddressGenerator(AbstractGenerator):
    '''
    A generator that returns a randomly generated IPv4 Address

    Methods
    -------

    generate : str
        generates a random IPv4 Address
    '''

    def __init__(self,  *args, **kwargs):
        super().__init__(*args, **kwargs)

    def generate(self):
        '''
        Generates a random IPv4 Address

        Returns
        -------

        str
            a string representing a valid IPv4 Address
        '''

        return '.'.join(str(part) for part in [
            PositiveIntegerGenerator(max_range=255).generate(),
            PositiveIntegerGenerator(max_range=255).generate(),
            PositiveIntegerGenerator(max_range=255).generate(),
            PositiveIntegerGenerator(max_range=255).generate()
        ])


class UuidGenerator(AbstractGenerator):
    '''
    A generator that returns a randomly generated UUID

    Methods
    -------

    generate : uuid.UUID
        generates a random UUID
    '''

    def __init__(self,  *args, **kwargs):
        super().__init__(*args, **kwargs)

    def generate(self):
        '''
        Generates a random UUID

        Returns
        -------

        uuid.UUID
            a ranom UUID
        '''

        return uuid.uuid4()
