import django_filters
from django_filters import CharFilter
from .models import Faq_QA


class FaqFilter(django_filters.FilterSet):
    question_Title = CharFilter(field_name='question_Title', lookup_expr='icontains')

    class Meta:
        model = Faq_QA
        fields = [
            'question_Title',
        ]
