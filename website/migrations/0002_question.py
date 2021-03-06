# Generated by Django 3.2.3 on 2021-06-03 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('best_selling_VR_game', models.TextField(choices=[('BEAT SABER', 'Beat Saber'), ('SUPERHOT', 'Superhot'), ('TROVER SAVES THE UNIVERSE', 'Trover Saves The Universe'), ('HALF LIFE: ALYX', 'Half Life: Alyx'), ('STAR TREK', 'Star Trek: Bridge Crew'), ('BONEWORKS', 'Boneworks'), ('JOB SIMULATOR', 'Job Simulator')])),
                ('most_popular_type_of_movement_in_VR', models.TextField(choices=[('TELEPORT', 'Teleport'), ('SMOOTH LOCOMOTION', 'Smooth locomotion'), ('ARM SWING', 'Arm Swing')])),
                ('can_VR_cause_motion_sickness', models.BooleanField()),
                ('bruhh_is_a_3D_ragdoll_physics_game', models.BooleanField()),
                ('what_is_bloodthirst_game_perspective', models.TextField(choices=[('GOD VIEW', 'God View'), ('2D SIDEVIEW', '2D Sideview'), ('2.5D', '2.5D'), ('ISOMETRIC', 'Isometric'), ('THIRD PERSON', 'Third Person'), ('FIRST PERSON', 'First Person')])),
                ('which_services_we_do_not_offer', models.TextField(choices=[('FULL CYCLE PRODUCTION', 'Full Cycle Production'), ('AR PRODUCTION', 'AR Production'), ('PROTOTYPING', 'Prototyping'), ('GAME PORTING', 'Game Porting')])),
                ('how_many_links_there_are_in_the_home_page', models.IntegerField()),
                ('what_is_anything_but_dark_genre', models.TextField(choices=[('ADVENTURE', 'Adventure'), ('ACTION', 'Action'), ('FPS', 'FPS'), ('RPG', 'RPG'), ('LIGHT NOVEL', 'Light Novel'), ('RHYTHM', 'Rhythm')])),
                ('what_was_the_icon_used_in_anastasis', models.CharField(max_length=10)),
                ('is_there_a_demonstration_video_on_this_website', models.BooleanField()),
            ],
        ),
    ]
