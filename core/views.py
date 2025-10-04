from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm
from difflib import SequenceMatcher

def similarity(a, b):
    return SequenceMatcher(None, a, b).ratio()


def index(request):
    recent = Item.objects.order_by('-created_at')[:8]
    return render(request, 'core/index.html', {'recent': recent})


def report_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            if request.user.is_authenticated:
                item.created_by = request.user
            item.save()
            counterpart_status = 'found' if item.status == 'lost' else 'lost'
            candidates = Item.objects.filter(status=counterpart_status, claimed=False)
            matches = []
            for c in candidates:
                score_title = similarity(item.title.lower(), c.title.lower())
                score_desc = similarity(item.description.lower(), c.description.lower()) if item.description and c.description else 0
                score_loc = similarity(item.location.lower(), c.location.lower()) if item.location and c.location else 0
                total = (score_title * 0.6) + (score_desc * 0.3) + (score_loc * 0.1)
                if total > 0.55:
                    matches.append((c, total))
            if matches:
                for m, score in matches[:5]:
                    print(f"Possible match: {m} (score {score:.2f})")
            return redirect('core:item_list')
    else:
        form = ItemForm()
    return render(request, 'core/report_form.html', {'form': form})


def item_list(request):
    q = request.GET.get('q')
    items = Item.objects.all().order_by('-created_at')
    if q:
        items = items.filter(title__icontains=q) | items.filter(description__icontains=q)
    return render(request, 'core/list.html', {'items': items})


def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'core/detail.html', {'item': item})
