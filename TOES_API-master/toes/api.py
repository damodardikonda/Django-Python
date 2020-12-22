from django.shortcuts import render
from authapp.models import (
    WorkerDetails, JobDetails, User, Categories
    )
from django.db import connection
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
import requests
import json

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def recruiters_requests(request,user_id):
    cursor=connection.cursor()
    #cursor.execute(f"select * from authapp_worker_Details where category_1 = '{category}' OR category_2 = '{category}' OR category_3 = '{category}' ")
    cursor.execute(
    
    """
    select recruiter_id, worker_id, job_detail_id, name ,address, amount , job_Description , 
    category_1 , category_1_exp, category_2, category_2_exp, category_3 , category_3_exp , job_title
    from authapp_user u 
    INNER JOIN authapp_workerdetails w on u.id = w.user_id  
    INNER JOIN authapp_recruitersrequests r on u.id = r.worker_id 
    LEFT JOIN authapp_jobdetails j on  j.id  = r.job_detail_id
    """
    )

    row = cursor.fetchall()
    print(row)
    content = {}
    payload = []
    for result in row:
        if result[0] == user_id:
            if result[13] == result[7]:
                content = {
                        'recruiter_id' : result[0],
                        'worker_id' : result[1],
                        'job_title' : result[13],
                        'job_detail_id' : result[2],
                        'worker_name' : result[3],
                        'address' : result[4],
                        'amount' : result[5],
                        'job_Description' : result[6],
                        'worker_profession' : result[7],
                        'workers_experience' : result[8],
            
                        }
            elif result[13] == result[9]:
                content = {
                        'recruiter_id' : result[0],
                        'worker_id' : result[1],
                        'job_title' : result[13],
                        'job_detail_id' : result[2],
                        'worker_name' : result[3],
                        'address' : result[4],
                        'amount' : result[5],
                        'job_Description' : result[6],
                        'worker_profession' : result[9],
                        'workers_experience' : result[10],
                     
            
                        }
            else:
                content = {
                        'recruiter_id' : result[0],
                        'worker_id' : result[1],
                        'job_title' : result[13],
                        'job_detail_id' : result[2],
                        'worker_name' : result[3],
                        'address' : result[4],
                        'amount' : result[5],
                        'job_Description' : result[6],
                        'worker_profession' : result[11],
                        'workers_experience' : result[12],
                        
            
                        }

            payload.append(content)

    return Response(data=payload, status=status.HTTP_200_OK)




@api_view(['GET'])
@permission_classes([IsAuthenticated])
def wokers_requests(request,user_id):
    cursor=connection.cursor()
    cursor.execute(

    """select recruiter_id, worker_id, job_title, job_detail_id, name,address , job_Description , 
    category_1 , category_1_vc, category_2, category_2_vc, category_3 , category_3_vc 
    from authapp_user u 
    INNER JOIN authapp_workerdetails w on u.id = w.user_id  
    INNER JOIN authapp_workersrequests r on u.id = r.worker_id 
    INNER JOIN authapp_jobdetails j on  j.id  = r.job_detail_id 
    """
    )
  
    row = cursor.fetchall()
    print(row)
    content = {}
    payload = []
    for result in row:
        if result[1] == user_id:
            if result[2] == result[7]:
                content = {
                        'recruiter_id' : result[0],
                        'worker_id' : result[1],
                        'job_title' : result[2],
                        'job_detail_id' : result[3],
                        'recruiter_name' : result[4],
                        'address' : result[5],
                        'job_Description' : result[6],
                        'workers_visiting_charges' : result[8],
            
                        }
            elif result[2] == result[9]:
                content = {
                      'recruiter_id' : result[0],
                        'worker_id' : result[1],
                        'job_title' : result[2],
                        'job_detail_id' : result[3],
                        'recruiter_name' : result[4],
                        'address' : result[5],
                        'job_Description' : result[6],
                        'workers_visiting_charges' : result[10],
                     
            
                        }
            else:
                content = {
                      'recruiter_id' : result[0],
                        'worker_id' : result[1],
                        'job_title' : result[2],
                        'job_detail_id' : result[3],
                        'recruiter_name' : result[4],
                        'address' : result[5],
                        'job_Description' : result[6],
                        'workers_visiting_charges' : result[12],
                        
            
                        }

            payload.append(content)

    return Response(data=payload, status=status.HTTP_200_OK)


