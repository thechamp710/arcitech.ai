# Generated by Django 5.0.4 on 2024-06-27 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_remove_blog_id_blog_content_id_blog_created_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='content_id',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='blog',
            name='id',
            field=models.BigAutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=500),
        ),
    ]
