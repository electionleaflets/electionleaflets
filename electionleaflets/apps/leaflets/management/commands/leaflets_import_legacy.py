# -*- coding: utf-8 -*-
import os

from django.core.management.base import BaseCommand
from django.conf import settings
from django.core.files import File

from legacy.models import legacyLeaflet, legacyParty

from leaflets.models import Leaflet, LeafletImage
from constituencies.models import Constituency
from uk_political_parties.models import Party

class Command(BaseCommand):

    def clean_legacy_leaflet(self, legacy_leaflet, party=None, constituency=None):
        data = legacy_leaflet.__dict__.copy()
        del data['publisher_party_id']
        del data['_publisher_party_cache']
        del data['_state']
        data['publisher_party'] = party
        data['constituency'] = constituency
        if data.get('live'):
            data['status'] = 'live'
        else:
            data['status'] = 'removed'
        del data['live']
        return data

    def clean_legacy_leaflet_image(self, legacy_image):
        data = {}
        key = "%s.jpg" % legacy_image.image_key
        if getattr(settings, 'IMAGE_LOCAL_CACHE'):
            image_path = os.path.join(
                settings.IMAGE_LOCAL_CACHE,
                key
            )

            if os.path.exists(image_path):
                print "Exists"
                f = open(image_path, 'r')
                data['image'] = File(f)
            else:
                image_path = os.path.join(
                    settings.IMAGE_LOCAL_CACHE,
                    'large',
                    key
                )
                if os.path.exists(image_path):
                    print "Exists"
                    f = open(image_path, 'r')
                    data['image'] = File(f)
                else:
                    print "Doesn't exist"
            return data

    def clean_constituency(self, con):
        con_name = con.constituency.name
        if con_name == "Ynys Mon":
            con_name = "Ynys Môn"
        if con_name == "Cotswold":
            con_name = "The Cotswolds"
        if con_name == "Taunton":
            con_name = "Taunton Deane"
        try:
            con = Constituency.objects.get(name__iexact=con_name)
        except Constituency.DoesNotExist:
            con_name = ", ".join(con_name.split(' ', 1))
            con = Constituency.objects.get(name=con_name)
        return con


    def handle(self, **options):
        for legacy_leaflet in legacyLeaflet.objects.all():
            if not legacy_leaflet.date_uploaded:
                if legacy_leaflet.date_delivered:
                    legacy_leaflet.date_uploaded = legacy_leaflet.date_delivered

            if legacy_leaflet.date_uploaded:
                if not bool(legacy_leaflet.publisher_party_id):
                    party = None
                else:
                    party = Party.objects.find_party_by_name(
                        legacy_leaflet.publisher_party.name)

                    cons = legacy_leaflet.legacyleafletconstituency_set.all()
                    con = None
                    if cons:
                        con = cons[0]
                        con = self.clean_constituency(con)

                    # import ipdb
                    # ipdb.set_trace()
                    new_leaflet, created = Leaflet.objects.update_or_create(
                        pk=legacy_leaflet.pk,
                        defaults=self.clean_legacy_leaflet(
                            legacy_leaflet,
                            party,
                            constituency=con
                            ))

                    # for legacy_image in legacy_leaflet.images.all():
                    #     new_image, created = LeafletImage.objects.update_or_create(
                    #     leaflet=new_leaflet,
                    #     legacy_image_key=legacy_image.image_key,
                    #     defaults=self.clean_legacy_leaflet_image(legacy_image))
                    #
                    #