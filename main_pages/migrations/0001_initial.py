# Generated by Django 5.1.1 on 2024-09-13 15:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(max_length=250, verbose_name='Имя категории')),
                ('cat_slug', models.SlugField(max_length=250, verbose_name='Путь до категории')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='SubInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cooking_time', models.TimeField(verbose_name='Время готовки')),
                ('difficulties', models.CharField(choices=[('E', 'Легко'), ('M', 'Продвинутый'), ('H', 'Сложно')], max_length=1, verbose_name='сложности готовки')),
            ],
            options={
                'verbose_name': 'Дополнительная информация',
                'verbose_name_plural': 'Дополнительная информация',
            },
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=250, verbose_name='Имя тега')),
                ('tag_slug', models.SlugField(max_length=250, verbose_name='Путь до тега')),
            ],
            options={
                'verbose_name': 'Тег',
                'verbose_name_plural': 'Теги',
            },
        ),
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('short_description', models.TextField(default='Нету короткого описания', verbose_name='Короткое описание')),
                ('full_description', models.TextField(default='Нету полного описания', verbose_name='Полное описание')),
                ('views', models.IntegerField(default=0, verbose_name='Просмотры')),
                ('count_like', models.IntegerField(default=0, verbose_name='Количество понравившихся')),
                ('count_dislike', models.IntegerField(default=0, verbose_name='Количество не понравившихся')),
                ('slug', models.SlugField(max_length=250, verbose_name='Путь до продукта')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main_pages.categories', verbose_name='Категория')),
                ('tags', models.ManyToManyField(to='main_pages.tags', verbose_name='Теги')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_comment', models.TextField(verbose_name='Текст комментария')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_pages.articles', verbose_name='Статья')),
                ('auth', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main_pages.comments', verbose_name='Ответ на комментарий')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
        migrations.CreateModel(
            name='FavoriteUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_pages.articles', verbose_name='Статья')),
                ('auth', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Фаворит',
                'verbose_name_plural': 'Фавориты',
            },
        ),
        migrations.CreateModel(
            name='GalleryArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='gallery/articles/', verbose_name='Изображения')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image_article', to='main_pages.articles', verbose_name='Статья')),
            ],
            options={
                'verbose_name': 'Галерея',
                'verbose_name_plural': 'Галерея',
            },
        ),
        migrations.CreateModel(
            name='LikeSystem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_like', models.BooleanField(default=False, verbose_name='Понравившихся')),
                ('status_dislike', models.BooleanField(default=False, verbose_name='Не понравившихся')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_pages.articles', verbose_name='Статья')),
                ('auth', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Фаворит',
                'verbose_name_plural': 'Фавориты',
            },
        ),
        migrations.CreateModel(
            name='RatingArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating_number', models.IntegerField(default=0, verbose_name='Оценка')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_pages.articles', verbose_name='Статья')),
                ('auth', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Фаворит',
                'verbose_name_plural': 'Фавориты',
            },
        ),
        migrations.CreateModel(
            name='StepRecipes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_step', models.CharField(max_length=250, verbose_name='Названия шага')),
                ('ingredient', models.CharField(max_length=250, verbose_name='Названия ингредиента')),
                ('unit_measurement', models.CharField(max_length=250, verbose_name='Единица измерения')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='step_recipes', to='main_pages.articles', verbose_name='Статья')),
            ],
            options={
                'verbose_name': 'Пошаговая инструкция',
                'verbose_name_plural': 'Пошаговая инструкция',
            },
        ),
    ]