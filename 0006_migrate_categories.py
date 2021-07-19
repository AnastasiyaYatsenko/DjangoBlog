# Generated by Django 3.2.5 on 2021-07-19 14:48

from django.db import migrations


def migrate_categories(apps, schema_editor):
    Post = apps.get_model('posts', 'Post')
    PostCategories = apps.get_model('posts', 'PostCategories')
    for p in Post.objects.all():
        if p.category_id:
            c = PostCategories(post_id=p.id,
                         category_id=p.category_id,
                         is_main=True)
            c.save()
            p.category = None
        p.save()


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20210719_1448'),
    ]

    operations = [
        migrations.RunPython(migrate_categories,
                             reverse_code=migrations.RunPython.noop),
    ]

