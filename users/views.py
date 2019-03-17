# Create your views here.
import hashlib

from django.db import transaction
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_swagger.views import get_swagger_view

from rest_framework.viewsets import ModelViewSet
from users.models import Users
from users.serializers import UsersSerializer, UsersLoginSerializer, UsersRegisterSerializer, UsersUpdateSerializer

schema_view = get_swagger_view(title='Assignment API')


class LoginUserView(generics.CreateAPIView):
    queryset = Users.objects.all()

    """
        Provides a post method handler.
    """
    serializer_class = UsersLoginSerializer

    def post(self, request, *args, **kwargs):

        """ Basic validations """

        try:

            login_model = UsersLoginSerializer(data=request.data)
            if not login_model.is_valid():
                data = {"message": "only username or password key allowed and value should not be empty"}
                return Response(data=data, status=status.HTTP_417_EXPECTATION_FAILED)
            else:
                username = request.data.get("username")
                password = request.data.get("password")

                if len(username) == 0 and len(password):
                    data = {"message": "only username or password key allowed and value should not be empty"}
                    return Response(data=data, status=status.HTTP_417_EXPECTATION_FAILED)

        except Exception as e:

            print("Error: ", e)
            data = {"message": "username or password key missing"}
            return Response(data=data, status=status.HTTP_417_EXPECTATION_FAILED)

        """ End of basic validation """

        new_user = {}

        """ Database query """
        try:

            result_pass = hashlib.md5(password.encode()).hexdigest()
            new_user = Users.objects.filter(username=username, password=result_pass).get()

        except Exception as e:

            print("Error: ", e)

        """ End of database query """

        if new_user == {}:
            data = {"message": "The user name or password is incorrect. Try again."}
            return Response(data=data, status=status.HTTP_404_NOT_FOUND)
        elif new_user:
            serializer = UsersSerializer(new_user, many=False)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            serializer = UsersSerializer(new_user, many=False)
            return Response(data=serializer.data, status=status.HTTP_200_OK)


class RegisterUserView(generics.CreateAPIView):
    queryset = Users.objects.all()

    """
        Provides a post method handler.
    """
    serializer_class = UsersRegisterSerializer

    @transaction.atomic
    def post(self, request, *args, **kwargs):

        first_name = request.data.get("firstName", "")
        middle_name = request.data.get("middle_name", "")
        last_name = request.data.get("lastName", "")
        email = request.data.get("email", "")
        mobile = request.data.get("mobile", "")
        password = request.data.get("password", "")
        is_superuser = request.data.get("isSuperuser", False)
        is_staff = request.data.get("isStaff", False)
        is_user = request.data.get("isUser", False)

        if (is_superuser and is_staff and is_user) or (is_superuser and is_staff) or (is_superuser and is_user) or (
                is_staff and is_user):
            data = {"message": "Please select only one role"}
            return Response(data=data, status=status.HTTP_417_EXPECTATION_FAILED)

        username = email
        hash_password = hashlib.md5(password.encode()).hexdigest()

        if not first_name and not last_name and not email and not mobile and not username:
            data = {
                "message": "first name, last name, email, mobile is required to register a user"
            }
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

        try:
            new_user = Users.objects.create(
                username=username,
                firstName=first_name,
                middleName=middle_name,
                lastName=last_name,
                email=email,
                mobile=mobile,
                password=hash_password,
                isSuperuser=is_superuser,
                isStaff=is_staff,
                isUser=is_user
            )
        except Exception as e:
            print("insert error: ", e)
            data = {
                "message": "email or mobile is already taken by other user."
            }
            return Response(data=data, status=status.HTTP_417_EXPECTATION_FAILED)

        if new_user:
            serializer = UsersSerializer(new_user, many=False)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class ListUserView(generics.ListAPIView):
    queryset = Users.objects.all()

    """
        Provides a get method handler.
    """
    serializer_class = UsersSerializer

    def get(self, request, *args, **kwargs):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = UsersSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class SubscriberViewSet(ModelViewSet):
    serializer_class = UsersSerializer
    #queryset = Users.objects.all()
    # if you need to get subscription by name
    #name = self.request.QUERY_PARAMS.get('name', None)
    #id = self.request.query_params.get('name',None)
    def get_queryset(self):
        queryset = Users.objects.all()
        # if you need to get subscription by name
        id = self.request.query_params.get('id', None)
        if id is not None:
            queryset = queryset.filter(id=id)

        return queryset

class UserDetailsView(generics.RetrieveUpdateAPIView):
    queryset = Users.objects.all()

    """
        Provides a get method handler.
    """
    serializer_class = UsersSerializer

    def get(self, request, *args, **kwargs):
        new_user = {}

        user_id = kwargs['id']

        try:
            new_user = Users.objects.filter(id=user_id).get()
        except Exception as e:
            print("error:", e)

        if new_user == {}:
            data = {
                "message": "User not present in the system"
            }
            return Response(data=data, status=status.HTTP_404_NOT_FOUND)
        elif new_user:
            serializer = UsersSerializer(new_user, many=False)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            serializer = UsersSerializer(new_user, many=False)
            return Response(data=serializer.data, status=status.HTTP_200_OK)

    """
        Provides a update method handler.
    """
    serializer_class = UsersUpdateSerializer

    @transaction.atomic
    def update(self, request, *args, **kwargs):

        first_name = request.data.get("firstName", "")
        middle_name = request.data.get("middleName", "")
        last_name = request.data.get("lastName", "")
        mobile = request.data.get("mobile", "")

        print('id', kwargs['id'])
        user_id = kwargs['id']
        if not user_id:
            data = {
                "message": "user id is required"
            }
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

        old_user = {}
        new_user = {}
        try:
            old_user = Users.objects.get(id=user_id)

            if len(first_name) == 0:
                first_name = old_user.firstName

            if len(middle_name) == 0:
                middle_name = old_user.middleName

            if len(last_name) == 0:
                last_name = old_user.lastName

            if len(mobile) == 0:
                mobile = old_user.mobile

            result = Users.objects.filter(id=user_id).update(
                firstName=first_name,
                middleName=middle_name,
                lastName=last_name,
                mobile=mobile
            )
            if result == 1:
                new_user = Users.objects.get(id=user_id)

        except Exception as e:
            print("insert error: ", e)
            if old_user == {}:
                data = {
                    "message": "User not present"
                }
                return Response(data=data, status=status.HTTP_404_NOT_FOUND)
            else:
                data = {
                    "message": e
                }
                return Response(data=data, status=status.HTTP_417_EXPECTATION_FAILED)

        if new_user:
            serializer = UsersSerializer(new_user, many=False)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
