from web_blog.models import Category,Tags

def get_all_categories(request):
    categories = Category.objects.all()
    tags = Tags.objects.all()
    context = {
        "categories":categories,
        "tag":tags
    }
    return context