from django.contrib.auth import authenticate, login, logout,authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,Http404,get_object_or_404, HttpResponseRedirect, redirect,HttpResponse
from django.utils.safestring import mark_safe
import datetime
from datetime import time
from django.urls import reverse
from django.contrib import messages
from django.conf import settings
# from django.db import IntegrityError
from django.core.exceptions import ValidationError
from django.contrib.admin.views.decorators import staff_member_required
from django.template.loader import render_to_string
from .forms import LoginForm, RegisterForm,ProfileEditForm,RegisterUserForm
from .models import MyUser,Gallery,Courses,OnlineClass,OnlineVideo,Testimonial,SatisfiedClient,Registeration,Calendar,Resources,AddCourses,PlayerStatistic
from django.contrib.messages import get_messages
from django.http import JsonResponse
import re

# from django.contrib.auth.views import password_change
# from django.contrib.auth.views import password_change_done
# from django.contrib.auth.views import password_reset
# from django.contrib.auth.views import password_reset_done
# from django.contrib.auth.views import password_reset_confirm
# from django.contrib.auth.views import password_reset_complete
from django.core.mail import send_mail
from datetime import datetime, timedelta
from django.utils import timezone
from .models import TestAnswer,TestQuestion
import re
import json
import xlwt
import math
# import pandas as pd
import csv                




def answer():
    question=TestQuestion.objects.all()
    with open('ans.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row, quest in zip(reader,question):
            # if len(row) > 5:
                choice1 = row['OPTION1']
                choice2 = row['OPTION2']
                choice3 = row['OPTION3']
                choice4 = row['OPTION4']
                # choice5 = row['choice5']
                correct_answer = row['ANSWER']
                get_answer=TestAnswer(choice1=choice1,choice2=choice2,choice3=choice3,choice4=choice4,correct_answer=correct_answer,questions=quest)
                get_answer.save()
            # else:
            #     choice1 = row['choice1']
            #     choice2 = row['choice2']
            #     choice3 = row['choice3']
            #     choice4 = row['choice4']
            #     correct_answer = row['correct_answer']
            #     get_answer=JMathAnswer(choice1=choice1,choice2=choice2,choice3=choice3,choice4=choice4,correct_answer=correct_answer,questions=quest)
            #     get_answer.save()


def question(request):
    # question=LevelOneQuestion.objects.all()
    with open('question.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            content = row['QUESTIONS']
            poster = request.user
            get_question = TestQuestion(content=content,poster=poster)
            get_question.save()

def del_answer():
    test = TestAnswer.objects.all()
    for ans in test:
        ans.delete()
    return test
    

# from itertools import chain
def del_question():
    test=TestQuestion.objects.all()
    for ans in test:
        ans.delete()
    return question


def load_question(request):
    answer()

    return HttpResponse("Questions Loading Activity Successful")


def validate_input(*args):
		check_against = re.compile(r'[a-zA-Z0-9 ]*$')
		false_arr=[]
		true_arr=[]
		for val in args:
			if check_against.match(val):
					true_arr.append(val)
					# print(true_arr)
			else:
					false_arr.append(val)
		if len(false_arr) > 0:
				return False
		return True

def register_user(request):
	register_form = RegisterUserForm(request.POST or None)
	context = {"register_form": register_form}
	if request.method == 'POST':
		if register_form.is_valid():
			username= register_form.cleaned_data['username']
			password= register_form.cleaned_data['password2'] 
			full_name = register_form.cleaned_data['full_name']
			email = register_form.cleaned_data['email']
			sex = register_form.cleaned_data.get('sex')
			mobile=register_form.cleaned_data['mobile']
			# pick_your_course=register_form.cleaned_data['pick_your_course']
			occupation=register_form.cleaned_data['occupation']

			detail = register_form.save(commit=False)
			detail.is_test_user = False
			detail.ip_address=get_ip(request)
			detail.set_password(password) 
			if validate_input(username,full_name,sex,occupation) == True:
				detail.save()
				try:
					mail_subject='%s Just Registered On LeadLeap'%full_name
					message = "Client Name:{} - Email:{} - Company:{} - Sex:{} - Occupation:{} -  Mobile:{} - Course:{}".format(full_name,email,sex,occupation,mobile,pick_your_course)
					to_email="aadmin@leadleapconsult.com"
					send_mail(mail_subject,email,message,[to_email])
					messages.success(request,"Successfully Registered")
					return redirect("/login")
				except:
					return redirect("/login")
			else:
				messages.error(request,"Invalid Input Details. Enter Valid Details")
				return render(request, "leadtkc/register.html", context)
		else:
			messages.error(request,"Not yet registered.Check for likely errors in your registeration form.")
	
	return render(request, "leadtkc/register.html", context)


def login_view(request):
    if not request.user.is_authenticated:
        form = LoginForm(request.POST or None)
        next_url = request.GET.get('next')
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if next_url is not None:
                    return HttpResponseRedirect(next_url)
                return HttpResponseRedirect("/")
        title = "Login"
        context = {
            "form": form,
            "title": title,
            }
        return render(request, "leadtkc/login.html", context)

    else:
        return HttpResponseRedirect("/")



def auth_logout(request):
	logout(request)
	#messages.success(request, "<strong>Successfully Logged out</strong>. Feel free to <a  href='%s'>login</a> again." %(reverse("login")), extra_tags='safe, abc')
	#return HttpResponseRedirect('%s'%(reverse("register")))
	return HttpResponseRedirect('/')




def dashboard(request,username):
    
	user = get_object_or_404(MyUser,username=username) 
	if not request.user.is_test_user:
		course = OnlineClass.objects.all().distinct('title')
		template = "leadtkc/dashboard.html"
		context={'course':course,"user":user}
		return render(request,"leadtkc/dashboard.html",context)
	else:
		redirect("/test/%s_testdashboard/"%request.user)


def test_dashboard(request,username):
	user = get_object_or_404(MyUser, username=username)
	context={"user":user}

	if user.is_test_user:
		template = "leadtkc/test/test.html"
		return render(request,"leadtkc/test/test.html",context)
	else:
		redirect("/test/%s_dashboard/"%request.user)
		return render(request,"leadtkc/dashboard.html",context)

def course_detail(request,username,course_title):
	# if request.user
	try:
		course = OnlineClass.objects.filter(slug=course_title)
		get_title = course[0].title
		course_title = get_title.upper()
		template = "leadtkc/video_detail.html"
		context={'course':course,'course_title':course_title}
		user_time = MyUser.objects.get(username=username,start_course__lte=datetime.now() - timedelta(days=14))
		# user_time.update(is_member=False)
		MyUser.objects.filter(username=username).update(is_member=False)
		messages.error(request,'Sorry your viewing time has expired. Contact us for more information')
		return render(request,template)
	except:	
		template = "leadtkc/video_detail.html"
		context={'course':course,'course_title':course_title}
		return render(request,template,context)


def get_ip(request):
	try:
		x_forward=request.META.get("HTTP_X_FORWARDED_FOR")
		if x_forward:
			ip=x_forward.split(",")[0]
		else:ip= request.META.get("REMOTE_ADDR")
	except:
			ip=""
	return ip

import uuid

def get_ref_id(request):
	ref_id=request.POST.get("username","")
	try:
		id_exists=MyUser.objects.get(ref_id=ref_id)
		get_ref_id()
	except:
		return ref_id

@login_required
def edit_studentprofile(request,username):
	user=get_object_or_404(MyUser,username=username)

	if request.method == 'POST':

		user_form = UserEditForm(instance=request.user,
                                 data=request.POST,files=request.FILES)
		profile_form = ProfileEditForm(instance=user.profile_user,
                                       data=request.POST,
                                       files=request.FILES)
		if user_form.is_valid() and profile_form.is_valid():
			user_form.image = user_form.cleaned_data['image']
			user_form.save()
			profile_form.save()
			messages.success(request, 'Profile updated successfully')
			return HttpResponseRedirect("/%s/student_profile/"%request.user)
		else:
			messages.error(request, 'Error updating your profile')
	else:
		user_form = UserEditForm(instance=request.user)
		profile_form = ProfileEditForm(instance=request.user.profile_user)

		#count=MyUser.objects.filter(friend=join_obj).count()
	return render(request, 'leadtkc/edit_studentprofile.html', {'user':user,'user_form': user_form,'profile_form': profile_form})#"count"

def auth_register(request):
	course=Courses.objects.all()
	logos = SatisfiedClient.objects.all()
	add_course=AddCourses.objects.all()
	resource=Resources.objects.all()
	gallery=Gallery.objects.all()
	testimonial=Testimonial.objects.all()
	calendar=Calendar.objects.all().order_by("-created_at")[:5]
	if  request.POST:
			register_form = RegisterForm(request.POST)

			if register_form.is_valid():

					name = register_form.cleaned_data['name']
					email = register_form.cleaned_data['email']
					sex = register_form.cleaned_data['sex']
					company=register_form.cleaned_data['company']
					occupation = register_form.cleaned_data['occupation']
					pick_your_course = register_form.cleaned_data['pick_your_course']
					mobile=register_form.cleaned_data['mobile']
					is_test_user= True
					detail=register_form.save(commit=False)
					detail.ip_address=get_ip(request)
					if validate_input(name,sex,company,occupation) == True:
						detail.save()

							
						# mail_subject='%s Just Registered On LeadLeap'%name
						# message = "Client Name:{} - Email:{} - Company:{} - Sex:{} - Occupation:{} -  Mobile:{} - Course:{}".format(name,email,company,sex,occupation,mobile,pick_your_course)
						# to_email="Info@leadleapconsult.com"
						# send_mail(mail_subject,email,message,[to_email])
						messages.success(request, "<strong>Successfully Registered </strong>")
						context = {"add_course":add_course,"logos":logos,"testimonial":testimonial,"resource":resource,"gallery":gallery,"register_form": register_form,"calendar":calendar,"course":course}
						return render(request, "leadtkc/home.html", context)
					else:
						messages.error(request, "<strong>Invalid Input Detail. Please Input Valid Characters. </strong>")
						context = {"add_course":add_course,"logos":logos,"testimonial":testimonial,"resource":resource,"gallery":gallery,"register_form": register_form,"calendar":calendar,"course":course}
						return render(request, "leadtkc/home.html", context)
			else:
					messages.error(request,"Invalid Details Detected.Kindly Correct Them")
					# context = {"testimonial":testimonial,"logos":logos,"resource":resource,"gallery":gallery,"register_form": register_form,"calendar":calendar,"course":course}
					return render(request, "leadtkc/home.html", {"logos":logos,"add_course":add_course,"testimonial":testimonial,"logos":logos,"resource":resource,"gallery":gallery,"register_form": register_form,"calendar":calendar,"course":course})

	else:
		register_form=RegisterForm()

		#register_form=RegisterForm()
	return render(request, 'leadtkc/home.html', {"add_course":add_course,"logos":logos,"testimonial":testimonial,"resource":resource,"gallery":gallery,"register_form":register_form,"calendar":calendar,"course":course})

def user_test(request):
	if request.method == 'POST':
		get_info = request.POST
		name = get_info.get("name")
		email = get_info.get("email")
		mobile = get_info.get("mobile")
		company = get_info.get("company1").lower()
		department = get_info.get("department").lower()
		password = get_info.get("password")
		result=[name,email,mobile,company,mobile,department]
		if len(result) == 6:

			try:
				if MyUser.objects.filter(full_name=name):
					messages.error(request,"Name already in use")
					return render(request,'leadtkc/test/test_register.html')

				if MyUser.objects.filter(email=email):
					messages.error(request,"Email already in use")
					return render(request,'leadtkc/test/test_register.html')

				if MyUser.objects.filter(mobile=mobile):
					messages.error(request,"Mobile already in use")
					return render(request,'leadtkc/test/test_register.html')

				if len(password) > 1 and len(password) < 6:
					messages.error(request,"Password must be greater than 6 characters")
					return render(request,'leadtkc/test/test_register.html')

				elif len(password) >= 6:  
					username = "".join(name.split(" ")).lower()
					if validate_input(company,department,name,mobile) == True:
    						
						user = MyUser(is_test_user=True,username=username,email=email,mobile=mobile,full_name=name,occupation=department,company=company)
						user.set_password(password)
						user.save()
						messages.success(request,"Successfully Logged in")
						return redirect('/test/{}_testdashboard'.format(username))
					else:
						messages.error(request,"Invalid Input Details. Enter Valid Details.")
						return render(request,'leadtkc/test/test_register.html')	
			except ValidationError as e:				
				error = e.args[0].split("=")[1]
				messages.error(request,"{}".format(error))
				print(messages.error)
				return render(request,'leadtkc/test/test_register.html')


	else:
		course_outline = AddCourses.objects.all()
		crs = [re.sub('[^A-Za-z0-9]+','',"".join(course.title.split(" ")).lower()) for course in course_outline]
    			
		return render(request,'leadtkc/test/test_register.html')

def submit_test(request,username):
		user=get_object_or_404(MyUser,username=username)
		data =dict()
		start_timer=0
		time_differ=0
		time_diff_arr= range(1,800)
		test_ans=TestAnswer.objects.all()
		context= {"test":test_ans}
		time_start = request.POST.get('time_start',)
		# print("timestart",time_start)
		if time_start:
			import time
			start_timer = time.time()
			# print("Hello start timer",start_timer)
			request.session["get-timer"]=start_timer
			data["reveal_question"] = render_to_string('leadtkc/test/test_partial.html', context)
		time_end = request.POST.get("end_time",)
		import time
		actual_time = math.floor(time.time() - request.session["get-timer"])
		if time_end or actual_time in time_diff_arr:
			end_timer=time.time()
			time_differ = math.floor(end_timer - request.session["get-timer"])
			if time_differ in time_diff_arr:
				score=0
				if request.method == 'POST':
					num_score=test_ans
					score_count=request.POST.getlist('answer[]',None)
					score_point=request.POST.getlist('ran_score',None)
					if type(score_point) == "<class 'list'>" :
						score_point=int(score_point[0])
					elif score_point == None:
						score_point=0

					correct_ans=[correct.correct_answer for correct in num_score]
					if score_count:
						contained=[a for a in score_count if a in correct_ans]
						for scores in contained:
							score+=5

						data['user_score']=score
					else:
						data["score_status"]="Score too low" 

					now=datetime.now()
					time=[9,12,15,18]
					if score > 0:
						PlayerStatistic.objects.create(player=user,score=score,mobile=user.mobile,name=user.full_name,company=user.company,department=user.occupation)
						data["thanks"]="Thank you for taking the assessment"
			else:
				data["busted"]="Hey! I can see You Cheating Backoff. "				
		return JsonResponse(data)



def take_test(request,username):
		user=get_object_or_404(MyUser,username=username)
		template ="leadtkc/test/test_question.html"
		context = {"user":user}
		candidate = PlayerStatistic.objects.filter(player=user).count()
		if candidate == 1:
			messages.error(request,"You have taken this test before")
			return redirect(f"/test/{username}_testdashboard")
		else:
			return render(request,template,context)


# def leadleap_test(request,username):
# 		user=get_object_or_404(MyUser,username=username)
# 		template ="leadtkc/test/leadleapTest.html"
# 		context = {"user":user}
# 		candidate = PlayerStatistic.objects.filter(player=user).count()
# 		if candidate == 1:
# 			messages.error(request,"You have taken this test before")
# 			return redirect(f"/test/{username}_testdashboard")
# 		else:
# 			return render(request,template,context)


def report(request,username):
	user=get_object_or_404(MyUser,username=username)
	template ="leadtkc/test/report.html"
	context = {"user":user}
	report = None
	if request.user.is_head or request.user.is_admin:
		if request.user.is_head:
			c_name = request.user.company.split(" ")[0]
			c_name2 = request.user.company.split(" ")[1]
			combine_name = c_name + " " + c_name2
			report = PlayerStatistic.objects.filter(company__icontains=combine_name)
		elif request.user.is_admin:
			report = PlayerStatistic.objects.all()
		context["report"] = report
		return render(request,template,context)
	else:
		messages.error(request,"You dont have permission to view this report")
		return redirect("/")

def download_excel_data(request,username):
	user=get_object_or_404(MyUser,username=username)
	data = None
	if user.is_head or request.user.is_admin:
			if user.is_head:
				c_name = request.user.company.split(" ")[0]
				c_name2 = request.user.company.split(" ")[1]
				combine_name = c_name + " " + c_name2
				data = PlayerStatistic.objects.filter(company__icontains=combine_name)
			elif user.is_admin:
				data = PlayerStatistic.objects.all()
			response=HttpResponse(content_type='application/ms-excel')
			response['Content-Disposition'] = 'attachment; filename="report_excel_data_%s.xls"'%datetime.now()
			wb= xlwt.Workbook(encoding='utf-8')
			ws= wb.add_sheet("sheet1")
			row_num = 0
			font_style = xlwt.XFStyle()
			font_style.font.bold =True
			columns= ['Full Name','Email','Phone Number','Department','Company','Score']
			for col_num in range(len(columns)):
				ws.write(row_num, col_num, columns[col_num], font_style)
			font_style =xlwt.XFStyle()
			for my_row in data:

				row_num = row_num + 1
				ws.write(row_num,0,my_row.name, font_style)
				ws.write(row_num,1,my_row.player.email, font_style)
				ws.write(row_num,2,my_row.mobile, font_style)
				ws.write(row_num,3,my_row.department,font_style)
				ws.write(row_num,4,my_row.company, font_style)
				ws.write(row_num,5,my_row.score, font_style)
			wb.save(response)
			return response
	else:
		messages.error(request,"You can only download reports with right permissions.")
		return redirect("/")

# def populate(request):
# 	users = MyUser.objects.all()
# 	get_user = [user for user in users]
# 	for play in get_user:
# 			try:
# 				PlayerStatistic.objects.filter(name=play.full_name).update(company=play.company.lower())
# 			except:
# 				pass
# 	return HttpResponse("Successfully Departed")