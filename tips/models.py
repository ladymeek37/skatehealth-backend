from django.db import models
from authentication.models import User

# Create your models here.



# lets us explicitly set upload path and filename
def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)



class Tip(models.Model):

    category_choices = (
        (1, "Yoga/Stretching"),
        (2, "Diet/Nutrition"),
        (3, "Lifestyle/Other"),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    text = models.TextField()
    link = models.CharField(max_length=200, blank = True)
    image_url = models.ImageField(upload_to=upload_to, blank=True)
    favorite_count = models.IntegerField(default="0")
    date = models.DateField()
    category = models.IntegerField(choices=category_choices, blank=True, null=True)

    def get_category_display(self):
        for choice in self.category_choices:
            if choice[0] == self.category:
                return choice[1]