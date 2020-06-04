from django import forms
from .models import AuthUser, FoodIntake, Food, CaloriesBurnedTraining, Training


class UserGoalForm(forms.ModelForm):
    class Meta:
        model = AuthUser
        fields = {
            'tdee',
            'weight',
            'height'
        }
        labels = {
            'tdee': 'Your daily calories goal is:',
            'weight': 'Your weight is:',
            'height': 'Your height is:'
        }


class AddFoodForm(forms.ModelForm):
    class Meta:
        model = FoodIntake
        exclude = ['date', 'food_id', 'user_id', 'id', 'amount']


class UpdateFoodQtyForm(forms.ModelForm):
    class Meta:
        model = FoodIntake
        # exclude = ['date', 'food_id', 'user_id', 'id', 'amount']
        fields = ['amount']


class DeleteFoodIntakeForm(forms.ModelForm):
    class Meta:
        model = FoodIntake
        exclude = ['date', 'food_id', 'user_id', 'id', 'amount']



class CreateFoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['food_name', 'kcal_100g', 'protein', 'carbs', 'fat']
        widgets = {
            'food_name': forms.Textarea(attrs={'rows': 1, 'cols': 15}),
        }


class AddExerciseForm(forms.ModelForm):
    class Meta:
        model = CaloriesBurnedTraining
        exclude = ['user_id', 'date', 'training_id']


class DeleteExerciseForm(forms.ModelForm):
    class Meta:
        model = CaloriesBurnedTraining
        exclude = ['user_id', 'date', 'training_id']


class CreateExerciseForm(forms.ModelForm):
    class Meta:
        model = Training
        fields = ['training_name', 'calories_burned']
        widgets = {
            'training_name': forms.Textarea(attrs={'rows': 1, 'cols': 15}),
        }