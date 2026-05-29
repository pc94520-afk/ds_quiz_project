from django.db import models

class Question(models.Model):
    category = models.CharField(max_length=100, verbose_name="章節")
    content = models.TextField(verbose_name="題目內容")

    def __str__(self):
        return self.content

class Option(models.Model):
    question = models.ForeignKey(Question, related_name='options', on_delete=models.CASCADE)
    text = models.CharField(max_length=255, verbose_name="選項文字")
    is_correct = models.BooleanField(default=False, verbose_name="是否為正確答案")

    def __str__(self):
        return self.text