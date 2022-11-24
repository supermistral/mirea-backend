from stats.fakers import FakeCustomerOrderGenerator
from stats.graphs import CustomerOrderGraphBuilder
from stats.utils import get_stats_images


def generate_statistics_data() -> None:
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


def main() -> None:
    generate_statistics_data()


main()
