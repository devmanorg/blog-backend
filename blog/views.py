from django.shortcuts import render
from blog.models import Comment, Post

from django.db.models import Count

import folium


def serialize_post(post):
    return {
        "title": post.title,
        "text": post.text,
        "author": post.author.username,
        "comments_amount": Comment.objects.filter(post=post).count(),
        "image_url": post.image.url if post.image else None,
        "published_at": post.published_at,
        "slug": post.slug,
    }


def index(request):
    all_posts = Post.objects.prefetch_related('author')
    popular_posts = all_posts.annotate(likes_count=Count('likes')).order_by('-likes_count')[:3]
    fresh_posts = all_posts.order_by('-published_at')[:5]

    context = {
        'most_popular_posts': [serialize_post(post) for post in popular_posts],
        'fresh_posts': [serialize_post(post) for post in fresh_posts],
    }
    return render(request, 'index.html', context)


def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    comments = Comment.objects.filter(post=post)
    serialized_comments = []
    for comment in comments:
        serialized_comments.append({
            'text': comment.text,
            'published_at': comment.published_at,
            'author': comment.author.username,
        })

    serialized_post = {
        "title": post.title,
        "text": post.text,
        "author": post.author.username,
        "comments": serialized_comments,
        'likes_amount': post.likes.count(),
        "image_url": post.image.url if post.image else None,
        "published_at": post.published_at,
        "slug": post.slug,
    }

    context = {
        'post': serialized_post,
    }
    return render(request, 'blog-details.html', context)


def contacts(request):
    # позже здесь будет код для статистики заходов на эту страницу
    # и для записи фидбека
    coordinates = [55.751244, 37.618423]
    folium_map = folium.Map(location=coordinates, zoom_start=12)
    folium.Marker(
        coordinates,
        tooltip="Мы здесь",
    ).add_to(folium_map)
    html_map = folium_map._repr_html_()
    return render(request, 'contacts.html', {"html_map": html_map})
