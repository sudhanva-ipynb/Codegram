from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Post)
admin.site.register(models.CommentPost)
admin.site.register(models.LikePost)
admin.site.register(models.ForkedPost)
admin.site.register(models.PullRequest)
