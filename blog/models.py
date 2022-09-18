from django.db import models
from django.contrib.auth.models import User

# Create your models here.

status = (
    ('draft', 'Draft'),
    ('published', 'Published'),
)

categories = (
    ('general', 'General'),
    ('technology', 'Technology'),
    ('celebrity', 'Celebrities'),
    ('computers', 'Computers'),
    ('educational', 'Educational'),
    ('travel', 'Travel'),
    ('kids', 'Kids'),
    ('gaming', 'Gaming'),
    ('diy', 'Diy')
)

visibility = (
    ('public', 'Public'),
    ('private', 'Private'),
)

class Post(models.Model):

    title = models.CharField(max_length=200)
    page_title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=User)
    content = models.TextField()
    category = models.CharField(choices=categories, default='general', max_length=100)
    visibility = models.CharField(max_length=100, choices=visibility, default='private')
    pub_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=250, choices=status, default='draft')

    l1 = models.CharField(max_length=150, default="")
    ext_link1 = models.CharField(max_length=100, default="")

    l2 = models.CharField(max_length=150, default="")
    ext_link2 = models.CharField(max_length=100, default="")

    l3 = models.CharField(max_length=150, default="")
    ext_link3 = models.CharField(max_length=100, default="")

    l4 = models.CharField(max_length=150, default="")
    ext_link4 = models.CharField(max_length=100, default="")

    l5 = models.CharField(max_length=150, default="")
    ext_link5 = models.CharField(max_length=100, default="")


