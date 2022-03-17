from django.db import models
from typing import Text
# Create your models here.


# 用于存储主题
class Topic(models.Model):
    """需要存储的主题"""
    text = models.CharField(max_length=200)  # 设置最大限制
    create_date = models.DateTimeField(auto_now_add=True)  # 创建时间
    update_date = models.DateTimeField(auto_now=True)  # 修改时间

    class Meta:
        verbose_name = 'Topic'
        verbose_name_plural = verbose_name

    def __str__(self):
        """返回模型的字符串表示"""
        return self.text


class Note(models.Model):
    """记录文本"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    title = models.CharField(verbose_name='title', max_length=100)
    text = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)  # 创建时间
    update_date = models.DateTimeField(auto_now=True)  # 修改时间

    class Meta:
        verbose_name_plural = 'note'

    def __str__(self):
        return self.title


class Excerpts(models.Model):
    """记录名言警句"""
    origin = models.CharField(verbose_name='origin', max_length=100)
    text = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)  # 创建时间
    update_date = models.DateTimeField(auto_now=True)  # 修改时间

    class Meta:
        verbose_name_plural = 'origin'

    def __str__(self):
        return self.origin
