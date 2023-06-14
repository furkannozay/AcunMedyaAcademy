# Generated by Django 4.2.2 on 2023-06-14 12:14

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_periodmodel_rename_departmentmodel_coursesmodel_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseCategoriesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='course_categories_images/')),
            ],
        ),
        migrations.AlterField(
            model_name='coursesmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='lesson_images/'),
        ),
        migrations.AddField(
            model_name='coursesmodel',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='account.coursecategoriesmodel'),
        ),
    ]
