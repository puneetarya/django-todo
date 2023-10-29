from django.db import models

# Create your models here.
class TotalCandidates(models.Model):
    State_Name = models.TextField(max_length=50, blank=True)
    Assembly_No = models.IntegerField(blank=True)
    Year = models.IntegerField(blank=True)
    Total_Candidate = models.IntegerField(blank=True)
    Deposit_Lost = models.IntegerField(blank=True)

    class Meta:
        verbose_name_plural = 'ae_contested_deposit_losts'

    def __str__(self) -> str:
        return f'{self.Year}--{self.Total_Candidate}'