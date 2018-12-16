from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import requests
from ruamel.yaml import YAML
import re

class Topic(models.Model):
    name = models.SlugField(help_text='slug', unique=True)
    full_name = models.CharField(max_length=50, blank=True)
    icon = models.URLField(blank=True)
    short_description = models.CharField(blank=True, max_length=200)
    related = models.CharField(max_length=100, blank=True)
    description = models.TextField(max_length=500, blank=True)
    url = models.URLField(blank=True)
    wikipedia_url = models.URLField(blank=True)

    class Meta:
        verbose_name_plural = "Topic"
        verbose_name = "Topics"

    def __str__(self):
        return self.full_name

    def save(self, force_insert=False, force_update=False, using=None):
        full_name = self.full_name
        if not Topic.objects.filter(full_name=full_name).exists():
            url = 'https://raw.githubusercontent.com/github/explore/master/topics/' + self.name + '/index.md'
            response = requests.get(url=url)
            if(response.status_code!=404):
                yaml = YAML()
                flag = 0
                str = ''
                desc = ''
                for i in range(3, len(response.text)):
                    if (flag == 0):
                        if (response.text[i] == response.text[i + 1] == response.text[i + 2] == '-'):
                            flag = i
                        else:
                            str = str + response.text[i]

                for i in range(flag+4, len(response.text)):
                    desc = desc + response.text[i]

                data = yaml.load(str)
                self.name = data['topic']
                self.full_name = data['display_name']
                self.short_description = data['short_description']
                self.description = desc
                if 'related' in data:
                    self.related = data['related']
                if 'logo' in data:
                    self.icon = 'https://raw.githubusercontent.com/github/explore/master/topics/' + data['topic'] + '/' + data['logo']
                if 'url' in data:
                    self.url = data['url']
                if 'wikipedia_url' in data:
                    self.wikipedia_url = data['wikipedia_url']
            super(Topic, self).save()


class Repository(models.Model):
    reponame = models.CharField(max_length=70,help_text='slug', unique=True)
    name = models.SlugField()
    owner = models.SlugField()

    topics = models.ManyToManyField(Topic, related_name='repo_name')

    hasTopicTag = models.BooleanField(default=None)
    hasDocumentation = models.BooleanField(default=None)
    hasDescription = models.BooleanField(default=None)
    hasLicense = models.BooleanField(default=None)
    hasContributingGuidelines = models.BooleanField(default=None)

    commitCount = models.IntegerField(null=True, blank=True)
    prCount = models.IntegerField(null=True, blank=True)
    prMergedCount = models.IntegerField(null=True, blank=True)
    issueCount = models.IntegerField(null=True, blank=True)
    branchCount = models.IntegerField(null=True, blank=True)
    maintainersCount = models.IntegerField(null=True, blank=True)

    avgIssueResolutionTime = models.DurationField(null=True, blank=True)
    avgPRmergeTime = models.DurationField(null=True, blank=True)
    avgFirstResponseTime = models.DurationField(null=True, blank=True)

    weeklyContributorsCount = models.IntegerField(null=True, blank=True)
    firstTimeContributorsThisWeek = models.IntegerField(null=True, blank=True)
    weeklyContributorsChange = models.IntegerField(null=True, blank=True)

    contributorsList = models.TextField(null=True, blank=True)
    contributorsThisWeekList = models.TextField(null=True, blank=True)

    score = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)
    baseScore = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)
    activityScore = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)
    popularityScore = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)
    inclusivityScore = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)
    meritScore = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Repositories"
        verbose_name = "Repository"

    def __str__(self):
        return self.reponame

