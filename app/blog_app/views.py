from django.shortcuts import render


def main_page(request):
    
    name = 'Max'
    name_2 = 'Artem'
    context = {
        'name': name,
        'name_2': name_2
    }
    
    return render(request, 'blog_app/blog_app_index.html', context=context)
