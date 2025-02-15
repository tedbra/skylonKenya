from django.db import models

# Create your models here.

class Job(models.Model):
    title = models.CharField(max_length=200, null=True) 
    location = models.CharField(max_length=200, null=True, blank=True)
    position = models.CharField(max_length=200, null=True, blank=True)
    responsibilities = models.TextField(blank=True)
    Requirements = models.TextField(blank=True)
    Benefits = models.TextField(blank=True)
    footmessage = models.TextField(blank=True)

    date_added = models.DateTimeField(auto_now_add=True, null=True)
    jobID = models.CharField(max_length=14, null=True, blank=True, verbose_name='Job ID')
    
    def __str__(self):
        return self.title + ' | ' + str(self.date_added)
    
    def save(self, *args, **kwargs):

        current_date = datetime.now()
        if self.jobID:
            print('ID OF Job Already Exist = ' + self.jobID)
        else:
            date_de_merde = str(current_date)
            self.jobID = 'SKYLON'+ date_de_merde[2:4] + str(self.id).zfill(4)
            print('********* THE FOREIGN ID IS : ' + str(self.id))
            print("Why is it going here when there is data in payment history")

        super(Job, self).save(*args, **kwargs)