from django.contrib import admin

# Register your models here.
from .models import RankingBoard         # add this line
admin.site.register(RankingBoard)          # add this line