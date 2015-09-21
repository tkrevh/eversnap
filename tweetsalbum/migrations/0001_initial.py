# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Album'
        db.create_table('tweetsalbum_album', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('max_id', self.gf('django.db.models.fields.BigIntegerField')(default=0)),
        ))
        db.send_create_signal('tweetsalbum', ['Album'])

        # Adding model 'TUser'
        db.create_table('tweetsalbum_tuser', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('screen_name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=64)),
        ))
        db.send_create_signal('tweetsalbum', ['TUser'])

        # Adding model 'Picture'
        db.create_table('tweetsalbum_picture', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('album', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tweetsalbum.Album'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tweetsalbum.TUser'])),
            ('likes', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=2000)),
        ))
        db.send_create_signal('tweetsalbum', ['Picture'])


    def backwards(self, orm):
        # Deleting model 'Album'
        db.delete_table('tweetsalbum_album')

        # Deleting model 'TUser'
        db.delete_table('tweetsalbum_tuser')

        # Deleting model 'Picture'
        db.delete_table('tweetsalbum_picture')


    models = {
        'tweetsalbum.album': {
            'Meta': {'object_name': 'Album'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_id': ('django.db.models.fields.BigIntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        'tweetsalbum.picture': {
            'Meta': {'object_name': 'Picture'},
            'album': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tweetsalbum.Album']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'likes': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tweetsalbum.TUser']"})
        },
        'tweetsalbum.tuser': {
            'Meta': {'object_name': 'TUser'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'screen_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'})
        }
    }

    complete_apps = ['tweetsalbum']