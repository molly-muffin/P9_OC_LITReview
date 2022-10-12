from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import (flux_page as flux,
                    posts_page as posts,
                    subscription_page as subscription,
                    ticket_creation,
                    edit_ticket,
                    edit_review,
                    edit_autoreview,
                    delete_ticket,
                    delete_review,
                    delete_autoreview,
                    unfollow,
                    review_creation,
                    auto_review_creation)

urlpatterns = [path("flux/", flux, name="flux"),
               path("posts/", posts, name="posts"),
               path("subscription/", subscription, name="subscription"),
               path("ticket/create", ticket_creation, name="ticket_create"),
               path("review/create/<int:ticket_id>/", review_creation, name="review_create"),
               path("review/auto_create/", auto_review_creation, name="auto_review_create"),
               path("ticket/<int:obj_id>/edit", edit_ticket, name="edit_ticket"),
               path("review/<int:obj_id>/edit", edit_review, name="edit_review"),
               path("auto_review/<int:obj_id>/edit", edit_autoreview, name="edit_autoreview"),
               path("ticket/<int:obj_id>/delete", delete_ticket, name="delete_ticket"),
               path("review/<int:obj_id>/delete", delete_review, name="delete_review"),
               path("auto_review/<int:obj_id>/delete", delete_autoreview, name="delete_autoreview"),
               path("follow-users/", subscription, name="follow_users"),
               path("unfollow/<user_follows_id>", unfollow, name="unfollow")]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
