from .models import Category, Company

def header(request):
    path = request.path.split('/')[1]
    active  = ''
    if path=='':
        active = 'home'
    elif path=='company':
        active = 'company'
    elif path=='machine':
        active = 'machine'
    elif path=="contact":
        active = "contact"
    return {
        "companies": Company.objects.all(),
        "categories": Category.objects.all(),
        "active": active
    }
