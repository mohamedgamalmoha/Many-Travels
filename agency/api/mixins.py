

class DefaultImageSerializerMixin:
    image_field_name: str = 'image'
    default_image_url: str = None

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        if not representation.get(self.image_field_name, None):
            representation[self.image_field_name] = self.build_image_url()

        return representation

    def build_image_url(self):
        request = self.context.get('request')
        return request.build_absolute_uri(self.default_image_url)
