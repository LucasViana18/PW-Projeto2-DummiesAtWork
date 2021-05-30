from django.shortcuts import render

# Create your views here.
def home_page_view(request):
	return render(request, 'website/index.html')

def portfolio_page_view(request):
	return render(request, 'website/portfolio.html')

def services_page_view(request):
	return render(request, 'website/services.html')

def aboutus_page_view(request):
	return render(request, 'website/aboutus.html')

def contact_page_view(request):
	return render(request, 'website/contact.html')