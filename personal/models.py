from django.db import models

class source(models.Model):
    valuesV = models.CharField(max_length = 50)
    valuesI = models.CharField(max_length = 50)
    valuesP = models.CharField(max_length = 50)

class node1(models.Model):
    value1V = models.CharField(max_length = 50)
    value1I = models.CharField(max_length = 50)
    value1P = models.CharField(max_length = 50)

class node2(models.Model):
    value2V = models.CharField(max_length = 50)
    value2I = models.CharField(max_length = 50)
    value2P = models.CharField(max_length = 50)

class node3(models.Model):
    value3V = models.CharField(max_length = 50)
    value3I = models.CharField(max_length = 50)
    value3P = models.CharField(max_length = 50)
