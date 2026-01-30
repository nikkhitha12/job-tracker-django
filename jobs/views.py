from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Job

@login_required
def job_list(request):
    if request.method == 'POST':
        company = request.POST['company']
        role = request.POST['role']
        Job.objects.create(
            user=request.user,
            company=company,
            role=role
        )
        return redirect('jobs')

    jobs = Job.objects.filter(user=request.user)
    return render(request, 'jobs.html', {'jobs': jobs})
