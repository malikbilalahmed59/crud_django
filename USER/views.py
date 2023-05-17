from django.views import View
from django.shortcuts import render, redirect
from .models import UserInformation
from .forms import Userform
from django.http import JsonResponse

class HomeView(View):
    users = UserInformation.objects.all()
    form = Userform()

    def get(self, request):
        users = UserInformation.objects.all()
        context = {'users': users, 'form': self.form}
        return render(request, 'home.html', context)

    def post(self, request):
        if request.method == 'POST':
            form = Userform(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home')
        return render(request, 'home.html')

def  update(request,pk):
    users = UserInformation.objects.all()
    user =UserInformation.objects.get(id=pk)
    form=Userform(instance=user)
    if request.method == 'POST':
        form = Userform(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return redirect('home')
    context={'form':form,'users':users}
    return render(request,'update.html',context)
def delete(request,pk):
    user=UserInformation.objects.get(id=pk)
    if request.method=="POST":
        user.delete()
        return redirect('home')
    return render(request,'delete.html',{'obj':user})
        # id1 = request.GET.get('id', None)
        # first_name1 = request.GET.get('first_name', None)
        # last_name1 = request.GET.get('last_name', None)
        # email1 = request.GET.get('email', None)
        # # password1=request.GET.get('password', None)
        # # Cnic_number1=request.GET.get('Cnic_number', None)
        # # birth_date1=request.GET.get('birth_date', None)
        #
        # obj = UserInformation.objects.get(id=id1)
        # obj.first_name = first_name1
        # obj.last_name = last_name1
        # obj.email = email1
        # # obj.password = password1
        # # obj.Cnic_number=Cnic_number1
        # # obj.birth_date = birth_date1
        # obj.save()
        #
        # user = {'id':obj.id,'first_name':obj.first_name,'last_name':obj.last_name,'email':obj.email}
        #
        # data = {
        #     'user': user
        # }
        # return JsonResponse(data)