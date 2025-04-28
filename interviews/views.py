from django.shortcuts import render , HttpResponse , redirect , get_object_or_404
from .models import Interview ,Comment,FavoriteInterview
from .form import InterviewForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST


# Create your views here.
def index(request):
    if request.POST :   # 如果送過來的request 是 POST  
        form = InterviewForm(request.POST)
        interview = form.save(commit=False)
        interview.user = request.user
        interview.save()
        # # 收集、新增資料：
        # # 收集資料  （從表單傳送過來的 POST 資料中取得每個欄位的值）
        # company_name = request.POST["company_name"]   #company_name(變數名稱) = 帶入 POST 請求帶進來的 company_name （HTML 中的<input name="company_name"> ）這個 的 value
        # position = request.POST["position"]         
        # interview_date = request.POST["interview_date"]
        # review = request.POST["review"]
        # result = request.POST["result"]
        # rating = request.POST["rating"]
        
        # # 新增 
        # interview = Interview.objects.create(   # 針對 Interview 這個 Model（在model.py的建立的） ，使用 Django 的Object中的create功能 新增這筆資料到資料庫
        #     company_name = company_name,    #  model 中的 欄位名稱   =  （收集進來的變數名稱）上面收集資料使用的 變數名稱
        #     position = position,
        #     interview_date =interview_date,
        #     review = review,
        #     result = result,
        #     rating = rating

        # )

        # return redirect("/interviews")
        # return redirect("interviews:index")
        return redirect("interviews:show",interview.id) 

    else:
        interviews = Interview.objects.order_by("-id")
        return render(
            request,
            "interviews/index.html",
            {"interviews":interviews},
        )

@login_required
def new(request):
    form = InterviewForm    # 新增一個變數 form
    return render(
        request,
        "interviews/new.html",
        {"form":form},
        )

@login_required
def show(request,id):
    interview = get_object_or_404(Interview,pk=id) 
    if request.POST : 
        form = InterviewForm(request.POST,instance=interview)
        form.save()
        return  redirect("interviews:show",interview.id) 

   # if request.POST :       #（舊版本） 
        company_name = request.POST["company_name"]   
        position = request.POST["position"]         
        interview_date = request.POST["interview_date"]
        review = request.POST["review"]
        result = request.POST["result"]
        rating = request.POST["rating"]

        interview = get_object_or_404(Interview,pk=id)  # 把 這筆 interview 挑出來，然後：

        interview.company_name = company_name 
        interview.position = position
        interview.interview_date =interview_date
        interview.review = review
        interview.result = result
        interview.rating = rating

        #更新
        interview.save()
        return  redirect("interviews:show",interview.id) 


    else:
        # interview = Interview.objects.get(pk=id)  #  pk =  primary key 主鍵  # 這個沒有引號的interview 可以改名字 interview_info 什麼都可以
        # interview = get_object_or_404(Interview,pk=id) 這樣也可以  ，可以直接搬到外面
        #comments = Comment.objects.filter(interview=interview)  #(interview_id=id)也可以
        comments = interview.comment_set.all()
        return render(
            request,
            "interviews/show.html",
            {"interview":interview,"comments":comments}
            )

@login_required
def edit(request,id):
    interview = get_object_or_404(Interview,pk=id)
    form = InterviewForm(instance=interview)
    return render(
        request,
        "interviews/edit.html",
        {"interview":interview,
         "form":form,
        },
    )

@login_required
def delete(request,id):
    interview = get_object_or_404(Interview,pk=id)
    interview.delete()

    return redirect("interviews:index")

@require_POST
@login_required
def comment(request,id):
    interview = get_object_or_404(Interview,pk=id)

    # Comment.objects.create(
    #     content = request.POST["content"],
    #     interview_id = id,
    # )

    interview.comment_set.create(
        content=request.POST["content"],
        user=request.user,)   ## 新增comment 

  
    return redirect('interviews:show',interview.id)


# @require_POST
# @login_required
# def favorite(request,id):
#     interview = get_object_or_404(Interview,pk=id)
#     user = request.user
#     f = FavoriteInterview.objects.filter(user=user,interview=interview)

#     if f:
#         f.delete()
#     else:
            
#         FavoriteInterview.objects.create(user=user,interview=interview)

#     return redirect('interviews:show',interview.id)

@require_POST
@login_required
def favorite(request,id):
    interview = get_object_or_404(Interview,pk=id)
    favorite = request.user.favorited_interviews
    

    if favorite.filter(pk=interview.pk).exists():
        favorite.remove(interview)
    else:
        favorite.add(interview)

    return render(request,
                  'interviews/favorite.html',
                  {
                    'user': request.user , 
                   'interview':interview
                   },
                   )
    # return redirect('interviews:show',interview.id)