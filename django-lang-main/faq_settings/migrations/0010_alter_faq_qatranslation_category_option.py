# Generated by Django 3.2.5 on 2022-09-19 05:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('faq_settings', '0009_alter_faq_qatranslation_category_option'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq_qatranslation',
            name='category_Option',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='faq_settings.category'),
        ),
    ]
