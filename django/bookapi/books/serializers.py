from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        # fields = ['id', 'title', 'author', 'price']


# class MenuItemSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MenuItem
#         fields = ['id','title','price','inventory']
#         extra_kwargs = {
#             'price': {'min_value': 2},
#             'inventory':{'min_value':0}
#         }

# To use the XML renderer effectively, install the djangorestframework-xml
# package using pip or pipenv in your project.
# REST_FRAMEWORK = {
#     'DEFAULT_RENDERER_CLASSES': [
#         'rest_framework.renderers.JSONRenderer',
#         'rest_framework.renderers.BrowsableAPIRenderer',
#         'rest_framework_xml.renderers.XMLRenderer',
#     ]
# }
