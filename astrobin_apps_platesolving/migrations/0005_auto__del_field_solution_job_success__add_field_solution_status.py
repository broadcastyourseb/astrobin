# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Solution.job_success'
        db.delete_column('astrobin_apps_platesolving_solution', 'job_success')

        # Adding field 'Solution.status'
        db.add_column('astrobin_apps_platesolving_solution', 'status', self.gf('django.db.models.fields.PositiveIntegerField')(default=0), keep_default=False)


    def backwards(self, orm):
        
        # Adding field 'Solution.job_success'
        db.add_column('astrobin_apps_platesolving_solution', 'job_success', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Deleting field 'Solution.status'
        db.delete_column('astrobin_apps_platesolving_solution', 'status')


    models = {
        'astrobin_apps_platesolving.solution': {
            'Meta': {'object_name': 'Solution'},
            'dec_center_dms': ('django.db.models.fields.CharField', [], {'max_length': '13', 'null': 'True', 'blank': 'True'}),
            'fieldh': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '14', 'decimal_places': '10', 'blank': 'True'}),
            'fieldunits': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'fieldw': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '14', 'decimal_places': '10', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_file': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'objects_in_field': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'orientation': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '14', 'decimal_places': '10', 'blank': 'True'}),
            'pixscale': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '14', 'decimal_places': '10', 'blank': 'True'}),
            'ra_center_hms': ('django.db.models.fields.CharField', [], {'max_length': '12', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'submission_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['astrobin_apps_platesolving']
