# Generated by Django 5.1.3 on 2024-12-14 17:12

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ClarificationCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clarification', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ClassificationType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Rfx',
            fields=[
                ('rfxid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Assign_To',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='General',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Due_date', models.DateField()),
                ('expires', models.DateTimeField()),
                ('assigned_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assign_to', to='taskapp.assign_to')),
                ('clarification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clarificationcategory', to='taskapp.clarificationcategory')),
                ('clarificationtype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clairifictiontype', to='taskapp.classificationtype')),
                ('rfx', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rfx', to='taskapp.classificationtype')),
            ],
        ),
        migrations.CreateModel(
            name='ClarificationFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('files', models.FileField(upload_to='file/')),
                ('general', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='general', to='taskapp.general')),
            ],
        ),
    ]
