from django.db import models


class Label(models.Model):
    id = models.AutoField("标签编号", primary_key=True)
    name = models.CharField("标签名称", unique=True, max_length=10)
    brief = models.CharField("标签描述", default="", max_length=64)
    date_create = models.DateTimeField("创建日期", auto_now_add=True)
    date_modify = models.DateTimeField("修改日期", null=True)
    spare1 = models.CharField("备用字段1", null=True, max_length=12)
    spare2 = models.CharField("备用字段2", null=True, max_length=12)

    def __str__(self):
        return self.name

