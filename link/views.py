from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from .forms import link_forms
from .models import links_model

# Create your views here.

# List we need to pass to our template:
# - Query set of items
# - Number of items we need to track
# - Number of items that are discounted
# - Form to save the objects, and error message if any

def home_view(request):
    no_discount = 0
    error = None
    form = link_forms(request.POST or None)

    if request.method == "POST":
        try:
            if form.is_valid():
                form.save()
        except AttributeError:
            error = 'Could not find the price'
        except Exception as e:
            error = 'Something went wrong'

    # Query set: grab all items from links_model
    qs = links_model.get_all()
    no_items = qs.count()
    discount_list = []  # Initialize discount list

    # Check for discounts
    for item in qs:
        if item.old_price !=None and item.current_price !=None:
            
            if item.old_price > item.current_price:
                discount_list.append(item)
    no_discount = len(discount_list)  # Count of items with discounts

    context = {
        'qs': qs,
        'no_items': no_items,
        'no_discount': no_discount,
        'form': form,
        'error': error
    }

    return render(request, "links/main.html", context)
def link_delete_view(request, pk):
    # Retrieve the link object or return a 404 if not found
    print("we are here...............")
    link = get_object_or_404(links_model, pk=pk)
    
    if request.method == 'POST':
        # Delete the link and redirect to the link list page
        link.delete()
        return redirect(reverse_lazy('home'))

    # If a GET request is made, redirect back to the link list
    return redirect(reverse_lazy('home'))