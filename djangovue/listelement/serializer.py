from rest_framework import serializers
from .models import Element, Category, Type
from comment.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    count = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = '__all__'

    def get_count(self,obj):
        return Comment.objects.filter(element_id = obj.element_id).count()

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'
    
class ElementSerializer(serializers.ModelSerializer):
    #busca la relacion con el mismo nombre (category, type) e imprimie el __str__
    # category = serializers.StringRelatedField()
    # type = serializers.StringRelatedField()
    type = TypeSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    # comments = serializers.StringRelatedField(many=True)
    comments = CommentSerializer(read_only=True, many=True)
    class Meta:
        model = Element
        fields = '__all__'