from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import FormSubmissionSerializer
from .models import FormSubmission
from django.shortcuts import redirect, render



@api_view(['POST'])
def register(request):
    serializer = FormSubmissionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        print(serializer.data)
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['GET'])
def lists(request):
    submissions = FormSubmission.objects.all()
    serializer = FormSubmissionSerializer(submissions, many=True)
    return Response(serializer.data)


def Register(request):
     if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        destination = request.POST.get('destination')
        travelers = request.POST.get('travelers')
        budget = request.POST.get('budget')

        # Create and save the form submission object
        submission = FormSubmission(
            name=name,
            email=email,
            destination=destination,
            travelers=travelers,
            budget=budget
        )
        submission.save()
        return redirect('lists')
     else:
         return render(request, "Register.html")

def Lists(request):
    
    submissions = FormSubmission.objects.all()
    return render(request, 'lists.html')
