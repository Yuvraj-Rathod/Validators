from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)



def create(self, validate_data):
    return Student.objects.create(**validate_data)

def update(self, instance, validate_data):
    instance.name = validate_data.get('name', instance.name)
    instance.roll = validate_data.get('roll', instance.roll)
    instance.city = validate_data.get('roll', instance.city)

    return instance

# FIELD LEVEL VALIDATION
def validate_roll(self, value) :
    if value >= 200 :
        raise serializers.ValidationError("SEAT FULL")
    return value


# OBJECT LEVEL VALIDATION
def validate(self, data):
    nm = data.get('name')
    ct = data.get('city')
    if nm.lower() == 'rohit' and ct.lower() != "ranchi":
        raise serializers.ValidationError('City Must Be Ranchi')
    return data


#VALIDATORS
def starts_with_r(self,value):
    if value [0].lower() != 'r':
        raise serializers.ValidationError('xxxx')
    
class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50, validators=[starts_with_r])
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)