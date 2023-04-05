from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from firstapp.models import Hotel,Orders1,Reservation,Reserve,Book,Room,Comment,FoodOrder
from django.contrib.auth.models import User,auth
from datetime import date
# Create your views here.
def index(request):
    return render(request,'firstapp/index.html')
def about(request):
    return render(request,'firstapp/about us.html')
def service(request):
    return render(request,'firstapp/service.html')
def gallery(request):
    h=Hotel.objects.all()
    return render(request,'firstapp/gallery.html',context={"dict":h})
def reservation(request):
    if(request.method=='POST'):
        name=request.POST['uname']
        mno=request.POST['mno']
        email=request.POST['email']
        indate=request.POST['cdate']
        outdate=request.POST['odate']
        yin=int(indate[0:4])
        min=int(indate[5:7])
        din=int(indate[8:10])
        yout=int(outdate[0:4])
        mout=int(outdate[5:7])
        dout=int(outdate[8:10])
        if(min==mout):
            c=dout-din
        else:# 30/11  01/01
            dict={1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
            c=dict[min]-din+dout
            k=mout-min
            month=min+1
            if(month>12):
                month=1
            while(month!=mout):
                c=c+dict[month] 
                month+=1
                if(month>12):
                    month=1

        if(c==0):
            c=1
        c=c*2000
        return render(request,'firstapp/payment.html',{'name':name,'mno':mno,'email':email,'indate':indate,'outdate':outdate,'c':c})
        
    else:
        return render(request,'firstapp/reservation.html')
def payment(request):
    if(request.method=='POST'):
        name=request.POST['name']
        mno=request.POST['mno']
        email=request.POST['email']
        indate=request.POST['cdate']
        outdate=request.POST['odate']
        obj=Room.objects.all()
        yin=int(indate[0:4])
        min=int(indate[5:7])
        din=int(indate[8:10])
        room=1
        con=0
        for i in obj:
            yout=int(i.outdate[0:4])
            mout=int(i.outdate[5:7])
            dout=int(i.outdate[8:10])
            if(yin>yout):
                room=i.room
                con=1
                i.delete()
                break
            elif((yin==yout) and (min>mout)):
                room=i.room
                con=1
                i.delete()
                break
            elif((yin==yout)and(min==mout)and(din>dout)):
                room=i.room
                con=1
                i.delete()
                break
        if(con==0):
            l=[]
            for i in obj:
                c=i.room
                l.append(int(c))
            if(len(l)==0):
                room=1
            else:
                room=max(l)+1
        if(int(room)>10):
            messages.info(request,'Rooms are fully booked ...Try next time')
            return redirect('/info/')
        else:
            room1=Room(name=name,mno=mno,email=email,indate=indate,outdate=outdate,room=room)
            room1.save()
            messages.info(request,'Your room has been booked successfully.You are alloted with room no :'+str(room))
            return redirect('/info/')
    else:
        return render(request,'firstapp/payment.html')
def bill(request):
    if(request.method=='POST'):
        name=request.POST['uname']
        dname=request.POST['dname']
        price=request.POST['price']
        d=date.today()
        f=FoodOrder(name=name,dname=dname,price=price,date=d)
        f.save();
        messages.info(request,'Your food has been ordered successfully !')
        return redirect('/info/')
    else:
        return render(request,'firstapp/bill.html')
def info(request):
    return render(request,'firstapp/info.html')
def contact(request):
    if(request.method=="POST"):
        name=request.POST['name']
        email=request.POST['email']
        mno=request.POST['pno']
        comments=request.POST['comments']
        comment=Comment(name=name,email=email,mno=mno,comments=comments)
        comment.save()
        return redirect('/')
    else:
        return render(request,'firstapp/contact us.html')
def order(request):
    if(request.method=='POST'):
        dname=request.POST['dname']
        amount=request.POST['amount']
        qty=request.POST['qty']
        c=int(amount)*int(qty)
        return render(request,'firstapp/bill.html',{'price':c,'amount':amount,'dname':dname})
    else:
        o=Orders1.objects.all()
        return render(request,'firstapp/order.html',context={"Orders":o})
def login(request):
    if(request.method=='POST'):
        username=request.POST['uname']
        password=request.POST['password1']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('/login/')
        
    else:
        return render(request,'firstapp/login.html')
def signup(request):
    if(request.method=='POST'):
        name=request.POST['uname']
        email=request.POST['email']
        password=request.POST['password']
        password1=request.POST['password1']
        if(password==password1):
            if(User.objects.filter(username=name).exists()):
                messages.info(request,'Username Taken')
                return redirect('/signup/')
            elif(User.objects.filter(email=email).exists()):
                messages.info(request,'Email Taken')
                return redirect('/signup/')
            else:
                user=User.objects.create_user(username=name,email=email,password=password)
                user.save()
                print('User created')
        else:
            messages.info(request,'Password mismatched !')
            return redirect('/signup/')
            
        return redirect('/login/')
    else:
        return render(request,'firstapp/signup.html')
def logout(request):
    auth.logout(request)
    return redirect('/')

