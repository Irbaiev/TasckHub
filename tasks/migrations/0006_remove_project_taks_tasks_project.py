# Generated by Django 4.2.6 on 2023-11-04 10:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_remove_tasks_project_project_content_project_taks_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='taks',
        ),
        migrations.AddField(
            model_name='tasks',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tasks.project'),
        ),
    ]