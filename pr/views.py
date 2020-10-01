from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Review, Company
from pr.forms import ReviewForm
import datetime
from django.views.generic import ListView
from django.db.models import Q
from django.contrib.auth.decorators import login_required



def review_list(request):
    latest_review_list = Review.objects.order_by('-pub_date')[:9]
    context = {'latest_review_list':latest_review_list}
    return render(request, 'pr/review_list.html', context)


def review_detail(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    return render(request, 'pr/review_detail.html', {'review': review})


def company_list(request):
    company_list = Company.objects.order_by('-name')
    context = {'company_list':company_list}
    return render(request, 'pr/company_list.html', context)


def company_detail(request, company_id):
    company = get_object_or_404(Company, pk=company_id)
    form = ReviewForm()
    return render(request, 'pr/company_detail.html', {'company': company, 'form': form})



class SearchResultsView(ListView):
    model = Company
    template_name = 'pr/search_results.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = Company.objects.filter(
            Q(name__icontains=query) 
        )
        return object_list
@login_required
def add_review(request, company_id):
    company = get_object_or_404(Company, pk=company_id)
    form = ReviewForm(request.POST)
    if form.is_valid():
        rating = form.cleaned_data['rating']
        comment = form.cleaned_data['comment']
        user_name = form.cleaned_data['user_name']
        review = Review()
        review.company = company
        review.user_name = user_name
        review.rating = rating
        review.comment = comment
        review.pub_date = datetime.datetime.now()
        review.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('pr:company_detail', args=(company.id,)))

    return render(request, 'pr/company_detail.html', {'company': company, 'form': form})


def user_review_list(request, username=None):
    if not username:
        username = request.user.username
    latest_review_list = Review.objects.filter(user_name=username).order_by('-pub_date')
    context = {'latest_review_list':latest_review_list, 'username':username}
    return render(request, 'pr/user_review_list.html', context)