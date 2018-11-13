from .views import BlogPostViewSet

routeList = (
    (r'blog_post', BlogPostViewSet, 'blog_post'),
)
