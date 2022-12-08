from typing import Any, Dict, List, Optional

from .fakers import FakeCustomerOrderGenerator
from .graphs import CustomerOrderGraphBuilder
from .utils import get_stats_images


class GeneratedStatisticsData:
    def __init__(self, images: List[str], data: Optional[List[Dict[str, Any]]],
                 is_base64: bool):
        self.images = images
        self.data = data
        self.is_base64 = is_base64


def generate_initial_statistics() -> None:
    faker = FakeCustomerOrderGenerator()
    graph_builder = CustomerOrderGraphBuilder()
    data = graph_builder.read_json()

    if data is None:
        faker.generate_json(amount=50)

    images = get_stats_images()

    if data is None or len(images) == 0:
        # Use read_json() to check if the file is readable
        graph_builder.set_data(graph_builder.read_json())
        graph_builder.build()
        graph_builder.save()



def generate_statistics_by_amount(generate_amount: Any) -> GeneratedStatisticsData:
    if generate_amount is None:
        data = CustomerOrderGraphBuilder().read_json()
        images = get_stats_images()
    else:
        try:
            generate_amount = int(generate_amount)
            if generate_amount < 1 or generate_amount > 1000:
                generate_amount = 50
        except Exception:
            generate_amount = 50

        fake_generator = FakeCustomerOrderGenerator()
        data = fake_generator.generate_dict(amount=generate_amount)

        graph_builder = CustomerOrderGraphBuilder(data=data)
        graph_builder.build()
        images = graph_builder.to_base64()
    
    return GeneratedStatisticsData(
        images=images,
        data=data,
        is_base64=generate_amount is not None
    )
