from django.views.generic.base import View
from django.http import HttpResponse

from apps.metrics.services.metrics import metrics_collect

from .services.metrics import metrics_collect


class CollectMetricView(View):
    def get(self, request, *args, **kwargs):
        metrics = metrics_collect()
        return HttpResponse(metrics)
