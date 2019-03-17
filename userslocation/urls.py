from django.urls import path

from userslocation.views import ListAndSaveUserLocationView, ListAllUsersLocationView , SubscriberViewSet

from rest_framework.routers import SimpleRouter
'''
urlpatterns = [
    path('locations/<userId>/', ListAndSaveUserLocationView.as_view(), name="list-and-save-user-location"),
    path('locations/', ListAllUsersLocationView.as_view(), name="list-all-users-location"),
]'''


router = SimpleRouter()
router.register('userlocations', SubscriberViewSet, base_name='userlocations')
#router.register('locations/<userId>/', ListAndSaveUserLocationView.as_view(), base_name="list-and-save-user-location"),
#router.register('locations/', ListAllUsersLocationView.as_view(), base_name="list-all-users-location")
urlpatterns = router.urls