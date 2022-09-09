from django.db import models
from api.user.models import User
from django.contrib.auth import get_user_model
from api.group.models import Group
from datetime import datetime
# Create your models here.
def get_deleted():
    return get_user_model().objects.get_or_create(username='Deleted User')[0]
class Post(models.Model):
	GroupId=models.ForeignKey(Group,on_delete=models.CASCADE,null=True,blank=True)
	UserID=models.ForeignKey(User,on_delete=models.CASCADE)
	Description=models.TextField(null=True)
	PostType=models.CharField(max_length=15)
	CodeBlock=models.TextField(blank=True,null=True)
	Image=models.ImageField(blank=True,null=True)
	CodeSnippet=models.TextField(blank=True,null=True)
	CodeLanguage=models.CharField(max_length=15)
	Created_at=models.DateTimeField(null=False)

	class Meta:
		ordering=['-Created_at']

class LikePost(models.Model):
	UserID=models.ForeignKey(User,on_delete=models.SET(get_deleted))
	PostID=models.ForeignKey(Post,on_delete=models.CASCADE)
	Created_at=models.DateTimeField(null=False)
class CommentPost(models.Model):
	PostID=models.ForeignKey(Post,on_delete=models.CASCADE)
	UserID=models.ForeignKey(User,on_delete=models.SET(get_deleted))
	ReplyID=models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True,related_name='replyid')
	Content=models.TextField(null=False)
	isAReply=models.BooleanField(default=False)
	Vote=models.PositiveIntegerField(default=0)
class ForkedPost(models.Model):
	UserID=models.ForeignKey(User,on_delete=models.CASCADE)
	PostID=models.ForeignKey(Post,on_delete=models.CASCADE)
	Description=models.TextField(null=True)
	Created_at=models.DateTimeField(null=False)
class PullRequest(models.Model):
	ForkID=models.ForeignKey(ForkedPost,on_delete=models.CASCADE)
	ToUserID=models.ForeignKey(User,on_delete=models.CASCADE,related_name='toUser')
	FromUserID=models.ForeignKey(User,on_delete=models.CASCADE,related_name='fromUser')
	PRstatus=models.BooleanField(null=True,default=None)

