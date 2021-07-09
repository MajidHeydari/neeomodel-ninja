from django.http import JsonResponse
from .models import Person,City
from django.views.decorators.csrf import csrf_exempt
import json


def getAllPersons(request):
    if request.method == 'GET':
        try:
            persons = Person.nodes.all()
            response = []
            for person in persons :
                obj = {
                    "uid": person.uid,
                    "name": person.name,
                    "age": person.age,
                }
                response.append(obj)
            return JsonResponse(response, safe=False)
        except:
            response = {"error": "Error occurred"}
            return JsonResponse(response, safe=False)

def getAllCities(request):
    if request.method == 'GET':
        try:
            cities = City.nodes.all()
            response = []
            for city in cities:
                obj = {
                    "code": city.code,
                    "name": city.name,
                }
                response.append(obj)
            return JsonResponse(response, safe=False)
        except:
            response = {"error": "Error occurred"}
            return JsonResponse(response, safe=False)

@csrf_exempt
def personDetails(request):
    if request.method == 'GET':
        # get one person by name
        name = request.GET.get('name', ' ')
        try:
            person = Person.nodes.get(name=name)
            response = {
                "uid": person.uid,
                "name": person.name,
                "age": person.age,
            }
            return JsonResponse(response, safe=False)
        except :
            response = {"error": "Error occurred"}
            return JsonResponse(response, safe=False)

    if request.method == 'POST':
        # create one person
        json_data = json.loads(request.body)
        name = json_data['name']
        age = int(json_data['age'])
        try:
            person = Person(name=name, age=age)
            person.save()
            response = {
                "uid": person.uid,
            }
            return JsonResponse(response)
        except :
            response = {"error": "Error occurred"}
            return JsonResponse(response, safe=False)

    if request.method == 'PUT':
        # update one person
        json_data = json.loads(request.body)
        name = json_data['name']
        age = int(json_data['age'])
        uid = json_data['uid']
        try:
            person = Person.nodes.get(uid=uid)
            person.name = name
            person.age = age
            person.save()
            response = {
                "uid": person.uid,
                "name": person.name,
                "age": person.age,
            }
            return JsonResponse(response, safe=False)
        except:
            response = {"error": "Error occurred"}
            return JsonResponse(response, safe=False)

    if request.method == 'DELETE':
        # delete one person
        json_data = json.loads(request.body)
        uid = json_data['uid']
        try:
            person = Person.nodes.get(uid=uid)
            person.delete()
            response = {"success": "Person deleted"}
            return JsonResponse(response, safe=False)
        except:
            response = {"error": "Error occurred"}
            return JsonResponse(response, safe=False)

@csrf_exempt
def cityDetails(request):
    if request.method == 'GET':
        # get one city by name
        name = request.GET.get('name', ' ')
        try:
            city = City.nodes.get(name=name)
            response = {
                "code": city.code,
                "name": city.name,
            }
            return JsonResponse(response, safe=False)
        except :
            response = {"error": "Error occurred"}
            return JsonResponse(response, safe=False)

    if request.method == 'POST':
        # create one city
        json_data = json.loads(request.body)
        name = json_data['name']
        code = json_data['code']
        try:
            city = City(name=name, code=code)
            city.save()
            response = {
                "code": city.code,
            }
            return JsonResponse(response)
        except :
            response = {"error": "Error occurred"}
            return JsonResponse(response, safe=False)

    if request.method == 'PUT':
        # update one city
        json_data = json.loads(request.body)
        name = json_data['name']
        code = json_data['code']
        try:
            city = City.nodes.get(code=code)
            city.name = name
            city.save()
            response = {
                "code": city.code,
                "name": city.name,
            }
            return JsonResponse(response, safe=False)
        except:
            response = {"error": "Error occurred"}
            return JsonResponse(response, safe=False)

    if request.method == 'DELETE':
        # delete one city
        json_data = json.loads(request.body)
        code = json_data['code']
        try:
            city = City.nodes.get(code=code)
            city.delete()
            response = {"success": "City deleted"}
            return JsonResponse(response)
        except:
            response = {"error": "Error occurred"}
            return JsonResponse(response, safe=False)

@csrf_exempt
def connectPaC(request):
    if request.method == 'PUT':
        json_data = json.loads(request.body)
        uid = json_data['uid']
        code = json_data['code']
        try:
            person = Person.nodes.get(uid=uid)
            city = City.nodes.get(code=code)
            res = person.city.connect(city)
            response = {"result": res}
            return JsonResponse(response, safe=False)
        except:
            response = {"error": "Error occurred"}
            return JsonResponse(response, safe=False)

@csrf_exempt
def connectPaP(request):
    if request.method == 'PUT':
        json_data = json.loads(request.body)
        uid1 = json_data['uid1']
        uid2 = json_data['uid2']
        try:
            person1 = Person.nodes.get(uid=uid1)
            person2 = Person.nodes.get(uid=uid2)
            res = person1.friends.connect(person2)
            response = {"result": res}
            return JsonResponse(response, safe=False)
        except:
            response = {"error": "Error occurred"}
            return JsonResponse(response, safe=False)