from django.contrib import admin
from .models import Company, Game, Developer

# Register the Company model with custom display settings
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('name', 'founded_date', 'headquarters', 'website')

# Define an inline admin class for developers (related to games)
class DeveloperInline(admin.TabularInline):
    model = Game.developers.through  # Use the through model for the many-to-many relationship
    extra = 1  # Number of extra forms to display

# Register the Game model with custom display settings
@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = (
        'title', 'release_year', 'company', 'sales', 'genre', 'platforms', 
        'rating', 'description', 'awards', 'box_art_url', 'display_developers'
    )

    # Add the inline developer admin
    inlines = [DeveloperInline]

    # Custom method to display developers for a game
    def display_developers(self, obj):
        # Join developer names with a comma
        return ", ".join([developer.name for developer in obj.developers.all()])
    display_developers.short_description = 'Developers'

# Register the Developer model with custom display settings
@admin.register(Developer)
class DeveloperAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('name', 'founded_date', 'headquarters', 'website')
