from django.db import models
from repo.models import Topic
from django.contrib.auth.models import User
from .user_rating import UserMetrics


class UserTopics(models.Model):
    pass

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    username = models.SlugField(help_text='slug', unique=True)
    name = models.CharField(max_length=60, null=True, blank=True)
    avatar = models.CharField(max_length=30, null=True, blank=True)

    token = models.CharField(max_length=100, null=True, blank=True)

    daysCount = models.IntegerField(null=True, blank=True)
    prCount = models.IntegerField(null=True, blank=True)
    issueCount = models.IntegerField(null=True, blank=True)
    repoOwnCount = models.IntegerField(null=True, blank=True)

    points = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)
    basePoints = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)
    contributionPoints = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)
    activityPoints = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)
    creationPoints = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)
    communityPoints = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)


    topics = models.ManyToManyField(Topic, related_name = 'user_topics', through='UserTopic')

    def __str__(self):
        return self.username

    def save(self):
        full_name = self.name
        username = self.username
        if not Topic.objects.filter(full_name=full_name).exists():
            user = UserMetrics(username, "03e5d817f468829fd9b3307f55de055461460c1a")

            self.name = user.fullName
            self.avatar = user.userID
            self.repoCount = user.repoOwnCount

            self.points = user.userPoints
            self.basePoints = user.basePoints
            self.contributionPoints = user.contributionPoints
            self.activityPoints = user.activityPoints
            self.creationPoints = user.creationPoints
            self.communityPoints = user.communityPoints

            super(Profile, self).save()

            for topic, value in user.topicInterestDict.items():
                if Topic.objects.filter(name=topic):
                    t = Topic.objects.get(name=topic)
                else:
                    t = Topic.objects.create(name=topic)
                    t.save()

                UserTopic.objects.create(profile=self, topic=t, interest=value)

            for topic, value in user.topicSkillDict.items():
                if Topic.objects.filter(name=topic):
                    t = Topic.objects.get(name=topic)
                else:
                    t = Topic.objects.create(name=topic)
                    t.save()

                UserTopic.objects.filter(profile=self, topic=t).update(skill=value)

            super(Profile, self).save()




class UserTopic(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, verbose_name='Topic Name')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    interest = models.DecimalField(decimal_places=2, max_digits=4, null=True, blank=True)
    skill = models.DecimalField(decimal_places=2, max_digits=4, null=True, blank=True)
