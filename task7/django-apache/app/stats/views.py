from django.shortcuts import render

from . import services


def index(request):
    generate_amount = request.GET.get('generate', None)
    generated_data = services.generate_statistics_by_amount(generate_amount)

    context = {
        'images': generated_data.images,
        'data': generated_data.data,
        'is_base64': generated_data.is_base64,
    }

    return render(request, 'stats/index.html', context=context)
