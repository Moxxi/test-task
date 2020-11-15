from rest_framework import serializers
from .models import Polls, Questions, Answers


class PollsSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Polls
        fields = ['Name', 'DateStart', 'DateEnd', 'Description']


class QuestionsSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Questions
        fields = ['Text', 'Type', 'Option']


class AnswersSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Answers
        fields = ['Question', 'Answer']