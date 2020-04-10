from django.db import models


class Page(models.Model):
    menu_title = models.CharField(max_length=200,blank=True)
    page_title = models.CharField(max_length=200,blank=True,null=True)


    def get_absolute_url(self):
        return self.page_title

class SubMenu(models.Model):
    sub_menu = models.ForeignKey(Page, on_delete=models.CASCADE,related_name="childr")
    menu_title = models.CharField(max_length=15,blank=True,null=True)
    page_title = models.CharField(max_length=200)

    def __str__(self):
        return '{}'.format(self.menu_title)