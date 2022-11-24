from django.shortcuts import render

from .utils import get_stats_images
from .graphs import CustomerOrderGraphBuilder
from .fakers import FakeCustomerOrderGenerator


def index(request):
    generate_amount = request.GET.get('generate', None)

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

    context = {
        'images': images,
        'data': data,
        'is_base64': generate_amount is not None,
    }

    return render(request, 'stats/index.html', context=context)
