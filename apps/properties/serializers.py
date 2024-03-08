from django_countries.serializer_fields import CountryField
from django_countries.serializer import CountryFieldMixin
from rest_framework import serializers
from .models import Property, PropertyViews

# Register your models here.

class PropertySerializer(serializer.modelsSerializer):
    user = serializers.SerializerMethodField()
    country = CountryField(name_only=True)

    class Meta:
        model = Property
        fields = [
            "id",
            "user",
            "title",
            "slug",
            "ref_code",
            "description",
            "country",
            "city",
            "postal_code",
            "street_address",
            "property_number",
            "price",
            "tax",
            "final_property_price",
            "plot_area",
            "total_floor",
            "bedrooms",
            "bathrooms",
            "advert_type",
            "property_type",
            "cover_photo",
            "photo1",
            "photo2",
            "photo3",
            "photo4",
            "published_status",
            "views",
        ]

    def det_user(self, obj):
        return obj.user.username

class PropertyCreateSerializer(serializers.ModelSerializer):
    country = CountryField(name_only=True)

    class Meta:
        model = Property
        exclude = ["updated_at", "pkid"]

class PropertyViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyViews
        exclude = ["updated_at", "pkid"]