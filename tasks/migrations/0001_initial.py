# Generated by Django 3.0 on 2019-12-28 22:53

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_due', models.DateField(blank=True, null=True)),
                ('order', models.IntegerField(default=0)),
                ('points', models.IntegerField(default=0)),
                ('priority', models.IntegerField(default=0)),
                ('status', models.IntegerField(choices=[(0, 'New'), (1, 'In Progress'), (2, 'On Hold'), (3, 'Completed')], default=0)),
                ('title', models.CharField(max_length=200)),
                ('_progress', models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('assigned_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='delegated', to=settings.AUTH_USER_MODEL)),
                ('assigned_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('sub_tasks', models.ManyToManyField(blank=True, related_name='_task_sub_tasks_+', to='tasks.Task')),
            ],
        ),
        migrations.CreateModel(
            name='TaskComments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateField(auto_now_add=True)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task_comments', to=settings.AUTH_USER_MODEL)),
                ('sub_comments', models.ManyToManyField(related_name='_taskcomments_sub_comments_+', to='tasks.TaskComments')),
            ],
            options={
                'verbose_name_plural': 'Task Comments',
            },
        ),
        migrations.CreateModel(
            name='TaskCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(default=0)),
                ('title', models.TextField()),
                ('tasks', models.ManyToManyField(to='tasks.Task')),
            ],
            options={
                'verbose_name_plural': 'Task Categories',
            },
        ),
    ]
