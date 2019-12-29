from django.db import models

# Create your models here.

class UserInfo(models.Model):
    user_name      = models.CharField(max_length=30, unique=True)
    user_type      = models.CharField(max_length=10)
    user_full_name = models.CharField(max_length=80)
    user_email     = models.CharField(max_length=80, unique=True)
    user_password  = models.CharField(max_length=150)
    user_mobile    = models.CharField(max_length=15)
    created_date   = models.DateTimeField(auto_now_add=True)   
    status         = models.BooleanField(default=True)

    def __str__(self):
        return self.user_name

    class Meta:
        verbose_name = "User List"
        verbose_name_plural = "User Lists"

class DistributorInfo(models.Model):
    distributor_name = models.CharField(max_length=35)
    distibu_type = (
        ('Distributor', 'Distributor'),
        ('Supermarkets', 'Supermarkets'),
        ('Food & Restaurent', 'Food & Restaurent'),
    )
    distributor_type = models.CharField(max_length=20, choices=distibu_type) 
    address          = models.CharField(max_length=200)  
    status           = models.BooleanField(default=True)

    def __str__(self):
        return str(self.distributor_name)

    class Meta:
        verbose_name = "Distributor Information"
        verbose_name_plural = "Distributor Informations"

class InspectionInfo(models.Model):
    user_name        = models.ForeignKey(UserInfo, on_delete = models.CASCADE)
    serial_number    = models.BigIntegerField(default=0)
    action_taken     = models.CharField(max_length=30, blank=True, null=True)
    distributor_name = models.ForeignKey(DistributorInfo, on_delete = models.CASCADE)
    option_one       = models.BooleanField(default=False) #1.There are other products in the same door
    option_one_img   = models.ImageField(upload_to ='inspection_img', blank=True)
    option_two       = models.BooleanField(default=False) #2.There is no sticker on the door
    option_two_img   = models.ImageField(upload_to ='inspection_img', blank=True)
    option_three     = models.BooleanField(default=False) #3.The temperature of the refrigerato
    option_three_img = models.ImageField(upload_to ='inspection_img', blank=True)
    option_four      = models.BooleanField(default=False) #4.Competitor product
    option_four_img  = models.ImageField(upload_to ='inspection_img', blank=True)
    option_five      = models.BooleanField(default=False) #5.Product expiry date
    option_five_img  = models.ImageField(upload_to ='inspection_img', blank=True)
    option_six       = models.BooleanField(default=False) #6.Product out of Freezer
    option_six_img   = models.ImageField(upload_to ='inspection_img', blank=True)
    fine_amount      = models.FloatField(default=0)
    issue_warning    = models.CharField(max_length=30, blank=True, null=True)
    inspection_date  = models.DateTimeField(auto_now_add=False)   
    inserted_date    = models.DateTimeField(auto_now_add=True)   
    status           = models.BooleanField(default=True)

    def __str__(self):
        return str(self.user_name)

    class Meta:
        verbose_name = "Inspection Information"
        verbose_name_plural = "Inspection Informations"
