from django.db import models

class vitrina(models.Model):
    marka_piva = models.CharField(max_length=150)
    cena_piva = models.IntegerField()
    kol_piva = models.IntegerField()
    birka_piva = models.ImageField(upload_to='upload/')

    def __str__(self):
        return self.marka_piva
        return self.cena_piva
        return self.kol_piva
        return self.birka_piva







    class Meta:
        verbose_name = 'витрину'
        verbose_name_plural ='Витрины'

