# Generated by Django 4.2.2 on 2023-06-15 19:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_alter_coursesmodel_options'),
        ('account', '0005_userlinksmodel_remove_customusermodel_birth_date_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='studentmodel',
            options={'verbose_name': 'Öğrenci', 'verbose_name_plural': 'Öğrenciler'},
        ),
        migrations.AddField(
            model_name='rolesmodel',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='rolesmodel',
            name='updated_on',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='studentmodel',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='studentmodel',
            name='updated_on',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='customusermodel',
            name='groups',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='users', to='account.rolesmodel', verbose_name='Rol'),
        ),
        migrations.AlterField(
            model_name='studentmodel',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='student_profile', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterModelTable(
            name='studentmodel',
            table='students',
        ),
        migrations.CreateModel(
            name='InstructorModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_on', models.DateTimeField(auto_now=True, null=True)),
                ('courses', models.ManyToManyField(blank=True, to='courses.coursesmodel')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='instructor_profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
