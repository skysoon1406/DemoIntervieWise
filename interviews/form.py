from django.forms import ModelForm , DateInput
from .models import Interview

class InterviewForm(ModelForm):
    class Meta:
        model = Interview
        fields = [
            "company_name",
            "position",
            "interview_date",
            "result",
            "review",
            "rating",
        ]

        labels = {
            "company_name" :  "公司名稱",
            "position":  "面試職稱",
            "interview_date":  "面試日期",
            "review":  "面試心得",
            "result":  "面試結果",
            "rating":  "面試評價",
        }

        help_texts = {
            "company_name" :  "面試的公司名稱全名",
            "result":  "例：錄取/未錄取/無聲卡/錄取未到職",
            "rating":  "請輸入 1~10分的分數，1分=非常不滿意 ，10分=非常滿意",
        }

        widgets = {
            "interview_date":DateInput({ "type" :"date" })
        }

