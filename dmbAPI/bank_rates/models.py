from django.db import models

# Create your models here.
class BankRates(models.Model):
    """Model to key in the rates of the bank"""
    COMMERICAL = 'CM'
    HDB = 'HDB'
    PRIVATE = 'PP'

    FIXED_RATE = 'fixed_rate'
    FLOAT_RATE = 'float_rate'
    BOTH_RATE = 'both'

    PROPERTY_TYPE_CHOICES = (
        (COMMERICAL, 'Commerical'),
        (HDB, 'HDB'),
        (PRIVATE, 'Private'),
    )

    LOAN_TYPE_CHOICES = (
        (FIXED_RATE, 'Fixed Rate'),
        (FLOAT_RATE, 'Floating Rate'),
        (BOTH_RATE, 'Both'),
    )

    DBS = 'http://127.0.0.1:8000/media/bank_images/dbs_logo.jpg'
    UOB = 'http://127.0.0.1:8000/media/bank_images/uob_logo.png'
    SCT = 'http://127.0.0.1:8000/media/bank_images/uob_logo.png'
    MYB = 'http://127.0.0.1:8000/media/bank_images/maybank_logo.png'
    HLB = 'http://127.0.0.1:8000/media/bank_images/hong_leong.jpg'
    BEA = 'http://127.0.0.1:8000/media/bank_images/bea_logo.png'
    OCBC = 'http://127.0.0.1:8000/media/bank_images/ocbc_logo.png'
    POSB = 'http://127.0.0.1:8000/media/bank_images/posb_logo.png'
    RHB = 'http://127.0.0.1:8000/media/bank_images/rhb_bank.png'

    BANK_IMAGE_CHOICES = (
        (DBS, 'DBS'),
        (UOB, 'UOB'),
        (SCT, 'Standard Charter'),
        (MYB, 'Maybank'),
        (HLB, 'Hong Leong Finance'),
        (BEA, 'BEA'),
        (OCBC, 'OCBC'),
        (POSB, 'POSB'),
        (RHB, 'RHB')
    )

    bank_name = models.CharField(max_length=109, blank=False, default='')
    loan_type = models.CharField(max_length=10, choices=LOAN_TYPE_CHOICES, default=FIXED_RATE)
    property_type = models.CharField(max_length=2, choices=PROPERTY_TYPE_CHOICES, default=PRIVATE)
    bank_image = models.CharField(max_length=200 , choices=BANK_IMAGE_CHOICES, default='')
    loan_tenure = models.IntegerField()
    interest_rates = models.FloatField()

    class Meta:
        ordering = ('interest_rates',)

    def __str__(self):
        return self.bank_name + "_no_of_years_" + str(self.loan_tenure) + "_interest_rates_" + str(self.interest_rates)

