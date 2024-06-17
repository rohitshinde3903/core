from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    Students = [
        {"Name" : "Rohit", "age" : 21},
        {"Name" : "Divyansh", "age" : 25},
        {"Name" : "Sarthak", "age" : 1},
        {"Name" : "Akshit", "age" : 22},
        {"Name" : "Shantanu", "age" : 15},
        {"Name" : "Shrideep", "age" : 11},
        {"Name" : "Mandar", "age" : 10}
    ]
    
    # Name = str(input("Write Name; "))
    # age = int(input("Add Age; "))
    
    # for i in range (1):
    #     taked = {}
    #     taked["Name"] = Name
    #     taked["age"] = age
    #     Students.append(taked)
    # print(taked)
    # print(Students)
    return render(request, "index.html", context= {"Students": Students})



def about(request):
     return render(request, "about.html")

def contact(request):
     return render(request, "contact.html")