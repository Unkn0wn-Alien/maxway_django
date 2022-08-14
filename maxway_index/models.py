from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta():
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Product(models.Model):
    category_product = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, db_index=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='media/%Y,%m,%d')
    price = models.IntegerField()
    cost = models.IntegerField(null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Customer(models.Model):
    first_name = models.CharField(null=False, blank=False,max_length=100)
    last_name = models.CharField(null=False, blank=False,max_length=100)
    phone_number = models.CharField(null=False, unique=True ,blank=False,max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Order(models.Model):
    name = models.CharField(max_length=100)
    payment_type = models.IntegerField(null=False, blank=False)
    status = models.IntegerField(null=False, blank=True, default=1)
    address = models.CharField(null=False, blank=False, max_length=250)
    customer = models.ForeignKey(Customer, blank=True, null=True, on_delete=models.SET_NULL)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta():
        verbose_name = 'Buyurtma'
        verbose_name_plural = 'Buyurtmalar'

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.PositiveIntegerField(default=1)
    count = models.IntegerField()