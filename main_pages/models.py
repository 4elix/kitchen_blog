from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User


class Categories(models.Model):
    cat_name = models.CharField(max_length=250, verbose_name='Имя категории')
    cat_slug = models.SlugField(max_length=250, verbose_name='Путь до категории')

    def __str__(self):
        return f'№{self.pk}. {self.cat_name}'

    def get_absolute_url(self):
        return reverse('show_category', kwargs={'slug_path': self.cat_slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Tags(models.Model):
    tag_name = models.CharField(max_length=250, verbose_name='Имя тега')
    tag_slug = models.SlugField(max_length=250, verbose_name='Путь до тега')

    def __str__(self):
        return f'№{self.pk}. {self.tag_name}'

    def get_absolute_url(self):
        return reverse('show_tag', kwargs={'slug_path': self.tag_slug})

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Articles(models.Model):
    title = models.CharField(max_length=250)
    short_description = models.TextField(default='Нету короткого описания', verbose_name='Короткое описание')
    full_description = models.TextField(default='Нету полного описания', verbose_name='Полное описание')
    views = models.IntegerField(default=0, verbose_name='Просмотры')
    category = models.ForeignKey(Categories, on_delete=models.PROTECT, verbose_name='Категория')
    count_like = models.IntegerField(default=0, verbose_name='Количество понравившихся')
    count_dislike = models.IntegerField(default=0, verbose_name='Количество не понравившихся')
    tags = models.ManyToManyField(Tags, verbose_name='Теги')
    slug = models.SlugField(max_length=250, verbose_name='Путь до продукта')

    def get_first_photo(self):
        photo = self.image_article.all().first()
        if photo is not None:
            return photo.image.url
        else:
            return 'https://images.satu.kz/126101312_w640_h640_razdel-v-razrabotketovary.jpg'

    def get_photos(self):
        try:
            photo = self.image_article.all()[1:]
            return photo
        except Exception as error:
            print(error)
            return 'not photos'

    def get_absolute_url(self):
        return reverse('product-info', kwargs={'slug_path': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class GalleryArticle(models.Model):
    article = models.ForeignKey(Articles, on_delete=models.CASCADE, related_name='image_article', verbose_name='Статья')
    image = models.ImageField(upload_to='gallery/articles/', verbose_name='Изображения')

    def __str__(self):
        return f'№{self.article.title}.'

    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галерея'


class SubInfo(models.Model):
    CHOICE_DIFFICULTIES = [
        ('E', 'Легко'),
        ('M', 'Продвинутый'),
        ('H', 'Сложно'),
    ]
    cooking_time = models.TimeField(verbose_name='Время готовки')
    difficulties = models.CharField(max_length=1, choices=CHOICE_DIFFICULTIES, verbose_name='сложности готовки')

    def __str__(self):
        return f'№{self.pk}.'

    class Meta:
        verbose_name = 'Дополнительная информация'
        verbose_name_plural = 'Дополнительная информация'


class StepRecipes(models.Model):
    article = models.ForeignKey(Articles, on_delete=models.CASCADE, related_name='step_recipes', verbose_name='Статья')
    name_step = models.CharField(max_length=250, verbose_name='Названия шага')
    ingredient = models.CharField(max_length=250, verbose_name='Названия ингредиента')
    unit_measurement = models.CharField(max_length=250, verbose_name='Единица измерения')

    def __str__(self):
        return f'№{self.pk} Шага. К какому блюду {self.article.title}'

    class Meta:
        verbose_name = 'Пошаговая инструкция'
        verbose_name_plural = 'Пошаговая инструкция'


class Comments(models.Model):
    auth = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    article = models.ForeignKey(Articles, on_delete=models.CASCADE, verbose_name='Статья')
    text_comment = models.TextField(verbose_name='Текст комментария')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True,
                               verbose_name='Ответ на комментарий')

    def __str__(self):
        return f'{self.auth} --- {self.article.title}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class FavoriteUser(models.Model):
    auth = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    article = models.ForeignKey(Articles, on_delete=models.CASCADE, verbose_name='Статья')

    def __str__(self):
        return f'{self.auth} --- {self.article.title}'

    class Meta:
        verbose_name = 'Фаворит'
        verbose_name_plural = 'Фавориты'


class RatingArticle(models.Model):
    auth = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    article = models.ForeignKey(Articles, on_delete=models.CASCADE, verbose_name='Статья')
    rating_number = models.IntegerField(default=0, verbose_name='Оценка')

    def __str__(self):
        return f'{self.auth} --- {self.article.title} --- {self.rating_number}'

    class Meta:
        verbose_name = 'Фаворит'
        verbose_name_plural = 'Фавориты'


class LikeSystem(models.Model):
    auth = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    article = models.ForeignKey(Articles, on_delete=models.CASCADE, verbose_name='Статья')
    status_like = models.BooleanField(default=False, verbose_name='Понравившихся')
    status_dislike = models.BooleanField(default=False, verbose_name='Не понравившихся')

    def __str__(self):
        return f'{self.auth} --- {self.article.title} --- {self.status_like} --- {self.status_dislike}'

    class Meta:
        verbose_name = 'Фаворит'
        verbose_name_plural = 'Фавориты'
