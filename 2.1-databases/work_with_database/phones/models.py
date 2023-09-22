from django.db import models


class Phone(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=100)
    image = models.ImageField(upload_to='phones')
    price = models.IntegerField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(unique=True, db_index=True, verbose_name='URL')

    pass

# id, name, price, image, release_date, lte_exists и slug. Поле id — должно быть основным ключом модели.