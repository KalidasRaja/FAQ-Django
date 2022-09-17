from django.views.generic import ListView
from django.shortcuts import render

from .models import Category, Faq_QA


class ListCourse(ListView):
    # model = Course
    template_name = 'index.html'
    context_object_name = 'courses'


def detail(request):
    dd = Category.objects.all()
    fee = Faq_QA.objects.all()
    context = {
        'cc_dd': dd,
        'fees': fee,
    }
    return render(request, 'detail.html', context)
