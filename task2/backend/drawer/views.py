from django.shortcuts import render
from django.core.exceptions import BadRequest

from typing import Tuple


def get_svg(shape: int, size: int, scale: int = 100) -> Tuple[Tuple[float, float], str]:
    side_size = scale * size
    rect_svg_size = (side_size,) * 2

    if shape == 0:
        return rect_svg_size, f'rect width={side_size} height={side_size}'
    elif shape == 1:
        return rect_svg_size, f'polygon points="0,{side_size} {side_size},{side_size} {side_size / 2},0"'
    elif shape == 2:
        return rect_svg_size, f'circle cx="{side_size / 2}" cy="{side_size / 2}" r="{side_size / 2}"'
    return (side_size * 1.5, side_size), f'polygon points="0,{side_size} {side_size},{side_size} {side_size * 1.5},0 {side_size / 2},0"'


def index(request):
    num = request.GET.get('num', None)

    if num is None:
        raise BadRequest("'num' parameter is required")

    try:
        num = int(num)
    except Exception as e:
        raise BadRequest("Invalid value of 'num' parameter")

    get_value = lambda x, y: (num >> x) & y

    shape = get_value(8, 3)
    color_code = (get_value(6, 3), get_value(4, 3), get_value(2, 3))
    size = get_value(0, 3) + 1

    color = map(lambda x: int(x * 255 / 3), color_code)
    svg_size, svg_shape_code = get_svg(shape, size)

    return render(request, "drawer.html", {
        'shape_code': svg_shape_code,
        'color': ','.join(map(str, color)),
        'size': svg_size
    })
    