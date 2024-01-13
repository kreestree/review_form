from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import QuerySet
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Problems


# Create your views here.
class ProblemList(LoginRequiredMixin, ListView):
    model = Problems
    template_name = 'problems/problem_list.html'
    context_object_name = 'problems'
    ordering = '-time_create'
    extra_context = {
        'title': 'Список проблем'
    }

    def get_queryset(self) -> QuerySet:
        return Problems.objects.prefetch_related('images').order_by('-time_create')

    # paginate_by = 5


class Problem(LoginRequiredMixin, DetailView):
    model = Problems
    template_name = 'problems/problem.html'
    slug_url_kwarg = 'problem_pk'
    context_object_name = 'problem'

    def get_object(self, queryset=None):
        return get_object_or_404(Problems.objects.prefetch_related('images'), pk=self.kwargs[self.slug_url_kwarg])
