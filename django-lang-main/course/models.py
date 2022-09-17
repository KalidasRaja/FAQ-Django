from django.db import models
from parler.models import TranslatableModel, TranslatedFields


class Category (TranslatableModel):
    translations = TranslatedFields(
        category_Title=models.CharField(max_length=500)
    )

    def __str__(self):
        return self.category_Title


class Faq_QA(TranslatableModel):
    translations = TranslatedFields(
        question_Title=models.CharField(max_length=500),
        question_Description=models.TextField(),
        category_Option=models.ForeignKey(Category, on_delete=models.CASCADE),
        SEO_Keywords=models.TextField(),
    )

    def __str__(self):
        return self.question_Title

