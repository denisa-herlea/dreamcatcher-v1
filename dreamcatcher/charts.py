# Define the abstract creator class
from django.db.models import Avg
from django.db.models.functions import TruncDate
from django.shortcuts import render

from .models import Dream


class ChartCreator:
    def create_chart(self, request):
        pass


class StressChartCreator(ChartCreator):
    def create_chart(self, request):
        user = request.user.username
        data = Dream.objects.filter(user=user).annotate(date=TruncDate('created')).values('created').annotate(
            stres=Avg('stres')).order_by('created')
        stress_data = []
        date_labels = []
        for item in data:
            stress_data.append(float(item['stres']))
            date_labels.append(item['created'].strftime('%Y-%m-%d'))

        chart_data = {
            'labels': date_labels,
            'datasets': [{
                'label': 'Stress Chart',
                'data': stress_data,
                'fill': 'false',
                'borderColor': 'rgb(0, 0, 0)',
                'lineTension': 0.1
            }]
        }
        return render(request, 'stres_chart.html', {'chart_data': chart_data})


class EnergyChartCreator(ChartCreator):
    def create_chart(self, request):
        user = request.user.username
        data = Dream.objects.filter(user=user).annotate(date=TruncDate('created')).values('created').annotate(
            nivelEnergie=Avg('nivelEnergie')).order_by('created')
        energy_data = []
        date_labels = []
        for item in data:
            energy_data.append(float(item['nivelEnergie']))
            date_labels.append(item['created'].strftime('%Y-%m-%d'))

        chart_data = {
            'labels': date_labels,
            'datasets': [{
                'label': 'Energy Chart',
                'data': energy_data,
                'fill': 'false',
                'borderColor': 'rgb(0, 0, 0)',
                'lineTension': 0.1
            }]
        }
        return render(request, 'energy_chart.html', {'chart_data': chart_data})


class DurationChartCreator(ChartCreator):
    def create_chart(self, request):
        user = request.user.username
        data = Dream.objects.filter(user=user).annotate(date=TruncDate('created')).values('created').annotate(
            durata=Avg('durata')).order_by('created')
        durata_data = []
        date_labels = []
        for item in data:
            durata_data.append(float(item['durata']))
            date_labels.append(item['created'].strftime('%Y-%m-%d'))

        chart_data = {
            'labels': date_labels,
            'datasets': [{
                'label': 'Period Chart',
                'data': durata_data,
                'fill': 'false',
                'borderColor': 'rgb(0, 0, 0)',
                'lineTension': 0.1
            }]
        }
        return render(request, 'durata_chart.html', {'chart_data': chart_data})
