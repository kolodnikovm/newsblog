# Generated by Django 2.0.3 on 2018-03-13 07:10

from django.db import migrations, models
import django.db.models.deletion
import news.utilfuncs


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20180305_1952'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=20)),
                ('is_published', models.BooleanField(default=False)),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('text_content', models.TextField()),
                ('main_picture', models.ImageField(blank=True, null=True, upload_to=news.utilfuncs.main_news_pic)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='news.Author')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.Category')),
                ('tags', models.ManyToManyField(to='news.Tag')),
            ],
            options={
                'verbose_name_plural': 'news',
            },
        ),
        migrations.RemoveField(
            model_name='draftnews',
            name='author',
        ),
        migrations.RemoveField(
            model_name='draftnews',
            name='category',
        ),
        migrations.RemoveField(
            model_name='draftnews',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='publishednews',
            name='draft_news',
        ),
        migrations.RemoveField(
            model_name='extrapics',
            name='published_news',
        ),
        migrations.AlterField(
            model_name='extrapics',
            name='news',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='extra_pics', to='news.News'),
        ),
        migrations.DeleteModel(
            name='DraftNews',
        ),
        migrations.DeleteModel(
            name='PublishedNews',
        ),
    ]
