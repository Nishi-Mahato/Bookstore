from django.db import models
from django.utils import timezone

category = (
    ('New', 'New'),
    ('Like New', 'Like New'),
    ('Good', 'Good'),
    ('Acceptable','Acceptable')
)


# Create your models here.
class Customer(models.Model):
    cust_id = models.IntegerField(blank=False, null=False)
    cust_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)

    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.cust_id)


class Author(models.Model):
    author_id = models.IntegerField(blank=False, null=False)
    author_name = models.CharField(max_length=200, db_index=True)
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.acquired_date = timezone.now()
        self.save()

    def updated(self):
        self.recent_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.author_id)


class Publisher(models.Model):
    publisher_id = models.IntegerField(blank=False, null=False)
    publisher_name = models.CharField(max_length=200, db_index=True)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)

    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.publisher_id)


class Book(models.Model):
    book_id = models.IntegerField(blank=False, null=False)
    name = models.CharField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(blank=False, null=False)
    category = models.CharField(max_length=10, choices=category, default='New', blank=False)
    bookAuthorID = models.ForeignKey(Author, on_delete=models.CASCADE, default=None, blank=False, null=False)
    bookPublisherID = models.ForeignKey(Publisher, on_delete=models.CASCADE, default=None, blank=False, null=False)

    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.book_id)


class Order(models.Model):
    order_id = models.IntegerField(blank=False, null=False)
    date = models.DateTimeField(auto_now_add=True)
    ship_date = models.DateTimeField(auto_now_add=True)
    ship_address = models.CharField(max_length=200)
    ship_city = models.CharField(max_length=50)
    ship_state = models.CharField(max_length=50)
    ship_zipcode = models.CharField(max_length=10)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    customerID = models.ForeignKey(Customer, on_delete=models.CASCADE, default=None, blank=False, null=False)
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.order_id)
