from django.db import models


# Create your models here.


class Brand(models.Model):

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, blank=False)
    brand_logo = models.ImageField(null=True, blank=False)
    side_banner = models.ImageField(null=True, blank=True)
    website = models.URLField(max_length=1024, null=True, blank=False)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Brands'

    def __str__(self):
        return self.friendly_name

    """ def get_friendly_name(self):
        return self.friendly_name """


class Memory(models.Model):

    class Meta:
        verbose_name_plural = 'Memorys'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class KeyFeatures(models.Model):

    class Meta:
        verbose_name_plural = 'Key Features'

    name = models.CharField(default='ProductCategory Features', max_length=254)

    feature_for = models.CharField(max_length=254, null=True, blank=False, default='Motherboard, Graphic Card etc.')
    feature_1_name = models.ForeignKey('Feature', related_name='feature_1_names', null=True, blank=False, on_delete=models.SET_NULL)
    feature_1 = models.CharField(max_length=254, blank=False)
    feature_2_name = models.ForeignKey('Feature', related_name='feature_2_names', null=True, blank=True, on_delete=models.SET_NULL)
    feature_2 = models.CharField(max_length=254, blank=True)
    feature_3_name = models.ForeignKey('Feature', related_name='feature_3_names', null=True, blank=True, on_delete=models.SET_NULL)
    feature_3 = models.CharField(max_length=254, blank=True)
    feature_4_name = models.ForeignKey('Feature', related_name='feature_4_names', null=True, blank=True, on_delete=models.SET_NULL)
    feature_4 = models.CharField(max_length=254, blank=True)
    feature_5_name = models.ForeignKey('Feature', related_name='feature_5_names', null=True, blank=True, on_delete=models.SET_NULL)
    feature_5 = models.CharField(max_length=254, blank=True)

    def __str__(self):
        return self.feature_for



class Feature(models.Model):

    class Meta:
        verbose_name_plural = 'Features'

    name = models.CharField(default='FeatureName', max_length=254)

    def __str__(self):
        return self.name
