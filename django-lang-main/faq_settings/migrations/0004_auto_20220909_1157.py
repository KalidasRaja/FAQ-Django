# Generated by Django 3.2.5 on 2022-09-09 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faq_settings', '0003_alter_faq_qatranslation_views'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq_qatranslation',
            name='question_Description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='faq_qatranslation',
            name='question_Title',
            field=models.CharField(db_index=True, max_length=500),
        ),
    ]
