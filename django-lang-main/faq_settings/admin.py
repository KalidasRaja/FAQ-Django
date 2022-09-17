from django.contrib import admin
from parler.admin import TranslatableAdmin

from .models import Category, Faq_QA, User, IpModel

admin.site.register(Category, TranslatableAdmin)
admin.site.register(Faq_QA, TranslatableAdmin)
admin.site.register(User)
admin.site.register(IpModel)
