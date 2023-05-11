from rest_framework import serializers
from rest_framework.relations import SlugRelatedField


from posts.models import Comment, Post, Follow, User, Group


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)
    image = serializers.ImageField(required=False)
    group = serializers.PrimaryKeyRelatedField(queryset=Group.objects.all(),
                                               required=False)

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )
    post = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        fields = '__all__'
        model = Comment


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )
    following = serializers.SlugRelatedField(slug_field='username',
                                             queryset=User.objects.all())

    class Meta:
        fields = ('following', 'user')
        model = Follow

    def validate_following(self, following):
        user = self.context['request'].user
        if user == following:
            raise serializers.ValidationError('You cannot'
                                              'subscribe to yourself')
        if (Follow.objects.filter(user__username=user)
           .filter(following__username=following)):
            raise serializers.ValidationError('Subscription already exists')
        return following


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Group
        ref_name = 'ReadOnlyGroups'
