# Generated by Django 3.2.5 on 2022-09-01 09:42

from django.db import migrations, models
import django.db.models.deletion
import parler.fields
import parler.models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_auto_20210729_1801'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course_detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'abstract': False,
            },
            bases = (parler.models.TranslatableModel, models.Model),
        ),
        migrations.CreateModel(
            name='Course_detailTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('cc_title', models.CharField(max_length=90)),
                ('cc_description', models.TextField()),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='course.course_detail')),
            ],
            options={
                'verbose_name': 'course_detail Translation',
                'db_table': 'course_course_detail_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases = (parler.models.TranslatableModel, models.Model),
        ),
    ]
