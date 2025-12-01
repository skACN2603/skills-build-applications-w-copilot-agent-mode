from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class ModelTests(TestCase):
    def setUp(self):
        marvel = Team.objects.create(name='Team Marvel')
        dc = Team.objects.create(name='Team DC')
        tony = User.objects.create(name='Tony Stark', email='tony@marvel.com', team=marvel)
        bruce = User.objects.create(name='Bruce Wayne', email='bruce@dc.com', team=dc)
        Activity.objects.create(user=tony, type='Run', duration=30, calories=300)
        Workout.objects.create(name='Morning Cardio', description='Cardio for all heroes', duration=40)
        Leaderboard.objects.create(user=tony, score=1000)

    def test_user_count(self):
        self.assertEqual(User.objects.count(), 2)
    def test_team_count(self):
        self.assertEqual(Team.objects.count(), 2)
    def test_activity_count(self):
        self.assertEqual(Activity.objects.count(), 1)
    def test_workout_count(self):
        self.assertEqual(Workout.objects.count(), 1)
    def test_leaderboard_count(self):
        self.assertEqual(Leaderboard.objects.count(), 1)
