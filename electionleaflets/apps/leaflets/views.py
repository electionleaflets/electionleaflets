import os

from django.template  import RequestContext
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.contrib.formtools.wizard.views import NamedUrlSessionWizardView
from django.core.urlresolvers import reverse
from django.conf import settings
from django.views.generic import DetailView, ListView, DetailView
from django.core.files.storage import FileSystemStorage

from .models import Leaflet, LeafletImage


class ImageView(DetailView):
    model = LeafletImage
    template_name = 'leaflets/full.html'
    pk_url_kwarg = 'image_key'

# def view_full_image(request, image_key):
#
#     li = LeafletImage.objects.filter(pk=image_key)
#     if li.count() == 1:
#         li = get_object_or_404(LeafletImage, image_key=image_key)
#     else:
#         # Should not do this, we'll need to fix it
#         # probably and upload artifact
#         li = li.all()[0]
#
#     return render_to_response('leaflets/full.html',
#                             {
#                                 'image': li,
#                                 'leaflet': li.leaflet,
#                             },
#                             context_instance=RequestContext(request), )


def view_all_full_images(request, leafletid):
    from leaflets.models import Leaflet, LeafletImage

    leaflet = get_object_or_404(Leaflet, pk=leafletid)
    images = LeafletImage.objects.filter(leaflet=leaflet)

    return render_to_response('leaflets/full_all.html',
                            {
                                'images': images,
                                'leaflet': leaflet,
                            },
                            context_instance=RequestContext(request), )


class LatestLeaflets(ListView):
    model = Leaflet
    template_name = 'leaflets/index.html'
    paginate_by = 60


class LeafletView(DetailView):
    template_name = 'leaflets/leaflet.html'
    queryset = Leaflet.objects.all()


class LeafletUploadWizzard(NamedUrlSessionWizardView):
    TEMPLATES = {
        "front": "leaflets/upload_form/image_form.html",
        "postcode": "leaflets/upload_form/postcode.html",
        "cc": "checkout/creditcard.html",
        "confirmation": "checkout/confirmation.html",
    }

    # template_name = "leaflets/upload_form/image_form.html"
    file_storage = FileSystemStorage(location=os.path.join(
        settings.MEDIA_ROOT, 'images/leaflets_tmp'))

    def get_template_names(self):
            return [self.TEMPLATES[self.steps.current]]

    # def render_next_step(self, form, **kwargs):
    #         data = get_cleaned_data('2')  # or whatever your step with the
    # flag is
    #         if data.get('your_flag', False):
    #             self.storage.reset()
    #             return HttpResponseRedirect()
    #         return super(Wizard, self).render_next_step(self, form, **kwargs)

    def done(self, form_list, **kwargs):
        #Create a new leaflet
        leaflet = Leaflet()
        leaflet.save()

        # Front
        front_image = LeafletImage(leaflet=leaflet, image_type="1_front")
        front_image.image = form_list[0].cleaned_data['image']
        front_image.save()

        return  redirect(reverse('leaflet', kwargs={'pk': leaflet.pk}))
