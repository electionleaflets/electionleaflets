import logging
import os

from sorl.thumbnail import ImageField
import pytesser
from PIL import Image
from PIL import ImageEnhance

from django.db import models

from tags.models import Tag
from categories.models import Category
from constituencies.models import Constituency
from uk_political_parties.models import Party

import constants

def update_filename(instance, filename):
    import uuid
    import os

    path = "uploads/"
    _, ext = os.path.splitext(filename)
    return os.path.join(path, str(uuid.uuid4()) + ext)


class UploadSession(models.Model):
    key = models.CharField(max_length=64, null=True, blank=True)
    image1 = models.ImageField(upload_to=update_filename, max_length=255,
                                null=True, blank=True)
    image2 = models.ImageField(upload_to=update_filename, max_length=255,
                                null=True, blank=True)
    image3 = models.ImageField(upload_to=update_filename, max_length=255,
                                null=True, blank=True)
    image4 = models.ImageField(upload_to=update_filename, max_length=255,
                                null=True, blank=True)
    image5 = models.ImageField(upload_to=update_filename, max_length=255,
                                null=True, blank=True)
    image6 = models.ImageField(upload_to=update_filename, max_length=255,
                                null=True, blank=True)
    image7 = models.ImageField(upload_to=update_filename, max_length=255,
                                null=True, blank=True)
    image8 = models.ImageField(upload_to=update_filename, max_length=255,
                                null=True, blank=True)
    s3keys = models.TextField(null=True, blank=True)

    def names(self):
        vals = []
        for x in range(1, 9):
            img = getattr(self, 'image%s' % x)
            if img:
                name = str(img).split('/')[-1]
                vals.append(name.split('.')[0])
        return vals

    def resize_file(self, fl, name, w, h):
        from PIL import Image
        from django.conf import settings
        import os

        x = w
        y = h

        srcpath = os.path.join(settings.MEDIA_ROOT, str(fl))
        path, ext = os.path.splitext(srcpath)
        parts = path.split('/')
        outpath = '/'.join(parts[:-1])
        outpath = os.path.join(outpath, name)

        outpath = os.path.join(outpath, parts[-1])
        outpath = outpath + '.jpg'

        try:
            f = open(srcpath, 'rb')
            image = Image.open(f)
            if image.mode not in ("L", "RGB"):
                image = image.convert("RGB")

            img_ratio = float(image.size[0]) / image.size[1]
            if x == 0.0:
                x = y * img_ratio
            elif y == 0.0:
                y = x / img_ratio
            x = int(x)
            y = int(y)

            img = image.resize((x, y,), Image.ANTIALIAS)
            img.save(outpath, "JPEG")
        except:
            return None

        return outpath

    def handle_file_uploads(self):
        for x in range(1, 9):
            img = getattr(self, 'image%s' % x)
            if img:
                f = self.resize_file(img, 'thumbnail', 140, 0)
                self.send_to_s3(f, "thumbnail")

                f = self.resize_file(img, 'small', 120, 0)
                self.send_to_s3(f, "small")

                f = self.resize_file(img, 'medium', 300, 0)
                self.send_to_s3(f, "medium")

                f = self.resize_file(img, 'large', 1024, 0)
                self.send_to_s3(f, "large")

    def send_to_s3(self, filename, folder):
        """
        Send the source file, filename, to S3 (if enabled) and store it in
        the named folder.
        """
        from django.conf import settings
        from third_party import S3

        import os.path
        import sys

        if not settings.S3_ENABLED:
            return

        if filename is None:
            # TODO: We need to log the error (and alert an admin)
            return

        try:
            conn = S3.AWSAuthConnection(settings.AWS_KEY, settings.AWS_SECRET)
            filedata = open(filename, 'rb').read()
            content_type = 'image/jpeg'

            newname = '%s/%s' % (folder, os.path.basename(filename),)
            #logging( "Uploading %s as %s" % (filename,newname,)

            conn.put(settings.S3_BUCKET, newname, S3.S3Object(filedata),
                {'x-amz-acl': 'public-read', 'Content-Type': content_type})
            del conn
        except:
            logging.error("Unexpected error:", sys.exc_info()[0])


class Leaflet(models.Model):
    title = models.CharField(blank=True, max_length=765)
    description = models.TextField(blank=True, null=True)
    publisher_party = models.ForeignKey(Party, blank=True, null=True)
    constituency = models.ForeignKey(Constituency, blank=True, null=True)

    attacks = models.ManyToManyField(Party, related_name='attacks',
        null=True, blank=True)
    tags = models.ManyToManyField(Tag, through='LeafletTag')
    categories = models.ManyToManyField(Category, through='LeafletCategory')
    imprint = models.TextField(blank=True, null=True)
    postcode = models.CharField(max_length=150, blank=True)
    lng = models.FloatField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    name = models.CharField(blank=True, max_length=300)
    email = models.CharField(blank=True, max_length=300)
    date_uploaded = models.DateTimeField(auto_now_add=True)
    date_delivered = models.DateTimeField(blank=True, null=True)
    status = models.CharField(choices=constants.LEAFLET_STATUSES,
        null=True, blank=True, max_length=255)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        from django.contrib.sites.models import Site
        return 'http://%s/leaflets/%s/' % (Site.objects.get_current().domain,
            self.id)

    def get_first_image(self):
        try:
            return self.images.all()[0]
        except IndexError:
            # TODO: Set image_key to value for 'empty' image
            return None

    def get_title(self):
        if self.title and len(self.title):
            return self.title
        elif self.publisher_party:
            return '%s leaflet' % self.party.name
        else:
            "Untitled leaflet"


class LeafletImage(models.Model):
    leaflet = models.ForeignKey(Leaflet, related_name='images')
    image = ImageField(upload_to="leaflets")
    legacy_image_key = models.CharField(max_length=255)
    image_type =  models.CharField(choices=constants.IMAGE_TYPES,
        null=True, blank=True, max_length=255)
    image_text = models.TextField(blank=True)

    class Meta:
        ordering = ['image_type']

    def ocr(self):
        if not self.image:
            return ""

        from PIL import ImageFilter

        image_path = self.image.path
        tmp_image_path = "/tmp/leaflet_image-%s.jpg" % self.legacy_image_key
        # image_file = Image.open(image_path) # open colour image
        # image_file = image_file.filter(ImageFilter.EDGE_ENHANCE)
        # image_file = image_file.filter(ImageFilter.SMOOTH_MORE)
        # image_file = image_file.filter(ImageFilter.FIND_EDGES)
        # image_file = image_file.filter(ImageFilter.DETAIL)
        # image_file = image_file.filter(ImageFilter.MinFilter(3))
        # image_file = image_file.convert('L') # convert image to black and white
        # image_file = ImageEnhance.Contrast(image_file)
        # image_file = image_file.enhance(1.5)

        # image_file.save(tmp_image_path, dpi=(300,300))

        text = pytesser.image_to_string(image_path)
        text = os.linesep.join([s for s in text.splitlines() if s])
        self.image_text = text
        self.save()
        os.remove(image_path)
        return text


class LeafletCategory(models.Model):
    leaflet = models.ForeignKey(Leaflet)
    category = models.ForeignKey(Category)


class LeafletTag(models.Model):
    leaflet = models.ForeignKey(Leaflet)
    tag = models.ForeignKey(Tag)

    def __unicode__(self):
        return u'tagged %s' % (self.tag.tag,)


class Promise(models.Model):
    promise_id = models.IntegerField(primary_key=True)
    leaflet_id = models.IntegerField()
    detail = models.TextField()


class RateInteresting(models.Model):
    rate_interesting_id = models.IntegerField(primary_key=True)
    leaflet_id = models.IntegerField()
    description = models.TextField()
    user_name = models.CharField(max_length=765)
    user_email = models.CharField(max_length=765)


class RateInterestingSeq(models.Model):
    sequence = models.IntegerField(primary_key=True)


class RateType(models.Model):
    rate_type_id = models.IntegerField(primary_key=True)
    left_label = models.CharField(max_length=150)
    right_label = models.CharField(max_length=150, blank=True)


class RateValue(models.Model):
    rate_value_id = models.IntegerField(primary_key=True)
    leaflet_id = models.IntegerField()
    user_name = models.CharField(max_length=300)
    user_email = models.CharField(max_length=300)
    rate_type_id = models.IntegerField()
    value = models.IntegerField()


class RateValueSeq(models.Model):
    sequence = models.IntegerField(primary_key=True)
