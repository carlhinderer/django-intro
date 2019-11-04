from django.shortcuts import render

def contact(request):
    # Content from the request or database is extracted here
    #   and passed to the template for display.
    return render(request, 'about/contact.html')