from main.models import Polls, Questions
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from main.serializers import PollsSerializers, QuestionsSerializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


@api_view(['GET'])
def auth(request):
    user = User.objects.get(username='admin')
    token = Token.objects.update_or_create(user=user)
    return Response({
        'Authorization': 'token ' + str(token[0])
    })


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_poll(request):
    ser = PollsSerializers(data=request.data)
    if ser.is_valid():
        ser.save()
        return Response(ser.data)
    return Response(ser.errors)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_question(request):
    request.data["Option"] = str(request.data["Option"])
    ser = QuestionsSerializers(data=request.data)
    if ser.is_valid():
        poll = Polls.objects.get(Name=request.data['Name'])
        poll.questions_set.create(Text=request.data['Text'], Type=request.data['Type'], Option=request.data['Option'])
        return Response(ser.data)
    return Response(ser.errors, status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def delete_question(request):
    try:
        Questions.objects.get(Text=request.data['Text']).delete()
        return Response('deleted')
    except:
        return Response("DoesNotExist")


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def delete_poll(request):
    try:
        Questions.objects.get(Text=request.data['Name']).delete()
        return Response('deleted')
    except:
        return Response("DoesNotExist")


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def change_question(request):
    question = Questions.objects.get(Text=request.data['Text'])
    try:
        for x in request.data['Change']:
            if x == 'Text':
                question.Text = request.data['Change']['Text']
            elif x == 'Type':
                question.DateEnd = request.data['Change']['Type']
            elif x == 'Option':
                question.Description = request.data['Change']['Option']
        question.save()
        return Response('update')

    except:
        return Response('some wrong')


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def change_poll(request):
    poll = Polls.objects.get(Name=request.data['Name'])
    try:
        for x in request.data['Change']:
            if x == 'Name':
                poll.Name = request.data['Change']['Name']
            elif x == 'DateEnd':
                poll.DateEnd = request.data['Change']['DateEnd']
            elif x == 'Description':
                poll.Description = request.data['Change']['Description']
        poll.save()
        return Response('update')

    except:
        return Response('some wrong')
