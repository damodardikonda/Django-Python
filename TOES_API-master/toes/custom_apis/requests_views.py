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
def recruiters_requests(request):
    cursor=connection.cursor()
    #cursor.execute(f"select * from authapp_worker_Details where category_1 = '{category}' OR category_2 = '{category}' OR category_3 = '{category}' ")
    cursor.execute('select job_description, job_title, worker_id,amount from authapp_recruitersrequests r , authapp_jobdetails j where j.recruiter_id = r.recruiter')
    row = cursor.fetchall()
    content = {}
    payload = []
    for data in row:
        cursor.execute(f'select name, address, category_1, category_1_exp, category_2,category_2_exp,category_3,category_3_exp from authapp_user u INNER JOIN authapp_workerdetails w on u.id = w.user_id where u.id = {data[2]}')
        row = cursor.fetchall()
        for info in row:

            content = {
            'job_title': data[1],
            'job_description': data[0],
            'woker_id': data[2],
            'amount': data[3],
            'worker_name':info[0],
            'address':info[1],
            'category_1':info[2],
            'category_1_exp':info[3],
            'category_2':info[4],
            'category_2_exp':info[5],
            'category_3':info[6],
            'category_3_exp':info[7],
            }
        payload.append(content)

    return Response(data=payload, status=status.HTTP_200_OK)




@api_view(['GET'])
@permission_classes([IsAuthenticated])
def wokers_requests(request,worker_id):
    cursor=connection.cursor()
    cursor.execute(f'select job_description, job_title, recruiter_id  from authapp_jobdetails ,authapp_workersrequests where authapp_workersrequests.job_detail_id = authapp_jobdetails.id  and worker_id = {worker_id}')
    row = cursor.fetchall()
    content = {}
    payload = []
    for data in row:
        u_id = data[2] 
        cursor.execute(f'select name, address from authapp_user where id = {u_id}')
        row = cursor.fetchall()
        for info in row:
            content = {
                'job_title': data[1],
                'job_description': data[0],
                'recruiter_id': data[2],
                'recruiter_name':info[0],
                'address':info[1],
            
                }  
        
        
        
        payload.append(content)

    return Response(data=payload, status=status.HTTP_200_OK)


