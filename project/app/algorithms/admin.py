from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from app.algorithms.models import Algorithm, AlgorithmTag

class AlgorithmAdmin (ModelAdmin):
    model = Algorithm
    exclude = ('creator', 'saved_by', 'date_created', 'date_saved',)
admin.site.register(Algorithm, AlgorithmAdmin)

class AlgorithmTagAdmin (ModelAdmin):
    model = AlgorithmTag
    exclude = ('creator', 'saved_by', 'date_created', 'date_saved',)
admin.site.register(AlgorithmTag, AlgorithmTagAdmin)
