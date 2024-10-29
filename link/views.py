from django.shortcuts import render
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
    qs = links_model.objects.all()
    no_items = qs.count()
    discount_list = []  # Initialize discount list

    # Check for discounts
    for item in qs:
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
