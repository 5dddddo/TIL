from django.shortcuts import render
from faker import Faker
from jobs.models import Job
import requests

# Create your views here.
def index(request):
    return render(request, 'jobs/index.html')

def name(request):
    name = request.POST.get('user_name')
    user = Job.objects.filter(name=name).first()
    
    if user:
        past_job = user.past_job
    else:
        fake = Faker()
        past_job = fake.job()
        job = Job(name=name, past_job=past_job)
        job.save()

    url = 'http://api.giphy.com/v1/gifs/search?api_key=oy272gv1gR7LNMg7ZKcb1wV0H4QxL6Pi&q=' + past_job
    response = requests.get(url).json()
    result = response['data'][0]['images']['original']['url']
    
    context= {
        'name' : name,
        'past_job' : past_job,
        'result' : result,
    }

    return render(request,'jobs/name.html', context)

