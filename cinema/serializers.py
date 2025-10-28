from rest_framework import serializers
from .models import Movie

<<<<<<< HEAD

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ["id", "title", "description", "duration"]
=======
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"
>>>>>>> 2b6308f2207193ba4916bdfbe9ecf71a54d126ed
