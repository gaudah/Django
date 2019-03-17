import json

from django.db import transaction
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_swagger.views import get_swagger_view

from users.models import Users
from userslocation.models import UsersLocation
from userslocation.serializers import UserLocationsSerializer, UserLocationsUpdateSerializer
from rest_framework.viewsets import ModelViewSet

schema_view = get_swagger_view(title='Assignment API')


class ListAndSaveUserLocationView(generics.ListCreateAPIView):
    queryset = UsersLocation.objects.all()

    """
        Provides a post method handler.
    """
    serializer_class = UserLocationsSerializer

    def get(self, request, *args, **kwargs):

        user_id = int(kwargs['userId'])

        if user_id == 0:
            data = {"message": "user id id required"}
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

        search = self.request.query_params.get('search')
        search_params = {}
        start_date = ''
        end_date = ''
        if search:
            search_params = json.loads(search, encoding=None)
            print('search_params: ', search_params)

            if 'startDate' in search_params:
                start_date = search_params['startDate']

            if 'endDate' in search_params:
                end_date = search_params['endDate']

        if search_params == {}:
            user_locations = UsersLocation.objects.filter(userId=user_id)
            print(user_locations.query)

        elif start_date and not end_date:
            user_locations = UsersLocation.objects.filter(userId=user_id, createdAt__gte=start_date)
            print(user_locations.query)

        elif start_date and end_date and (start_date == end_date):
            user_locations = UsersLocation.objects.filter(userId=user_id,
                                                          createdAt__contains=start_date)
            print(user_locations.query)

        elif start_date and end_date:
            user_locations = UsersLocation.objects.filter(userId=user_id, createdAt__gte=start_date,
                                                          createdAt__lte=end_date)
            print(user_locations.query)

        else:
            user_locations = UsersLocation.objects.filter(userId=user_id)
            print(user_locations.query)

        # user_locations = UserLocations.objects.filter(userId=user_id)
        serializer = UserLocationsSerializer(user_locations, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    """
        Provides a post method handler.
    """
    serializer_class = UserLocationsUpdateSerializer

    @transaction.atomic
    # @transaction.rollback
    def post(self, request, *args, **kwargs):
        new_location = {}

        q_user_id = int(kwargs['userId'])

        if q_user_id == 0:
            data = {"message": "user_id id required"}
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

        user_id = int(request.data.get("userId", 0))
        latitude = request.data.get("latitude", 0.000000)
        longitude = request.data.get("longitude", 0.00000)
        area = request.data.get("area", "")

        if user_id == 0:
            data = {"message": "user_id id required"}
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

        elif user_id > 0:
            try:
                # new_user = Users.objects.get(id=q_user_id)
                new_location = UsersLocation.objects.create(
                    userId=user_id,
                    latitude=latitude,
                    longitude=longitude,
                    area=area
                )
            except Exception as e:
                print("insert error: ", e)
                data = {
                    "message": "Provided data not available"
                }
                return Response(data=data, status=status.HTTP_406_NOT_ACCEPTABLE)

        serializer = UserLocationsSerializer(new_location, many=False)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class ListAllUsersLocationView(generics.ListAPIView):
    queryset = UsersLocation.objects.all()

    """
        Provides a get method handler.
    """
    serializer_class = UserLocationsSerializer

    def get(self, request, *args, **kwargs):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = UserLocationsSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)




class SubscriberViewSet(ModelViewSet):
    serializer_class = UserLocationsSerializer
    #queryset = Users.objects.all()
    # if you need to get subscription by name
    #name = self.request.QUERY_PARAMS.get('name', None)
    #id = self.request.query_params.get('name',None)
    def get_queryset(self):
        queryset = UsersLocation.objects.all()
        # if you need to get subscription by name
        id = self.request.query_params.get('id', None)
        if id is not None:
            queryset = queryset.filter(userId=id)

        return queryset
