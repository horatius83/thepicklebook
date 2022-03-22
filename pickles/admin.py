from django.contrib import admin

from .models import Pickle, Rating, Tag, PickleTag, Review, PickleMaker

admin.site.register(Pickle)
admin.site.register(Rating)
admin.site.register(Tag)
admin.site.register(PickleTag)
admin.site.register(Review)
admin.site.register(PickleMaker)