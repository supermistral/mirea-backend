import json, base64
from io import BytesIO
from typing import Any, Dict, List, Optional, Tuple

from django.conf import settings

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.axes import Axes
from matplotlib.figure import Figure
from PIL import Image

from .utils import get_filename_from_fields, datetime_parser


class GraphBuilder:
    """
    Base graphics builder using the ``matplotlib`` module. The builder contains methods
    of creating various types of charts that must be implemented in child classes
    """
    json_filename: Optional[str] = None

    _plots: Dict[str, Tuple[Figure, Axes]] = {}
    _data: List[Dict[str, Any]] = []

    def __init__(self, from_json: bool = False, json_filename: Optional[str] = None,
                 data: Optional[Dict[str, Any]] = None):
        if from_json:
            self._data = self.read_json(json_filename)
            assert self._data is not None
        elif data is not None:
            self.set_data(data)

    def _get_builder_methods_names(self) -> List[str]:
        return [x for x in dir(self)
                if x.startswith('create_') and callable(getattr(self, x))]

    def _get_plots_names(self) -> List[str]:
        return [x.replace('create_', '') for x in self._get_builder_methods_names()]

    def read_json(self, filename: Optional[str] = None) -> Optional[List[Dict[str, Any]]]:
        json_filename = get_filename_from_fields(filename, self.json_filename)
        path = settings.STATS_FAKE_ROOT / json_filename

        if not path.is_file():
            return None

        with open(path, 'r', encoding='utf-8') as f:
            result = json.load(f, object_hook=datetime_parser)

        return result

    def set_data(self, data: List[Dict[str, Any]]) -> None:
        self._data = data

    def get_data(self) -> List[Dict[str, Any]]:
        return self._data

    def save(self) -> None:
        path = settings.STATS_MEDIA_ROOT
        path.mkdir(parents=True, exist_ok=True)

        for name, (fig, _) in self._plots.items():
            fig.savefig(path / (name + '.png'))

    def to_base64(self) -> List[str]:
        encoded_plots = []

        for name in sorted(self._plots.keys()):
            fig, _ = self._plots[name]
            bytes_io = BytesIO()
            fig.savefig(bytes_io, format='png')
            encoded_plots.append(base64.b64encode(bytes_io.getvalue()).decode('utf8'))

        return encoded_plots

    def build(self) -> None:
        plots_names = self._get_plots_names()

        for name in plots_names:
            self._plots[name] = plt.subplots(figsize=(8, 8))

        builder_methods = [getattr(self, x) for x in self._get_builder_methods_names()]
        plots_names = self._get_plots_names()

        for name, build_method in zip(plots_names, builder_methods):
            build_method(self._plots[name][1])

        self.add_watermark([fig for fig, _ in self._plots.values()])

    def add_watermark(self, figs: List[Figure]) -> None:
        watermark = Image.open(settings.STATS_WATERMARK_ROOT)
        watermark_size = (70, 70)
        watermark.thumbnail(watermark_size, Image.LANCZOS)      # Resizing

        offset = 100

        for fig in figs:
            fig_size = fig.get_size_inches() * fig.dpi
            fig.figimage(
                watermark,
                fig_size[0] - watermark_size[0] - offset,
                offset,
                zorder=1,
                alpha=.3
            )

    def create_plot(self, ax: Axes) -> None:
        raise NotImplementedError()

    def create_bar(self, ax: Axes) -> None:
        raise NotImplementedError()

    def create_pie(self, ax: Axes) -> None:
        raise NotImplementedError()


class CustomerOrderGraphBuilder(GraphBuilder):
    json_filename = 'customers.json'

    def create_plot(self, ax: Axes) -> None:
        dates = [x['date'] for x in self._data]
        unique_dates = sorted(set(dates), key=lambda t: t.strftime('%Y/%m/%d %H:%M:%S'))
        dates_amounts = [dates.count(x) for x in unique_dates]

        ax.plot(unique_dates, dates_amounts)
        ax.set_ylabel('Кол-во заказов')
        ax.set_title('Кол-во заказов по датам в течение 1 мес.')
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%y'))

        for label in ax.get_xticklabels():
            label.set(rotation=30, horizontalalignment='right')

    def create_bar(self, ax: Axes) -> None:

        def calculate_price_amount(p1: int, p2: int) -> int:
            return len([x for x in self._data
                        if x['total_price'] >= p1 and x['total_price'] < p2])

        price_500 = calculate_price_amount(0, 500)
        price_500_1000 = calculate_price_amount(500, 1000)
        price_1000_3000 = calculate_price_amount(1000, 3000)
        price_3000_10000 = calculate_price_amount(3000, 10000)
        price_10000_100000 = calculate_price_amount(10000, 100000)
        prices_labels = ['<500', '500-1000', '1000-3000', '3000-10000', '10000-20000']
        prices = [price_500, price_500_1000, price_1000_3000, price_3000_10000, price_10000_100000]

        ax.bar(prices_labels, prices)
        ax.set_xlabel('Сумма заказа')
        ax.set_ylabel('Кол-во заказов')
        ax.set_title('Кол-во заказов по суммам')

    def create_pie(self, ax: Axes) -> None:
        regions = [x['region'] for x in self._data]
        unique_regions = list(set(regions))
        regions_amounts = [regions.count(x) for x in unique_regions]

        ax.pie(regions_amounts, labels=unique_regions, autopct='%1.1f%%')
        ax.set_title('Кол-во заказов по регионам')
