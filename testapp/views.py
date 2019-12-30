from django.shortcuts import render, redirect
import os, hashlib, json, random, string
from PIL import Image
from . import models
from . import myserializers
from django.http import JsonResponse, HttpResponse
from django.conf import settings
from django.core.serializers.json import DjangoJSONEncoder
from django.views.decorators.csrf import csrf_exempt
from . import customValidation
# Create your views here.

@csrf_exempt
def user_login(request):
    try:
        if request.method == "POST":
            user_name = request.POST['user_name'].strip()
            user_password = request.POST['user_password'].strip()
            
            chkValidInput = customValidation.chkUserValidation(user_name, user_password)
            if chkValidInput == True:
                user_pass_hash = hashlib.md5(user_password.encode())
                getUserList = models.UserInfo.objects.filter(user_name = user_name, user_password = user_pass_hash.hexdigest(), status = True)
                if getUserList:
                    token = hashlib.md5(user_name.encode()+str(getUserList[0].user_full_name).encode()+str(getUserList[0].created_date).encode())
                    user_token = str(''.join(random.choice(string.ascii_letters + string.digits) for i in range(15)))+str(token.hexdigest())
                    request.session["user_token__"] = user_token
                    data = {
                        'message': "Login success",
                        'status': True, 
                        'user_token': user_token,
                    }
                    return JsonResponse(data, safe = False)
                else:    
                    request.session["user_token__"] = None
                    return JsonResponse({'message': 'Login failed. Username or password invalid', 'status': False}, safe = False)
            else:
                return JsonResponse({'message': chkValidInput, 'status': False}, safe = False)
        else:
            request.session["user_token__"] = None
            return JsonResponse({'message': 'Your request is not valid', 'status': False}, safe = False)       
    except:
        return JsonResponse({'message': 'request not valid', 'status': False}, safe = False)
            
def get_all_user(request):
    try:
        if request.method == "GET": 
            if request.session["user_token__"] == request.GET.get('user_token'):
                getUserList = models.UserInfo.objects.all()
                serializer = myserializers.UserInfoSerializer(getUserList, many=True)
                return JsonResponse(serializer.data, safe = False)
            else:
                return JsonResponse({'message': 'Please login then try', 'status': False}, safe = False)   
        else:
            return JsonResponse({'message': 'Your request is not valid', 'status': False}, safe = False)   
    except:
        return JsonResponse({'message': 'request not valid', 'status': False}, safe = False)
            
            
def dashboard(request):
    try:
        if request.method == "GET": 
            if request.session["user_token__"] == request.GET.get('user_token'):
                page_number = 0
                try:
                    page_number = int(request.GET.get('page_number')) 
                except:
                    pass

                inspection_list = models.InspectionInfo.objects.values('id','user_name','serial_number','action_taken','distributor_name_id__distributor_name','distributor_name_id__distributor_type','inspection_date','status').order_by("inspection_date")[page_number:][:10] 
                return HttpResponse(json.dumps(list(inspection_list), cls=DjangoJSONEncoder))
            else:
                return JsonResponse({'message': 'Please login then try', 'status': False}, safe = False)   
        else:
            return JsonResponse({'message': 'Your request is not valid', 'status': False}, safe = False)   
    except:
        return JsonResponse({'message': 'request not valid', 'status': False}, safe = False)
            
@csrf_exempt            
def create_inspection(request):
    try: 
        if request.method == "POST": 
            if request.session["user_token__"] == request.POST['user_token']:
                user_name         = request.POST['user_name'].strip()
                distributor_name  = request.POST['distributor_name']
                option_one        = request.POST['option_one']
                option_one_img    = request.POST['option_one_img']
                option_two        = request.POST['option_two']
                option_two_img    = request.POST['option_two_img']
                option_three      = request.POST['option_three']
                option_three_img  = request.POST['option_three_img']
                option_four       = request.POST['option_four']
                option_four_img   = request.POST['option_four_img']
                option_five       = request.POST['option_five']
                option_five_img   = request.POST['option_five_img']
                option_six        = request.POST['option_six']
                option_six_img    = request.POST['option_six_img']
                inspection_date   = request.POST['inspection_date'] 

                serial_number     = 10001 
                get_last_serial   = models.InspectionInfo.objects.order_by("-serial_number").first() 
                if get_last_serial:
                    serial_number = get_last_serial.serial_number+1

                models.InspectionInfo.objects.create(
                    user_name_id = user_name, serial_number = serial_number, distributor_name_id = distributor_name,
                    option_one = option_one, option_one_img = option_one_img, option_two = option_two, option_two_img = option_two_img,
                    option_three = option_three, option_three_img = option_three_img, option_four = option_four, option_four_img = option_four_img,
                    option_five = option_five, option_five_img = option_five_img, option_six = option_six, option_six_img = option_six_img, inspection_date = inspection_date
                ) 
                return JsonResponse({'message': 'Inpection save successful', 'status': True}, safe = False)   
            else:
                return JsonResponse({'message': 'Please login then try', 'status': False}, safe = False)   
        else:
            return JsonResponse({'message': 'Your request is not valid', 'status': False}, safe = False)   
    except:
        return JsonResponse({'message': 'request not valid', 'status': False}, safe = False) 

@csrf_exempt            
def find_single_inspection(request):
    try:
        if request.method == "POST": 
            if request.session["user_token__"] == request.POST['user_token']:
                inspection_list = models.InspectionInfo.objects.values('id','user_name','serial_number','action_taken','distributor_name_id__distributor_name','distributor_name_id__distributor_type','inspection_date','status').filter(serial_number = request.POST['serial_number']) 
                return HttpResponse(json.dumps(list(inspection_list), cls=DjangoJSONEncoder))
            else:
                return JsonResponse({'message': 'Please login then try', 'status': False}, safe = False)   
        else:
            return JsonResponse({'message': 'Your request is not valid', 'status': False}, safe = False)   
    except:
        return JsonResponse({'message': 'request not valid', 'status': False}, safe = False)  

                 
@csrf_exempt            
def set_fine_amount(request):
    try:
        if request.method == "POST": 
            if request.session["user_token__"] == request.POST['user_token']:
                fine_amount = float(request.POST['fine_amount'])
                issue_warning = None
                try:
                    issue_warning = request.POST['issue_warning']  
                except:
                    pass

                if fine_amount and issue_warning:
                    models.InspectionInfo.objects.filter(serial_number = request.POST['serial_number']).update(fine_amount = fine_amount, issue_warning = request.POST['issue_warning']) 
                    return JsonResponse({'message': 'Fine amount set successful', 'status': True}, safe = False)
                else:    
                    models.InspectionInfo.objects.filter(serial_number = request.POST['serial_number']).update(fine_amount = fine_amount) 
                    return JsonResponse({'message': 'Issue warning set successful', 'status': True}, safe = False) 
            else:
                return JsonResponse({'message': 'Please login then try', 'status': False}, safe = False)   
        else:
            return JsonResponse({'message': 'Your request is not valid', 'status': False}, safe = False)   
    except:
        return JsonResponse({'message': 'request not valid', 'status': False}, safe = False)  