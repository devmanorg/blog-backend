from django.db import migrations

from django.utils.text import slugify



def calculate_slug_if_null(apps, schema_editor):
    Post = apps.get_model('blog', 'Post')
    for post in Post.objects.filter(slug=""):
        post.slug = slugify(post.title)
        post.save()


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_slug'),
    ]

    operations = [
        migrations.RunPython(calculate_slug_if_null),
    ]
