import json
from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple

from django.conf import settings
from faker import Faker

from .utils import get_filename_from_fields

Faker.seed(0)


class FakeGenerator:
    """
    Base fake data generator using the ``faker`` module
    """
    fake: Faker
    properties: Dict[str, Sequence[Any]]
    json_filename: Optional[str] = None

    _data: Dict[str, Tuple[Callable, Sequence[Any], Dict[str, Any]]] = {}

    def __init__(self):
        for prop_name in self.properties:
            fake_prop, *args = self.properties[prop_name]

            if len(args) > 0 and isinstance(args[-1], dict):
                kwargs = args.pop()
            else:
                kwargs = {}

            fake_method = getattr(self.fake, fake_prop)
            self._data[prop_name] = ((fake_method, args, kwargs))

    def _generate_dict(self) -> Dict[str, Any]:
        result = {}
        for prop_name, prop_args in self._data.items():
            method, args, kwargs = prop_args
            result[prop_name] = method(*args, **kwargs)
        return result

    def generate_dict(self, amount: int = 1) -> List[Dict[str, Any]]:
        return [self._generate_dict() for _ in range(amount)]

    def generate_json(self, amount: int = 1,
                      filename: Optional[str] = None) -> List[Dict[str, Any]]:
        json_filename = get_filename_from_fields(filename, self.json_filename)

        path = settings.STATS_FAKE_ROOT / json_filename
        path.parent.mkdir(parents=True, exist_ok=True)

        generated_data = self.generate_dict(amount=amount)

        with open(path, 'w', encoding='utf-8') as f:
            json.dump(generated_data, f, indent=4, default=str, ensure_ascii=False)

        return generated_data


class FakeCustomerOrderGenerator(FakeGenerator):
    fake = Faker('ru_RU')
    properties = {
        'name': ('name',),
        'date_of_birth': ('date_of_birth',),
        'region': ('administrative_unit',),
        'total_price': ('random_int', 50, 20000),
        'date': ('date_between', {'start_date': '-30d', 'end_date': 'today'})
    }

    json_filename = 'customers.json'
