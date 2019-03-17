from django.urls import path

from users.views import LoginUserView, RegisterUserView, ListUserView, UserDetailsView ,SubscriberViewSet

from rest_framework.routers import SimpleRouter

from rest_framework_jwt.views import obtain_jwt_token

'''
urlpatterns = [
    path('login/', LoginUserView.as_view(), name="login"),
    path('register/', RegisterUserView.as_view(), name="user-register"),
    path('users/', ListUserView.as_view(), name="user-all"),
    path('users/<int:id>/', UserDetailsView.as_view(), name="user-details"),
    path('users/<int:id>/', UserDetailsView.as_view(), name="user-update"),
    #path('subscriber/', SubscriberViewSet.as_view({'get': 'list', 'post': 'create'}), name="subscriber api all"),
    #path('subscriber/<int:pk>', SubscriberViewSet.as_view({'get': 'retrieve', 'put':'update'}), name="subscriber api by user"),

]'''


router = SimpleRouter()
router.register('users', SubscriberViewSet, base_name='users')
#urlpatterns = router.urls
urlpatterns = router.urls +  [
    #path(r'^jwt-auth/', obtain_jwt_token),
    path('jwtValidate/', obtain_jwt_token, name="jwt token validation"),
]