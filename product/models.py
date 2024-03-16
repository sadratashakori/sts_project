from django.db import models

# Create your models here.
class productCategory(models.Model):
    title=models.CharField(max_length=50,verbose_name='نام دسته بندی')
    url_title=models.CharField(max_length=100,null=False,verbose_name='نام دسته بندی در آدرس')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name='دسته بندی'
        verbose_name_plural='دسته بندی ها'



class tags(models.Model):
    title=models.CharField(max_length=30,verbose_name='نام تگ')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name='تگ'
        verbose_name_plural='تگ ها'

class productModel(models.Model):
    title=models.CharField(max_length=50,verbose_name='عنوان')
    price=models.IntegerField(verbose_name='قیمت')
    off=models.IntegerField(null=True,verbose_name='تخفیف(%)')
    category=models.ForeignKey(productCategory,on_delete=models.CASCADE,verbose_name='دسته بندی')
    tag=models.ManyToManyField(tags,verbose_name='برچسب',null=True)
    des=models.TextField(max_length=200,verbose_name='توضیحات',null=True)
    is_active=models.BooleanField(default=True,verbose_name='فعال/غیرفعال')
    slug=models.SlugField(null=False,max_length=100,db_index=True,allow_unicode=True,verbose_name='اسم در آدرس')
    def __str__(self):
       return self.title

    class Meta:
        verbose_name='محصول'
        verbose_name_plural='محصولات'





