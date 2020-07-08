from users.models import Users, ActivityPeriod
from rest_framework import serializers


class ActivityPeriodSerializer(serializers.ModelSerializer):
    start_time = serializers.CharField(source='StartTime')
    end_time = serializers.CharField(source='EndTime')

    class Meta:
        model = ActivityPeriod
        fields = ('start_time', 'end_time')


class UserSerializer(serializers.ModelSerializer):
    real_name = serializers.CharField(source='get_full_name')
    tz = serializers.CharField(source='Timezone')
    activity_periods = ActivityPeriodSerializer(many=True, read_only=True)

    class Meta:
        model = Users
        fields = ('id', 'real_name', 'tz', 'activity_periods')
