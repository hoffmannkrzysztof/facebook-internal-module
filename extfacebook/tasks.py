import datetime
from celery.task import task, periodic_task
from dateutil.relativedelta import relativedelta
from facepy import GraphAPI, FacepyError
from models import ExtendedUser, FacebookPost


@task()
def post_link(user, link, message=None):
    graph = GraphAPI(user.access_token)

    post = None
    error = None
    id = None

    try:
        post = graph.post(
            path='/me/feed',
            link=link,
            message=message
        )

    except FacepyError, error:

        error_list = ['application to perform this action', 'has not authorized application', 'validating access token', 'not be decrypted']

        for msg in error_list:
            if msg in error.message:
                user.is_active = False
                user.save()
                break

    if post:
        id = post['id']

    if id:

        FacebookPost.objects.create(
            user=user,
            post_id = id,
            delete_after = datetime.datetime.now()+relativedelta(hours=+3)
        )

    return id, error


@task()
def post_link_to_users(object, limit, website, rand=True, message=None):
    users = ExtendedUser.objects.filter(access_token__isnull=False, app_id=website.app_id, is_active=True)

    if rand:
        users = users.order_by("?")
    else:
        users = users.order_by("-id")

    users = users[:limit]
    for user in users:
        link = "http://" + website.domain + object.get_absolute_url()
        post_link.delay(user=user,
                       link=link,
                       message=message,
        )

@task()
def delete_post(post):
    user = post.user
    graph = GraphAPI(user.access_token)

    try:
        graph.delete( post.post_id )
        post.is_deleted = True
    except FacepyError,e:
        post.error_delete = e

    post.is_finished = True
    post.save()

@periodic_task(run_every=datetime.timedelta(minutes=5))
def delete_expired_posts():
    for post in FacebookPost.objects.filter(
        delete_after__lt=datetime.datetime.now(),
        is_finished = False
    ):
        delete_post.delay(post)