from .views import BlogPostViewSet

routeList = (
    (r'blog_posts', BlogPostViewSet, 'blog_posts'),
)
