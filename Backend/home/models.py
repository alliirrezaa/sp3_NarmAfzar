from django.db import models

class faq(models.Model):
    question=models.CharField(max_length=150)
    answer=models.TextField()

    def __str__(self):
        return self.question

class Category(models.Model):
    sub_category=models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True,related_name='sub_cat')
    sub=models.BooleanField(default=False)
    name=models.CharField(max_length=200)
    create=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now=True)
    image=models.ImageField(upload_to='category',null=True,blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    category=models.ManyToManyField(Category)
    name=models.CharField(max_length=200)
    information=models.TextField(blank=True,null=True)
    extra_information=models.TextField(blank=True,null=True)
    create=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now=True)
    image=models.ImageField(upload_to='product')

    def __str__(self):
        return self.name
