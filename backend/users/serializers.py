from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

User = get_user_model()


# ------------------------------
# User Serializer (For Profile)
# ------------------------------
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","email","name","phone","profile_images"]
        read_only_fields = ["id","emails"] 


# ------------------------------
# Register Serializer
# ------------------------------
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True,required=True,validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ["email","name","phone","password","password2"]
    
    def validate(self, attrs):
        if attrs["password"]!= attrs["password2"]:
            raise serializers.ValidationError("Passwords do not match")
        return attrs
    
    def create(self, validated_data):
        validated_data.pop("password2")
        user = User.objects.create_user(**validated_data)
        return user
    

# ------------------------------
# Change Password Serializer
# ------------------------------    
class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True,validators= [validate_password]
    )


# ------------------------------
# Update Profile Serializer
# ------------------------------
class UpdateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["name", "phone", "profile_image"]


