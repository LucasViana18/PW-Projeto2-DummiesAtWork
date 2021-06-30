from django.db import models


# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    country = models.CharField(max_length=30)
    subject = models.CharField(max_length=1000)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Question(models.Model):
    TYPE_MOVEMENT = (
        ("TELEPORT", "Teleport"),
        ("SMOOTH LOCOMOTION", "Smooth locomotion"),
        ("ARM SWING", "Arm Swing"),
    )

    VR_GAMES = (
        ("BEAT SABER", "Beat Saber"),
        ("SUPERHOT", "Superhot"),
        ("TROVER SAVES THE UNIVERSE", "Trover Saves The Universe"),
        ("HALF LIFE: ALYX", "Half Life: Alyx"),
        ("STAR TREK", "Star Trek: Bridge Crew"),
        ("BONEWORKS", "Boneworks"),
        ("JOB SIMULATOR", "Job Simulator"),
    )

    GAME_PERSPECTIVE = (
        ("GOD VIEW", "God View"),
        ("2D SIDEVIEW", "2D Sideview"),
        ("2.5D", "2.5D"),
        ("ISOMETRIC", "Isometric"),
        ("THIRD PERSON", "Third Person"),
        ("FIRST PERSON", "First Person"),
    )

    SERVICES = (
        ("FULL CYCLE PRODUCTION", "Full Cycle Production"),
        ("AR PRODUCTION", "AR Production"),
        ("PROTOTYPING", "Prototyping"),
        ("GAME PORTING", "Game Porting"),
    )

    GENRES = (
        ("ADVENTURE", "Adventure"),
        ("ACTION", "Action"),
        ("FPS", "FPS"),
        ("RPG", "RPG"),
        ("LIGHT NOVEL", "Light Novel"),
        ("RHYTHM", "Rhythm"),
    )

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    best_selling_VR_game = models.TextField(choices=VR_GAMES)
    most_popular_type_of_movement_in_VR = models.TextField(choices=TYPE_MOVEMENT)
    can_VR_cause_motion_sickness = models.BooleanField()
    bruhh_is_a_3D_ragdoll_physics_game = models.BooleanField()
    what_is_bloodthirst_game_perspective = models.TextField(choices=GAME_PERSPECTIVE)
    which_services_we_do_not_offer = models.TextField(choices=SERVICES)
    how_many_links_there_are_in_the_home_page = models.IntegerField()
    what_is_anything_but_dark_genre = models.TextField(choices=GENRES)
    what_was_the_icon_used_in_anastasis = models.CharField(max_length=10)
    is_there_a_demonstration_video_on_this_website = models.BooleanField()
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Comment(models.Model):
    name = models.CharField(max_length=120)
    subject = models.TextField(max_length=500)

    def __str__(self):
        return self.name
