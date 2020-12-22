from django.urls import path
from .worker_details_views  import display_by_category, display_all, get_specific_worker_details
from .job_views import display_job,display_recruiter_job
from .requests_views import recruiters_requests, wokers_requests
from .responses_views import recruiters_response, workers_response
from .web_views import home_total_wokers , home_total_jobs , home_total_req , home_accept_req , home_smart_reg
urlpatterns =[
    #Worker_Details
    path('category/<str:category>/', display_by_category ),
    path('allcategories/', display_all ),
    path('specific/workerdetails/<int:user_id>', get_specific_worker_details ),

    #Job_Details
    path('specificjobs/<int:user>', display_job ),
    path('recruiterinfo/<int:recruiterid>',display_recruiter_job),

    #recruiters_requests
    path('recuriters/requests/',recruiters_requests),
    path('workers/requests/<int:worker_id>',wokers_requests),

    #RESPONSES
    path('recreq/<int:st>/<int:job_id>',recruiters_response),
    path('worreq/<int:st>/<int:job_id>',workers_response),

    #Home page website
    path('totalworker/' , home_total_wokers , name = 'totalworker'),
    path('totaljobs/' , home_total_jobs , name = 'totaljobs'),
    path('totalreq/',home_total_req , name ='totalreq'),
    path('Acceptreq/' , home_accept_req , name = 'Acceptreq'),

    #without smartphones
    path('smartreg/' , home_smart_reg , name = 'smartreg'),
]
