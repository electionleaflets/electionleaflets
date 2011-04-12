# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Leaflet.imprint'
        db.add_column(u'leaflet', 'imprint', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Leaflet.imprint'
        db.delete_column(u'leaflet', 'imprint')


    models = {
        'categories.category': {
            'Meta': {'object_name': 'Category', 'db_table': "u'category'"},
            'default_value': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '765'}),
            'slug': ('django.db.models.fields.SlugField', [], {'db_index': 'True', 'max_length': '255', 'blank': 'True'})
        },
        'constituencies.constituency': {
            'Meta': {'object_name': 'Constituency', 'db_table': "u'constituency'"},
            'alternative_name': ('django.db.models.fields.CharField', [], {'max_length': '765', 'blank': 'True'}),
            'area_code': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'}),
            'area_uri': ('django.db.models.fields.CharField', [], {'max_length': '765', 'blank': 'True'}),
            'constituency_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['constituencies.ConstituencyType']"}),
            'count': ('django.db.models.fields.IntegerField', [], {}),
            'guardian_aristotle_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'guardian_pa_code': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '765'}),
            'retired': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'db_index': 'True', 'max_length': '255', 'blank': 'True'}),
            'url_id': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'wikipedia_url': ('django.db.models.fields.CharField', [], {'max_length': '765', 'blank': 'True'})
        },
        'constituencies.constituencytype': {
            'Meta': {'object_name': 'ConstituencyType', 'db_table': "u'constituency_type'"},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Country']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'url_id': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'})
        },
        'core.country': {
            'Meta': {'object_name': 'Country', 'db_table': "u'country'"},
            'country_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'iso': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'iso3': ('django.db.models.fields.CharField', [], {'max_length': '9', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '240'})
        },
        'leaflets.leaflet': {
            'Meta': {'object_name': 'Leaflet', 'db_table': "u'leaflet'"},
            'attacks': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'attacks'", 'symmetrical': 'False', 'through': "orm['leaflets.LeafletPartyAttack']", 'to': "orm['parties.Party']"}),
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['categories.Category']", 'through': "orm['leaflets.LeafletCategory']", 'symmetrical': 'False'}),
            'constituencies': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['constituencies.Constituency']", 'through': "orm['leaflets.LeafletConstituency']", 'symmetrical': 'False'}),
            'date_delivered': ('django.db.models.fields.DateTimeField', [], {}),
            'date_uploaded': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imprint': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'lat': ('django.db.models.fields.FloatField', [], {}),
            'live': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'lng': ('django.db.models.fields.FloatField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'postcode': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'publisher_party': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['parties.Party']"}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['tags.Tag']", 'through': "orm['leaflets.LeafletTag']", 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '765'})
        },
        'leaflets.leafletcategory': {
            'Meta': {'object_name': 'LeafletCategory', 'db_table': "u'leaflet_category'"},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['categories.Category']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'leaflet': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['leaflets.Leaflet']"})
        },
        'leaflets.leafletconstituency': {
            'Meta': {'object_name': 'LeafletConstituency', 'db_table': "'leaflet_constituency'"},
            'constituency': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['constituencies.Constituency']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'leaflet': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['leaflets.Leaflet']"})
        },
        'leaflets.leafletimage': {
            'Meta': {'object_name': 'LeafletImage', 'db_table': "u'leaflet_image'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_key': ('django.db.models.fields.CharField', [], {'max_length': '765'}),
            'leaflet': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'images'", 'to': "orm['leaflets.Leaflet']"}),
            'sequence': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        'leaflets.leafletpartyattack': {
            'Meta': {'object_name': 'LeafletPartyAttack', 'db_table': "u'leaflet_party_attack'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'leaflet': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['leaflets.Leaflet']"}),
            'party': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['parties.Party']"})
        },
        'leaflets.leaflettag': {
            'Meta': {'object_name': 'LeafletTag', 'db_table': "u'leaflet_tag'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'leaflet': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['leaflets.Leaflet']"}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tags.Tag']"})
        },
        'leaflets.promise': {
            'Meta': {'object_name': 'Promise', 'db_table': "u'promise'"},
            'detail': ('django.db.models.fields.TextField', [], {}),
            'leaflet_id': ('django.db.models.fields.IntegerField', [], {}),
            'promise_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'})
        },
        'leaflets.rateinteresting': {
            'Meta': {'object_name': 'RateInteresting', 'db_table': "u'rate_interesting'"},
            'description': ('django.db.models.fields.TextField', [], {}),
            'leaflet_id': ('django.db.models.fields.IntegerField', [], {}),
            'rate_interesting_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'user_email': ('django.db.models.fields.CharField', [], {'max_length': '765'}),
            'user_name': ('django.db.models.fields.CharField', [], {'max_length': '765'})
        },
        'leaflets.rateinterestingseq': {
            'Meta': {'object_name': 'RateInterestingSeq', 'db_table': "u'rate_interesting_seq'"},
            'sequence': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'})
        },
        'leaflets.ratetype': {
            'Meta': {'object_name': 'RateType', 'db_table': "u'rate_type'"},
            'left_label': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'rate_type_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'right_label': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'})
        },
        'leaflets.ratevalue': {
            'Meta': {'object_name': 'RateValue', 'db_table': "u'rate_value'"},
            'leaflet_id': ('django.db.models.fields.IntegerField', [], {}),
            'rate_type_id': ('django.db.models.fields.IntegerField', [], {}),
            'rate_value_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'user_email': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'user_name': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'value': ('django.db.models.fields.IntegerField', [], {})
        },
        'leaflets.ratevalueseq': {
            'Meta': {'object_name': 'RateValueSeq', 'db_table': "u'rate_value_seq'"},
            'sequence': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'})
        },
        'leaflets.uploadsession': {
            'Meta': {'object_name': 'UploadSession'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image1': ('django.db.models.fields.files.ImageField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'image2': ('django.db.models.fields.files.ImageField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'image3': ('django.db.models.fields.files.ImageField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'image4': ('django.db.models.fields.files.ImageField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'image5': ('django.db.models.fields.files.ImageField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'image6': ('django.db.models.fields.files.ImageField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'image7': ('django.db.models.fields.files.ImageField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'image8': ('django.db.models.fields.files.ImageField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            's3keys': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'parties.party': {
            'Meta': {'object_name': 'Party', 'db_table': "u'party'"},
            'colour': ('django.db.models.fields.CharField', [], {'max_length': '18', 'blank': 'True'}),
            'count': ('django.db.models.fields.IntegerField', [], {}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Country']"}),
            'force_top': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo_file': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'major': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '765'}),
            'popular': ('django.db.models.fields.IntegerField', [], {}),
            'show_on_add_page': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'db_index': 'True', 'max_length': '255', 'blank': 'True'}),
            'twitter_account': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'url_id': ('django.db.models.fields.CharField', [], {'max_length': '765', 'blank': 'True'})
        },
        'tags.tag': {
            'Meta': {'object_name': 'Tag', 'db_table': "u'tag'"},
            'dead': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'db_index': 'True', 'max_length': '255', 'blank': 'True'}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '765'}),
            'tag_clean': ('django.db.models.fields.CharField', [], {'max_length': '765', 'blank': 'True'})
        }
    }

    complete_apps = ['leaflets']
