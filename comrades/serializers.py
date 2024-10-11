from rest_framework import serializers

from comrades.models import Comrades


class ComradesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comrades
        fields = ['id','name','email','semester','academic_year','course','year_in_school']