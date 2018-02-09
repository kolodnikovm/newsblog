# Generated by Django 2.0 on 2018-02-09 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publishednews',
            name='id',
        ),
        migrations.AlterField(
            model_name='publishednews',
            name='draft_news',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='news.News'),
            preserve_default=False,
        ),
    ]
