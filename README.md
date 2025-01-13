# Django Application for Printing Prime Numbers

This project is a beginner-friendly Django web application that allows users to input a number and check whether it is a prime number or not. It also demonstrates fundamental Django concepts such as creating views, forms, and templates.

## Features

1. **Input Form**: Users can enter a number using a simple Django form.
2. **Prime Check**: The application checks if the entered number is a prime number.
3. **Result Display**: The result is displayed dynamically on the web page.
4. **Learning Oriented**: Built with simplicity to help beginners understand Django basics.

## Requirements

- Python 3.11 or higher
- Django 4.2 or higher

## Installation Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/django-prime-number.git
   ```

2. Navigate to the project directory:
   ```bash
   cd django-prime-number
   ```

3. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

5. Run the development server:
   ```bash
   python manage.py runserver
   ```

6. Open your browser and navigate to:
   ```
   http://127.0.0.1:8000
   ```

## How It Works

1. **Form Input**:
   - A Django form collects user input.

2. **Backend Logic**:
   - The view processes the input and checks if the number is prime using Python logic.

3. **Template Rendering**:
   - The result is displayed on the template dynamically.

## Code Overview

### Views
```python
from django.shortcuts import render

def check_prime(request):
    result = None
    if request.method == 'POST':
        number = int(request.POST.get('number'))
        if number > 1:
            for i in range(2, int(number ** 0.5) + 1):
                if number % i == 0:
                    result = f"{number} is not a prime number."
                    break
            else:
                result = f"{number} is a prime number."
        else:
            result = f"{number} is not a prime number."
    return render(request, 'prime_check.html', {'result': result})
```

### Template
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Prime Number Checker</title>
</head>
<body>
    <h1>Prime Number Checker</h1>
    <form method="post">
        {% csrf_token %}
        <label for="number">Enter a number:</label>
        <input type="number" id="number" name="number" required>
        <button type="submit">Check</button>
    </form>
    {% if result %}
        <p>{{ result }}</p>
    {% endif %}
</body>
</html>
```

## Git Commit Description

- **Initial Commit**: Added project structure with basic configurations.
- **Form Implementation**: Created a Django form for user input.
- **Prime Logic**: Added logic to check for prime numbers in the views.
- **Template Setup**: Designed a simple HTML template to display results.

## GitHub Repository

1. **Create a GitHub Repository**: 
   - Go to GitHub and create a new repository named `django-prime-number`.

2. **Add Remote Origin**:
   ```bash
   git remote add origin https://github.com/yourusername/django-prime-number.git
   ```

3. **Push to GitHub**:
   ```bash
   git add .
   git commit -m "Initial Commit"
   git push -u origin main
   ```

---
This project serves as a foundation for learning Django and building interactive web applications. Feel free to clone, experiment, and enhance it!

