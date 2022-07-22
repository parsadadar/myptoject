from django.db import models


class category(models.Model):
    id = models.IntegerField(primary_key=True, unique=True, verbose_name='کد اصلی دست بندی')
    name = models.CharField(max_length=50, verbose_name='نام اصلی دست بندی')


class subcategory(models.Model):
    id = models.IntegerField(primary_key=True, unique=True, verbose_name='کد اصلی زیر دست بندی')
    name = models.CharField(max_length=50, verbose_name='نام اصلی زیر دست بندی')
    parent = models.ForeignKey(category, on_delete=models.CASCADE, verbose_name='دست بندی')


class product(models.Model):
    id = models.IntegerField(primary_key=Tre, unique=True, verbose_name="کد محصول")
    name = models.CharField(max_length=50, verbose_name="نام محصول")
    count = models.SmallIntegerField(verbose_name="تعداد")
    images = models.ImageField(path_to="", upload_to='/', verbose_name='عکس محصول')
    amount = models.IntegerField(verbose_name='قیمت محصول')
    conten = models.IntegerField(verbose_name='توضیحات')
    is_active = models.BooleanField(default=True, blank=True, null=False, verbose_name='کالا موجود است')
    is_deleted = models.BooleanField(default=False, blank=True, null=False, verbose_name='کالا موجود نیست')
    categories = models.OneToOneField(subcategory, on_delete=models.SET_NULL, null=True, verbose_name='دست بندی')