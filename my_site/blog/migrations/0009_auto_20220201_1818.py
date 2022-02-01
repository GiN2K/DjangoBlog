# Generated by Django 3.1.3 on 2022-02-01 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_article_image_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='image_link',
        ),
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(default='blog/image1.jpg', upload_to=''),
        ),
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(default='', editable=False, max_length=200, unique=True),
        ),
    ]
