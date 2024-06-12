from django.shortcuts import render
from django.http import JsonResponse
from .models import Category, Language, Feedback
from bson import json_util
import json

# Helper function to format data into JSON format
def get_formatted_data(data):
    formatted_data = []
    for row in data:
          formatted_data.append(row)
    json_data = json.dumps(formatted_data, default=json_util.default)
    return json_data

# View for the 'index' page
def index(request):
     # Retrieve category and language data from the database
     category_data = Category.objects.filter(is_deleted=0)
     language_data = Language.objects.filter(is_deleted=0)

     # Format the language and category data as JSON
     formatted_category_data = get_formatted_data(category_data.values())
     formatted_language_data = get_formatted_data(language_data.values())

     # Render the 'index.html' template with the formatted data
     return render(request, 'index.html', {'category_data': formatted_category_data, 'language_data': formatted_language_data})

# View for the 'content' page
def content(request, lng_id):
     # Retrieve language data from the database
     language_data = Language.objects.filter(is_deleted=0, id=lng_id).all()
     
     # Retrieve page title for each page
     for i in language_data.values():
          page_title = i['name']

     # Format the language data as JSON
     formatted_language_data = get_formatted_data(language_data.values())

     # Render the 'content.html' template with the formatted data
     context = {
        'page_title': page_title,
        'language_data': formatted_language_data,
    }
     
     return render(request, 'content.html', context)

def feedback_form(request):
     return render(request, 'feedback_form.html')

def insert_data(request):
    if request.method == 'POST':
        try:
            name = request.POST['name']
            email = request.POST['email']
            feedback = request.POST['feedback']

            data = Feedback(name=name, email_id=email, feedback=feedback)
            data.save()

            return render(request, 'feedback_form.html')
        except Exception as e:
            # Handle exceptions, log or return an error response if needed
            return JsonResponse({'error': str(e)}, status=500)

    # Return a default response if the request method is not POST
    return JsonResponse({'error': 'Invalid request method'}, status=400)
