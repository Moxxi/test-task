from .models import Polls, Questions
from datetime import datetime
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def get_poll(request):
    try:
        poll = Polls.objects.get(Name=request.data['Name'])
    except:
        return Response('not found')

    if datetime.timestamp(datetime.strptime(poll.DateEnd, '%d.%m.%Y')) > datetime.timestamp(
            datetime.strptime(str(datetime.now().date()), '%Y-%m-%d')) > datetime.timestamp(
        datetime.strptime(poll.DateStart, '%d.%m.%Y')):
        questions = []
        for x in poll.questions_set.all():
            questions.append({
                "Text": x.Text,
                "Type": x.Type,
                "Option": x.Option
            })
        return Response({
            "Poll": {
                "Name": poll.Name,
                "Description": poll.Description,
            },
            "Questions": questions
        })
    return Response('poll is over or not yet')


@api_view(['GET'])
def get_polls(request):
    polls = []
    try:
        for x in Polls.objects.all():
            if datetime.timestamp(datetime.strptime(x.DateEnd, '%d.%m.%Y')) > datetime.timestamp(
                datetime.strptime(str(datetime.now().date()), '%Y-%m-%d')) > datetime.timestamp(
                datetime.strptime(x.DateStart, '%d.%m.%Y')):
                polls.append({
                    "Name": x.Name,
                    "Description": x.Description
                })
        return Response({
            "Polls": polls
        })
    except:
        return Response('empty')


@api_view(['POST'])
def get_user_poll(request):
    poll = Polls.objects.get(Name=request.data['Name'])
    response = {
        'poll': poll.Name,
        'description': poll.Description
    }
    for x in poll.questions_set.all():
        response[x.Text] = x.answers_set.get(UserId=request.data['Id']).Answer
    return Response(response)


@api_view(['POST'])
def get_user_polls(request):
    response = {}
    for x in Polls.objects.all():
        try:
            x.questions_set.first().answers_set.get(UserId=request.data['Id'])
            response[x.Name] = x.Description
        except:
            continue
    return Response(response)


@api_view(['POST'])
def create_answers(request):
    id_user = request.data["Id"]
    try:
        for x in request.data['Answers']:
            question = Questions.objects.get(Text=x)
            question.answers_set.create(Answer=request.data['Answers'][x], UserId=id_user)
        return Response('answers save')
    except:
        return Response('false question')
