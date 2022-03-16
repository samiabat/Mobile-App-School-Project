from unicodedata import name
from rest_framework.decorators import api_view
from rest_framework.response import Response

from . models import User, App
from .serializers import UserSerializer, AppSerializer

# Create your views here.


@api_view(['GET'])
def getRoutes(request):
    route = [
        {
            "name":"samuel",
            "grade": "university",
        },
        {
            "name":"mulugeta Abatneh",
            "grade": "university",
        }
    ]
    return Response(route)



@api_view(['GET'])
def getWidgets(request):
    widgets = [

        {"widget": {
            "debug": "on",
            }
        },
        {"window": {
            "title": "Sample Konfabulator Widget",
            "name": "main_window",
            "width": 500,
            "height": 500
            }
        },
        {"image": { 
            "src": "Images/Sun.png",
            "name": "sun1",
            "hOffset": 250,
            "vOffset": 250,
            "alignment": "center"
            }
        },

        {"text": {
            "data": "Click Here",
            "size": 36,
            "style": "bold",
            "name": "text1",
            "hOffset": 250,
            "vOffset": 100,
            "alignment": "center",
            "onMouseUp": "sun1.opacity = (sun1.opacity / 100) * 90;"
            }
        }
    ]
    return Response(widgets)



@api_view(['GET'])
def getApps(request):
    apps = App.objects.all()
    serializer = AppSerializer(apps, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def getApp(request, pk):
    app = App.objects.get(id=pk)
    serializer = AppSerializer(app, many = False)
    return Response(serializer.data)

@api_view(['POST'])
def createApp(request):
    data = request.data

    app = App.objects.create(
        name = data['name'], 
        auther = data['auther'],
        )
    serializer = AppSerializer(app, many = False)
    return Response(serializer.data)


@api_view(['PUT'])
def updateApp(request, pk):
    data = request.data
    app = App.objects.get(id = pk)
    serializer = AppSerializer(app, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteApp(request, pk):
    app = App.objects.get(id=pk)
    app.delete()
    return Response("deleted!")
