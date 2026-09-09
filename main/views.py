from django.shortcuts import render

from main.models import Experience


def show_main(request):
    context = {
        "name": "Fadlan Fathul Islam",
        "npm": "2506601275",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "A Computer Science student at Universitas Indonesia who has a big interest in machine learning and human behaviour. Currently at the 3rd semester and pushing for competition, research, and studying for data science and machine learning. Open to collaborate :D"
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Fadlan Fathul Islam",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)