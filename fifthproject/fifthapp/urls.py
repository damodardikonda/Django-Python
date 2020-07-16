from django.urls import path
from fifthapp import views as fifthapp_view
urlpatterns = [
    path('first/',fifthapp_view.first_view),
    path('second/',fifthapp_view.second_view),
    path('third/',fifthapp_view.third_view),
    path('fourth/',fifthapp_view.fourth_view),
    path('fifth/',fifthapp_view.fifth_view),

]
