# Generated by Django 4.0.8 on 2022-10-21 06:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_contest_likes_remove_contest_saved'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContestLikes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='contest',
            name='likes',
            field=models.ManyToManyField(through='core.ContestLikes', to='core.profile'),
        ),
        migrations.AddField(
            model_name='profile',
            name='liked_contest',
            field=models.ManyToManyField(through='core.ContestLikes', to='core.contest'),
        ),
        migrations.AddField(
            model_name='contestlikes',
            name='contest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.contest'),
        ),
        migrations.AddField(
            model_name='contestlikes',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.profile'),
        ),
    ]
