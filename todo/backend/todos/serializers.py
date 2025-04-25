from rest_framework import serializers
from .models import Todo
import pytz         #For datetime formatting

class TodoSerializer(serializers.ModelSerializer):
    formatted_datetime = serializers.SerializerMethodField()

    class Meta:
        model = Todo
        fields = ('id', 'title', 'body','formatted_datetime')

    def get_formatted_datetime(self, obj):
        tz = pytz.timezone('Africa/Dar_es_Salaam')
        local_dt = obj.create_time.astimezone(tz)
        return local_dt.strftime("Created at %I:%M:%p on  %A, %dth %b, %Y")
        