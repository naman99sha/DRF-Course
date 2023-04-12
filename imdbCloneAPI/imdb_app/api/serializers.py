from rest_framework import serializers
from imdb_app.models import *

class MovieSerializer(serializers.ModelSerializer):
    len_name = serializers.SerializerMethodField()
    
    def get_len_name(self,objects):
        return len(objects.name)
    class Meta:
        model = Movie
        fields = '__all__'
    
    def validate(self, data):
        if data['name'] == data['desc']:
            raise serializers.ValidationError("title and description cant be same")
        return data

# def name_length(val):
#     if len(val)<2:
#         raise serializers.ValidationError("too short name")

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     desc = serializers.CharField()
#     active = serializers.BooleanField()
    
#     def create(self, validatedData):
#         return Movie.objects.create(**validatedData)
    
#     def update(self,instance, validatedData):
#         instance.name = validatedData.get('name',instance.name)
#         instance.desc = validatedData.get('desc',instance.desc)
#         instance.active = validatedData.get('active',instance.active)
#         instance.save()
#         return instance