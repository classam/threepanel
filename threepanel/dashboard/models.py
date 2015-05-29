from django.db import models
from django.core.cache import cache


# Create your models here.
class SiteOptions(models.Model):
    # Basic
    title = models.CharField(max_length=100,
                             default="Cube Drone",
                             help_text="The title of your comic")
    tagline = models.CharField(max_length=200,
                               default="Code/comics, updates Tuesday & Thursday",
                               help_text="A short tagline for your comic")
    elevator_pitch = models.TextField(default="Comics about software development in a small Vancouver startup.",
                                      help_text="A Tweet-length description of your comic.")

    # Author
    author_name = models.CharField(max_length=100,
                                   default="Curtis Lassam",
                                   help_text="What's the author (or author's) names?")
    author_website = models.CharField(max_length=100,
                                      default="http://curtis.lassam.net",
                                      help_text="Does the author have a personal website?")

    # Google tracking code number
    google_tracking_code = models.CharField(max_length=50,
                                            default="UA-41279849-1")
    youtube_channel = models.CharField(max_length=150,
                                            default="http://www.youtube.com/user/IkoIkoComic/playlists")
    # Twitter
    twitter_username = models.CharField(max_length=50, default="classam")
    twitter_widget_id = models.CharField(max_length=50, default="304715092187025408")

    twitter_consumer_key = models.CharField(max_length=100, default="", help_text="Get from apps.twitter.com")
    twitter_consumer_secret = models.CharField(max_length=100, default="", help_text="Get from apps.twitter.com")
    twitter_access_key = models.CharField(max_length=100, default="", help_text="Get from apps.twitter.com")
    twitter_access_secret = models.CharField(max_length=100, default="", help_text="Get from apps.twitter.com")

    def save(self):
        super().save()
        cache.clear()

    @classmethod
    def get(cls):
        opts = SiteOptions.objects.all()
        if len(opts) > 0:
            return opts[0]
        else:
            new_options = SiteOptions()
            new_options.save()
            return new_options
