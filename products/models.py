from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, default="Uncategorized")

    class Meta:
        "to custimaze the name of the model which is displayed in the admin page"

        verbose_name = "Category"
        verbose_name_plural = "Categories"

    # def __str__(self):
    #     return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    description = models.TextField()
    image = models.ImageField(upload_to="uploads/")
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="images"
    )
    category = models.CharField(max_length=50, default="Uncategorized")
    stock = models.IntegerField(default=0)

    # def __str__(self):
    #     return self.name