from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.db.models import Q
from itertools import chain
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.db.models import CharField, Value
from .forms import (TicketForm, 
				   DeletePostForm, 
				   ReviewForm, 
				   AutoReviewForm)
from .models import (Ticket, 
					UserFollows, 
					Review, 
					AutoReview)


@login_required
def get_posts(request):
	"""	Get all posts user and users followed """

	users_followed = []
	for user in UserFollows.objects.filter(user=request.user):
		users_followed.append(user.followed_user)
	tickets = Ticket.objects.filter(Q(user=request.user) | Q(user__in=users_followed))
	reviews = Review.objects.filter(Q(user=request.user) | Q(ticket__user=request.user)	| Q(user__in=users_followed))
	auto_reviews = AutoReview.objects.filter(Q(user=request.user) | Q(user__in=users_followed))
	tickets = tickets.annotate(content_type=Value("TICKET", CharField()))
	reviews = reviews.annotate(content_type=Value("REVIEW", CharField()))
	auto_reviews = auto_reviews.annotate(content_type=Value("AUTOREVIEW", CharField()))
	all_posts = sorted(chain(reviews, tickets, auto_reviews),key=lambda post: post.time_created,reverse=True)
	return all_posts


@login_required
def flux_page(request):
	"""	Get all posts from get_posts() and goes in flux page """

	posts = get_posts(request)
	return render(request, "review_ticketing/flux.html", context={"posts": posts})


@login_required
def posts_page(request):
	"""	Get all posts from get_posts() and goes in posts page """

	posts = get_posts(request)
	return render(request, "review_ticketing/posts.html", context={"posts": posts})


@login_required
def ticket_creation(request):
	"""	Create ticket and goes in flux page if ok """

	ticket_form = TicketForm()
	if request.method == "POST":
		ticket_form = TicketForm(request.POST, request.FILES)
		if ticket_form.is_valid():
			ticket = ticket_form.save(commit=False)
			ticket.user = request.user
			ticket.save()
			return redirect("flux")
	context = {"ticket_form": ticket_form}
	return render(request, "review_ticketing/create_ticket_post.html", context=context)


@login_required
def review_creation(request, ticket_id):
	"""	Get ticket id and create review for this ticket	"""

	review_form = ReviewForm()
	ticket = Ticket.objects.get(id=ticket_id)
	if request.method == "POST":
		review_form = ReviewForm(request.POST, request.FILES)
		if review_form.is_valid():
			review = review_form.save(commit=False)
			review.ticket = ticket
			ticket.review_existing = True
			ticket.save()
			review.user = request.user
			review.save()
			return redirect("flux")
	context = {	"review_form": review_form,
				"ticket": ticket}
	return render(request, "review_ticketing/create_review_post.html", context=context)


@login_required
def auto_review_creation(request):
	"""	Create autoreview (ticket + review)	"""

	auto_review_form = AutoReviewForm()
	if request.method == "POST":
		auto_review_form = AutoReviewForm(request.POST, request.FILES)
		if auto_review_form.is_valid():
			auto_review = auto_review_form.save(commit=False)
			ticket = Ticket.objects.create(title=auto_review.title,
										   description=auto_review.description,
										   user=request.user,
										   image=auto_review.image,
										   time_created=auto_review.time_created,
										   review_existing=True)
			auto_review.ticket = ticket
			auto_review.user = request.user
			auto_review.save()

			return redirect("flux")
	context = {"auto_review_form": auto_review_form}
	return render(request,"review_ticketing/create_auto_review_post.html",context=context)


@login_required
def subscription_page(request):
	"""	Get users_followed and users_followers, and checks if input = user existing	"""

	users_followed = UserFollows.objects.filter(user=request.user)
	users_followers = UserFollows.objects.filter(followed_user=request.user)
	if request.method == "POST":
		follow = request.POST["name"]  # get input name's user from html page.
		username = request.user
		try:
			to_follow = User.objects.get(username=follow)
			if to_follow != username:
				if (UserFollows.objects.get_or_create(user=request.user, followed_user=to_follow)
					is False):
					UserFollows.objects.create(user=request.user, followed_user=to_follow)
				else:
					messages.add_message(request,messages.INFO,f"Vous êtes abonné à {to_follow}.")
			else:
				messages.add_message(request, messages.INFO, f"Vous êtes {request.user} !")
		except ObjectDoesNotExist:
			messages.add_message(request, messages.INFO, "Cet utilisateur n'existe pas.")

	return render(request, "review_ticketing/subscription.html", context={"users_followed": users_followed,
																		  "users_followers": users_followers})


@login_required
def unfollow(request, user_follows_id):
	"""	Get user followed id delete subscription and redirect to 'subscription'	"""

	if request.method == "GET":
		subscription = UserFollows.objects.filter(pk=user_follows_id)
		subscription.delete()
	return redirect("subscription")


@login_required
def edit_ticket(request, obj_id):
	"""	Get post's id edit post if is a ticket """

	obj = Ticket.objects.get(id=obj_id)
	form = TicketForm
	html = "review_ticketing/edit_ticket.html"
	edit_form = form(instance=obj)
	if request.method == "POST":
		edit_form = form(request.POST or None, request.FILES or None, instance=obj)
		if edit_form.is_valid():
			edit_form.save()
			return redirect("posts")
	context = {"edit_form": edit_form, "post": obj}
	return render(request, html, context=context)


@login_required
def edit_review(request, obj_id):
	"""	Get post's id edit post if is a review """

	obj = Review.objects.get(id=obj_id)
	form = ReviewForm
	html = "review_ticketing/edit_review.html"
	edit_form = form(instance=obj)
	if request.method == "POST":
		edit_form = form(request.POST or None, request.FILES or None, instance=obj)
		if edit_form.is_valid():
			edit_form.save()
			return redirect("posts")
	context = {"edit_form": edit_form, "post": obj}
	return render(request, html, context=context)


@login_required
def edit_autoreview(request, obj_id):
	"""	Get post's id edit post if is an autoreview """

	obj = AutoReview.objects.get(id=obj_id)
	form = ReviewForm
	html = "review_ticketing/edit_review.html"
	edit_form = form(instance=obj)
	if request.method == "POST":
		edit_form = form(request.POST or None, request.FILES or None, instance=obj)
		if edit_form.is_valid():
			edit_form.save()
			return redirect("posts")
	context = {"edit_form": edit_form, "post": obj}
	return render(request, html, context=context)


@login_required
def delete_ticket(request, obj_id):
	"""	Get post's id delete post if is a ticket """

	obj = Ticket.objects.get(id=obj_id)
	delete_form = DeletePostForm()
	html = "review_ticketing/delete_post.html"
	if request.method == "POST":
		delete_form = DeletePostForm(request.POST)
		if delete_form.is_valid():
			obj.delete()
			return redirect("posts")
	context = {"delete_form": delete_form,}
	return render(request, html, context=context)

@login_required
def delete_review(request, obj_id):
	"""	Get post's id delete post if is a review """

	obj = Review.objects.get(id=obj_id)
	delete_form = DeletePostForm()
	html = "review_ticketing/delete_post.html"
	if request.method == "POST":
		delete_form = DeletePostForm(request.POST)
		if delete_form.is_valid():
			if isinstance(obj, Review):
				#ticket = Ticket.objects.get(id=ticket_id)
				#ticket.review_existing = True
				#ticket.save()
				obj.ticket.review_existing = False
				obj.ticket.save()
			obj.delete()
			return redirect("posts")
	context = {"delete_form": delete_form,}
	return render(request, html, context=context)


@login_required
def delete_autoreview(request, obj_id):
	"""	Get post's id delete post if is an autoreview """

	obj = AutoReview.objects.get(id=obj_id)
	delete_form = DeletePostForm()
	html = "review_ticketing/delete_post.html"
	if request.method == "POST":
		delete_form = DeletePostForm(request.POST)
		if delete_form.is_valid():
			if isinstance(obj, Review):
				obj.ticket.review_existing = False
				obj.ticket.save()
			obj.delete()
			return redirect("posts")
	context = {"delete_form": delete_form,}
	return render(request, html, context=context)