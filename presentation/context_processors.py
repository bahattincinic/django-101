from .models import Category


def export_categories(request):
    return {
        'categories': Category.objects.all()
    }
