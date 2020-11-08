from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer
User = get_user_model()

class UserMapSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["map"]

    def save(self, *args, **kwargs):
        if self.instance.map:
            self.instance.map.delete()
        return super().save(*args, **kwargs)