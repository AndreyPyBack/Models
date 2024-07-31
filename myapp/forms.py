# forms.py
from django import forms
from django.contrib.auth.models import User
from .models import Book
from .models import Course, Student
from .models import Profile


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']


class CourseForm(forms.ModelForm):
    students = forms.ModelMultipleChoiceField(queryset=Student.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Course
        fields = ['name', 'students']


class UserProfileForm(forms.ModelForm):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    bio = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Profile
        fields = ['username', 'email', 'password', 'bio']

    def save(self, commit=True):
        # Создаем пользователя
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password']
        )
        # Создаем профиль, привязывая его к пользователю
        profile = Profile(user=user, bio=self.cleaned_data['bio'])
        if commit:
            profile.save()
        return profile
