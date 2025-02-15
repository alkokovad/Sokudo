from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import *
from .models import Meet
import folium
import base64


@api_view(['GET', 'POST'])
def service(request):
    m = folium.Map(location=[59.945502, 30.311220], tiles="Cartodb dark_matter", zoom_control=False, attributionControl=0)

#     icon = folium.CustomIcon(
#         icon_image,
#         icon_size=(512, 512),
#         icon_anchor=(0, 0),
#         popup_anchor=(-3, -76),
#     )
    kw = {"prefix": "fa", "color": "green", "icon": "arrow-up"}

    angle = 180
    icon = folium.Icon(angle=angle, **kw)

    mark = folium.Marker(
        location=[60.012433, 30.323237], icon=icon, tooltip=str(angle)
    ).add_to(m)
    m = m.get_root().render()
    if request.method == 'GET':
        data = Meet.objects.all()
        serializer = MeetSerializer(data, context={'request': request}, many=True)
        return Response(m)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'DELETE'])
def service_detail(request, pk):
    try:
        content = Meet.objects.get(pk=pk)
    except Content.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        serializer = MeetSerializer(content, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
