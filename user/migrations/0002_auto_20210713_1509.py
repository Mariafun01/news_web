# Generated by Django 3.2.4 on 2021-07-13 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='new',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='new',
            name='comments_list',
        ),
        migrations.RemoveField(
            model_name='new',
            name='fname',
        ),
        migrations.RemoveField(
            model_name='users',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='users',
            name='comments_list',
        ),
        migrations.AddField(
            model_name='comments',
            name='createUser',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='user.users', verbose_name='评论者'),
        ),
        migrations.AddField(
            model_name='comments',
            name='new',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='user.new', verbose_name='所在新闻'),
        ),
        migrations.AddField(
            model_name='fname',
            name='new',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='user.new', verbose_name='所属新闻'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='title',
            field=models.CharField(max_length=100, null=True, verbose_name='标题'),
        ),
        migrations.RemoveField(
            model_name='new',
            name='label',
        ),
        migrations.AddField(
            model_name='new',
            name='label',
            field=models.ManyToManyField(db_table='tbNewsLabels', related_name='new_label', to='user.Lable', verbose_name='新闻标签表'),
        ),
    ]
