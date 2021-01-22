from django.db import models

# Create your models here.
class Item(models.Model):
    item_name=models.CharField(max_length=20)
    item_image = models.ImageField(upload_to='images', blank=True)

    def __str__(self):
        return self.item_name


class SubItem(models.Model):

    item= models.ForeignKey(
        Item, on_delete=models.CASCADE,related_name='children',
    )
    sub_item_name=models.CharField(max_length=20)
    sub_item_image= models.ImageField(upload_to='images', blank=True)
    dry_wash_price=models.IntegerField()
    steam_wash_price=models.IntegerField()
    dry_iron_price=models.IntegerField()
    steam_iron_price=models.IntegerField()

