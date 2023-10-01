from django.shortcuts import render
from django.http import JsonResponse
import joblib
from .forms import PredictionForm

# Load the model
model = joblib.load('model_filename.pkl')

def predict_view(request):
    if request.method == 'POST':
        form = PredictionForm(request.POST, request.FILES)  # Include request.FILES to handle file uploads

        if form.is_valid():
            input_data = form.cleaned_data['input_data']
            uploaded_image = form.cleaned_data['image_upload']  # Get the uploaded file

            # Perform predictions using the loaded model and uploaded image
            prediction = model.predict([input_data])

            # Handle the uploaded image as needed, e.g., save it
            # uploaded_image.save('path_to_save_uploaded_image.jpg')

            # Return the prediction as JSON
            return JsonResponse({'prediction': prediction[0]})

    else:
        form = PredictionForm()

    # Render the HTML template with the form for user input
    return render(request, 'predict.html', {'form': form})
