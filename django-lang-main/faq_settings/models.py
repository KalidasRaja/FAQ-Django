from django.db import models
from parler.models import TranslatableModel, TranslatedFields


class IpModel(models.Model):
    ip = models.CharField(max_length=100)

    def __str__(self):
        return self.ip


class Category (TranslatableModel):
    translations = TranslatedFields(
        category_Title=models.CharField(max_length=500)
    )

    def __str__(self):
        return self.category_Title


class Faq_QA(TranslatableModel):
    translations = TranslatedFields(
        question_Title=models.CharField(max_length=500, db_index=True),
        question_Description=models.TextField(blank=True),
        category_Option=models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True),
        SEO_Keywords=models.TextField(blank=True),
        views=models.ManyToManyField(IpModel, related_name="faq_views", blank=True)
    )

    def __str__(self):
        return self.question_Title


class User(models.Model):
    user = models.TextField(max_length='256', default=None)

    def __str__(self):
        return self.user

