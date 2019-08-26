import datetime
import random
import string
import uuid

from abc import ABC, abstractmethod
from decimal import Decimal


class AbstractGenerator(ABC):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @abstractmethod
    def generate(self):
        pass


class StaticGenerator(AbstractGenerator):

    def __init__(self, value=None, *args, **kwargs):
        self.value = value
        super().__init__(*args, **kwargs)

    def generate(self):
        return self.value


class NoneGenerator(AbstractGenerator):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def generate(self):
        return None


class BooleanGenerator(AbstractGenerator):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def generate(self):
        return bool(random.getrandbits(1))


class IntegerGenerator(AbstractGenerator):

    range_min = -1000000000
    range_max = 1000000000

    def __init__(self, range_min=None, range_max=None, *args, **kwargs):
        if range_min is not None:
            self.range_min = range_min

        if range_max is not None:
            self.range_max = range_max

        super().__init__(*args, **kwargs)

    def generate(self):
        return random.randint(self.range_min, self.range_max)


class PositiveIntegerGenerator(IntegerGenerator):

    def __init__(self, range_max=None, *args, **kwargs):
        super().__init__(range_min=0, range_max=range_max, *args, **kwargs)


class NegativeIntegerGenerator(IntegerGenerator):

    def __init__(self, range_min=None, *args, **kwargs):
        super().__init__(range_min=range_min, range_max=-1, *args, **kwargs)


class FloatGenerator(AbstractGenerator):
    range_min = -1000000000
    range_max = 1000000000
    precision = 1

    def __init__(self, range_min=None, range_max=None, precision=None, *args,
                 **kwargs):

        if range_min is not None:
            self.range_min = range_min

        if range_max is not None:
            self.range_max = range_max

        if precision is not None:
            self.precision = precision

        super().__init__(*args, **kwargs)

    def generate(self):
        return round(random.uniform(self.range_min, self.range_max),
                     self.precision)


class PositiveFloatGenerator(FloatGenerator):

    def __init__(self, range_max=None, precision=None, *args, **kwargs):
        super().__init__(range_min=0, range_max=range_max, precision=precision,
                         *args, **kwargs)


class NegativeFloatGenerator(FloatGenerator):

    def __init__(self, range_min=None, precision=None, *args, **kwargs):
        super().__init__(range_min=range_min, range_max=-1,
                         precision=precision, *args, **kwargs)


class DecimalGenerator(FloatGenerator):

    def __init__(self, range_min=None, range_max=None, precision=None, *args,
                 **kwargs):

        super().__init__(range_min=range_min, range_max=range_max,
                         precision=precision, *args, **kwargs)

    def generate(self):
        return round(Decimal(super().generate()), self.precision)


class PositiveDecimalGenerator(DecimalGenerator):

    def __init__(self, range_max=None, precision=None, *args, **kwargs):
        super().__init__(range_min=0, range_max=range_max, precision=precision,
                         *args, **kwargs)


class NegativeDecimalGenerator(DecimalGenerator):

    def __init__(self, range_min=None, precision=None, *args, **kwargs):
        super().__init__(range_min=range_min, range_max=-1,
                         precision=precision, *args, **kwargs)


class StringGenerator(AbstractGenerator):

    max_length = 20
    def __init__(self, max_length=None, *args, **kwargs):

        if max_length is not None:
            self.max_length = max_length

        super().__init__(*args, **kwargs)

    def generate(self):
        str_length = random.randint(1, self.max_length)
        value = u''

        for i in range(str_length):
            value += random.choice(string.ascii_letters + u' ')

        return value


class DateTimeGenerator(AbstractGenerator):

    def __init__(self, min_date=None, max_date=None, *args, **kwargs):
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
        timestamp = random.randint(round(self.min_date.timestamp()),
                                   round(self.max_date.timestamp()))

        return datetime.datetime.fromtimestamp(timestamp)


class DateGenerator(DateTimeGenerator):

    def __init__(self, min_date=None, max_date=None, *args, **kwargs):
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
        return super().generate().date()


class TimeGenerator(AbstractGenerator):

    def __init__(self,  *args, **kwargs):
        super().__init__(*args, **kwargs)

    def generate(self):
        hour = random.randint(0, 23)
        minute = random.randint(0, 59)
        second = random.randint(0, 59)

        return datetime.time(hour, minute, second)


class EmailGenerator(StringGenerator):

    def __init__(self,  *args, **kwargs):
        super().__init__(*args, **kwargs)

    def generate(self):
        return "%s@%s.com" % (super().generate(), super().generate())


class UrlGenerator(StringGenerator):

    def __init__(self,  *args, **kwargs):
        super().__init__(*args, **kwargs)

    def generate(self):
        return "http://%s.com" % super().generate()


class IpAddressGenerator(AbstractGenerator):

    def __init__(self,  *args, **kwargs):
        super().__init__(*args, **kwargs)

    def generate(self):
        return '.'.join(str(part) for part in [
            PositiveIntegerGenerator(max_range=255).generate(),
            PositiveIntegerGenerator(max_range=255).generate(),
            PositiveIntegerGenerator(max_range=255).generate(),
            PositiveIntegerGenerator(max_range=255).generate()
        ])


class UuidGenerator(AbstractGenerator):

    def __init__(self,  *args, **kwargs):
        super().__init__(*args, **kwargs)

    def generate(self):
        return uuid.uuid4()
