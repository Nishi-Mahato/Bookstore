from django.contrib import admin
from .models import Customer, Author, Publisher, Order, Book


class CustomerList(admin.ModelAdmin):
    list_display = ( 'cust_id', 'cust_name', 'email', 'phone_number' )
    list_filter = ( 'cust_name', 'email')
    search_fields = ('cust_id', 'email' )
    ordering = ['cust_id']


class AuthorList(admin.ModelAdmin):
    list_display = ( 'author_id', 'author_name')
    list_filter = ( 'author_id', 'author_name')
    search_fields = ('author_id', 'author_name' )
    ordering = ['author_id']


class PublisherList(admin.ModelAdmin):
    list_display = ( 'publisher_id', 'publisher_name', 'address')
    list_filter = ( 'publisher_name', 'address')
    search_fields = ('publisher_name','address' )
    ordering = ['publisher_id']


class OrderList(admin.ModelAdmin):
    list_display = ( 'order_id', 'date', 'cost')
    list_filter = ( 'order_id', 'cost')
    search_fields = ('order_id', 'cost')
    ordering = ['order_id']


class BookList(admin.ModelAdmin):
    list_display = ('book_id', 'name', 'price')
    list_filter = ('book_id', 'name')
    search_fields = ('book_id', 'name')
    ordering = ['book_id']


admin.site.register(Customer, CustomerList)
admin.site.register(Author, AuthorList)
admin.site.register(Publisher, PublisherList)
admin.site.register(Order, OrderList)
admin.site.register(Book, BookList)