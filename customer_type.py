from enum import Enum


class CustomerType(Enum):
    PAY_AS_YOU_GO: 1
    UNLIMITED: 0

    @classmethod
    def iter_enum(self):
        for data in CustomerType:
            print(data.name, data.value)

iter_enum()