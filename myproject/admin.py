from django.contrib import admin
#from django.core.exceptions import FieldError
from rostermaker.models import Player, HOF 
from season.models import Season
from section.models import Page, Item
from photo.models import Photo
from gamemaker.models import Stat, Game, GameRosterForm

class StatInline(admin.TabularInline):
    model = Stat
    fieldsets = (
        (None, {
            'fields': (('player',),('AB','single','double','triple','HR','BB','SO','SAC','R','RBI',),)
        }),
    )
    
class GameRosterAdmin(admin.ModelAdmin):
    form = GameRosterForm
    filter_horizontal = ('players',)
    fieldsets = (
        (None, {
            'fields': (('when', 'opponent', 'location'),)
        }),
        ('Roster', {
            'classes': ('grp-collapse grp-closed',),
            'fields': ('players', 'RosterRulesOn',)
        }),
        ('Score', {
            'fields': (('scoreMPR', 'scoreOPP'),)
        }),
    )
       
    inlines = [
        StatInline,
    ]

    def save_model(self, request, obj, form, change):
        obj.save()
        form.save_m2m()
        count = obj.players.count()
        women = obj.players.filter(sex='F')
        women_count = women.count()
        if count != 0:
            women_pct = int((women_count/float(count))*100)
            self.message_user(request,"Players scheduled: %s | Women: %s percent" % (count, women_pct))
        else:
            self.message_user(request,"Players scheduled: 0 | Women: 0 percent")

        

class HOFInline(admin.TabularInline):
    model = HOF
    verbose_name = "Hall of Fame"
    verbose_name_plural = "Hall of Fame"
    can_delete = True
    fieldsets = (
        (None, {
            'fields': ('wing', 'yearEntered', 'inscription',)
        }),
    )

    class Media:
        js = [
			'/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
			'/static/grappelli/tinymce_setup/tinymce_setup.js',
		]


class PlayerAdmin(admin.ModelAdmin):
    #form = PlayerForm
    list_display = ('lastName', 'firstName', 'active', )    
    ordering = ('-active','lastName','firstName',)
    search_fields = ('lastName', 'firstName', 'alias')
    list_filter = ('active',)

    inlines = [
        HOFInline,
    ]
      

    
class SeasonAdmin(admin.ModelAdmin):
    filter_horizontal = ('roster', 'captains', 'rookies', 'mvp', 'battingchamps', 'goldengloves', 'mostimproved','whippet','bombat','walker',)
    fieldsets = (
        ('Season/Record', {
            'fields': (('year', 'wins', 'losses', 'ties'),)
        }),
        ('Recap', {
            'classes': ('collapse',),
            'fields': ('recap',),
        }),
        ('Roster', {
            'classes': ('collapse',),
            'fields': ('roster',),
        }),
        ('Captains',  {
            'classes': ('collapse',),
            'fields': ('captains',),
        }),
        ('Rookie(s) of the Year',  {
            'classes': ('collapse',),
            'fields': ('rookies',),
        }),
        ('Most Valuable Player(s)',  {
            'classes': ('collapse',),
            'fields': ('mvp',),
        }),
        ('Batting Champs',  {
            'classes': ('collapse',),
            'fields': ('battingchamps',),
        }),
        ('Golden Glove(s)',  {
            'classes': ('collapse',),
            'fields': ('goldengloves',),
        }),
        ('Most Improved',  {
            'classes': ('collapse',),
            'fields': ('mostimproved',),
        }),
        ('Whippet(s) of the Year',  {
            'classes': ('collapse',),
            'fields': ('whippet',),
        }),
        ('Bombat',  {
            'classes': ('collapse',),
            'fields': ('bombat',),
        }),
        ('Walker Award',  {
            'classes': ('collapse',),
            'fields': ('walker',),
        }),
    )
    class Media:
        js = [
			'/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
			'/static/grappelli/tinymce_setup/tinymce_setup.js',
		]    
    
class ItemAdmin(admin.TabularInline):
    model = Item
    fields = ("title","content","published","position",)
    # define the sortable
    sortable_field_name = "position"
    
    class Media:
        js = [
            '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/static/grappelli/tinymce_setup/tinymce_setup.js',
        ]
    
class PageAdmin(admin.ModelAdmin):
    inlines = [
        ItemAdmin,
    ]
    

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('description','image','year','caption')
    filter_horizontal = ('player_tag',)
    fieldsets = (
        (None, {
            'fields': (('image', 'description', 'year'),)
        }),
        (None, {
            'fields': ('caption','player_tag',)
        }),
    )    
    
admin.site.register(Player, PlayerAdmin)
admin.site.register(Game, GameRosterAdmin)
admin.site.register(Season, SeasonAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(Photo, PhotoAdmin)
#admin.site.register(HOF, HallAdmin)