# Generated by Django 5.0.8 on 2024-08-07 14:12

from django.db import migrations, models

def create_initial_data(apps, schema_editor):
    Company = apps.get_model('polls', 'Company')
    Game = apps.get_model('polls', 'Game')

    # Create company records
    rockstar = Company.objects.create(
        name="Rockstar Games", 
        founded_date="1998-01-01", 
        headquarters="New York City", 
        website="https://www.rockstargames.com"
    )
    naughty_dog = Company.objects.create(
        name="Naughty Dog", 
        founded_date="1984-01-01", 
        headquarters="Santa Monica", 
        website="https://www.naughtydog.com"
    )
    activision_blizzard = Company.objects.create(
        name="Activision Blizzard", 
        founded_date="2008-01-01", 
        headquarters="Santa Monica", 
        website="https://www.activisionblizzard.com"
    )
    ubisoft = Company.objects.create(
        name="Ubisoft", 
        founded_date="1986-01-01", 
        headquarters="Montreuil", 
        website="https://www.ubisoft.com"
    )
    insomniac_games = Company.objects.create(
        name="Insomniac Games", 
        founded_date="1994-01-01", 
        headquarters="Burbank", 
        website="https://www.insomniacgames.com"
    )

    # Create game records linked to the companies
    Game.objects.create(
        title="Grand Theft Auto V", 
        release_year=2013, 
        company=rockstar, 
        sales=145000000, 
        genre="Action-Adventure", 
        platforms="PS4, Xbox One, PC", 
        rating=9.8, 
        description="An open-world action-adventure game.", 
        awards="Game of the Year", 
        box_art_url="https://example.com/gta_v_box_art.jpg"
    )
    Game.objects.create(
        title="The Last of Us", 
        release_year=2013, 
        company=naughty_dog, 
        sales=20000000, 
        genre="Action-Adventure", 
        platforms="PS3, PS4", 
        rating=9.5, 
        description="A post-apocalyptic action-adventure game.", 
        awards="Game of the Year", 
        box_art_url="https://example.com/last_of_us_box_art.jpg"
    )
    Game.objects.create(
        title="God of War (2018)", 
        release_year=2018, 
        company=ubisoft, 
        sales=10000000, 
        genre="Action-Adventure", 
        platforms="PS4", 
        rating=9.7, 
        description="An action-adventure game with Norse mythology themes.", 
        awards="Game of the Year", 
        box_art_url="https://example.com/god_of_war_box_art.jpg"
    )
    Game.objects.create(
        title="Call of Duty: Modern Warfare 2", 
        release_year=2009, 
        company=activision_blizzard, 
        sales=25000000, 
        genre="First-Person Shooter", 
        platforms="PS3, Xbox 360, PC", 
        rating=9.3, 
        description="A popular first-person shooter game.", 
        awards="Best Shooter", 
        box_art_url="https://example.com/cod_mw2_box_art.jpg"
    )
    Game.objects.create(
        title="Spider-Man", 
        release_year=2018, 
        company=insomniac_games, 
        sales=33000000, 
        genre="Action-Adventure", 
        platforms="PS4", 
        rating=9.4, 
        description="An open-world Spider-Man game.", 
        awards="Best Superhero Game", 
        box_art_url="https://example.com/spiderman_box_art.jpg"
    )


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='sales',
            field=models.BigIntegerField(),
        ),
        migrations.RunPython(create_initial_data),
    ]
