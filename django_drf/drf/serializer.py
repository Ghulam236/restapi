from rest_framework import serializers
from .models import Student


# 3--> validators method name spycify in field name 
def starts_with_r(value):
    if value[0].lower()!='r':
        raise serializers.ValidationError("name starts with R ")
class StudentSerializer(serializers.Serializer):
    # we use model serializer for ding fast and less code 
    #  so we use ModelSerializer instead of Serializer
    # class StudentSerializer(serializers.ModlelSerializer):
    #     class Meta:
    #         model=Student
    #         fields=['name','roll','city']
    #  also use validators as i used in serializers
    #     def validate(self,data):
    #     nm=data.get('name')
    #     ct=data.get('city')
    #     if nm.lower()=='sarfaraz' and ct!='bareilly':
    #         raise serializers.ValidationError("city must be bareilly")
    #     return data    
    name=serializers.CharField(max_length=100,validators=[starts_with_r])
    roll=serializers.IntegerField()
    city=serializers.CharField(max_length=100)
    def create(self,validated_data):
        return Student.objects.create(**validated_data)
    def update(self,instance,validated_data):
        print(instance.name)

        instance.name=validated_data.get('name',instance.name)
        print(instance.name)
        instance.roll=validated_data.get('roll',instance.roll)
        instance.city=validated_data.get('city',instance.city)
        instance.save()
        return instance
    

    # ##################### VALIDATION #####################################
    #  1--> field validation

    # if i want to validate filed then create a method as validate_fieldname here fieldname is 
    # which field youb wanrt to validate so i validate roll no then validate_roll(self,value)
    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError('seat full')
        return value
                 
    #   2---> object validation
    #  
    #  object level validation##############
    #  in this def validate(self,data) wher data is dict of field
    def validate(self,data):
        nm=data.get('name')
        ct=data.get('city')
        if nm.lower()=='sarfaraz' and ct!='bareilly':
            raise serializers.ValidationError("city must be bareilly")
        return data

    
    

    
