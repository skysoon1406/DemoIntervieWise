from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Interview(models.Model):   # 新增一個類別 Interview  ， 繼承了 models.Model 這個類別
    company_name =  models.CharField(max_length=100,null=False)  # 預設值 就是null=False
    position =  models.CharField(max_length=50)
    interview_date = models.DateField(null=True)  #null = True 代表：  這個非必填
    review = models.TextField()
    rating = models.PositiveSmallIntegerField(default=5)
    result = models.CharField(max_length=50,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    favorited_by = models.ManyToManyField(User,through="FavoriteInterview",related_name="favorited_interviews")
    #                                                   # FavoriteInterview  這個時候還沒出現，會出錯，所以要用字串方式呈現

class Comment(models.Model):
    content = models.TextField()
    interview = models.ForeignKey(Interview,on_delete=models.SET_NULL , null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
# interviews
#     company_name
#     positon
#     interview_date
#     review
#     rating


# Join Table 
class FavoriteInterview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    interview = models.ForeignKey(Interview,on_delete=models.CASCADE)