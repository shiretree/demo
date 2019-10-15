from django import forms
from .models import Student

class StudentForm(forms.ModelForm):            #此处必须导入forms.ModelForm， 而不能导入forms.Form，两个实现不一样；一般情况下，
                                               # 如果要将表单中的数据写入数据库或者修改某些记录的值，就要让表单类继承ModelForm;
                                               # 如果提交表单后 不会对数据库就行修改，则继承Form类。
    """name = forms.CharField(label='姓名', max_length=128)
    sex = forms.ChoiceField(label='性别', choices=Student.SEX_ITEM)
    profession = forms.CharField(label='职业', max_length=128)
    email = forms.CharField(label='电邮', max_length=128)
    qq = forms.CharField(label='QQ', max_length=128)
    phone = forms.CharField(label='手机号', max_length=128)

    def clean_qq(self):
        cleaned_data = self.cleaned_data['qq']
        if not cleaned_data.isdigit():
            raise forms.ValidationError('必须是数字!')
        return int(cleaned_data)"""
    class Meta:
        model = Student
        fields = (
            'name', 'sex', 'profession',
            'email', 'qq', 'phone'
        )