from rest_framework import serializers

from novousapp.models import fuel


class FuelStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = fuel
        fields = ('Name','CompanyName','Address','City','State')