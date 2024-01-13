from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, FormView

from .forms import AddProblemForm
from problems.models import Image, Problems


class ReportProblem(FormView):
    form_class = AddProblemForm
    template_name = 'reviewform/add_problem.html'
    success_url = reverse_lazy('success')
    extra_context = {
        'title': 'Сообщить о проблеме',
    }

    def form_valid(self, form):
        problem = form.save()
        images = form.cleaned_data["image_field"]
        if images:
            for image in images:
                Image.objects.create(problem=problem, image=image)
        return super().form_valid(form)


def success(request):
    return render(request, 'reviewform/success.html', {'title': 'Успешно'})


