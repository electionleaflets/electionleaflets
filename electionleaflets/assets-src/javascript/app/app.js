/*global Ember, DS, Leaflets:true */


// window.Leaflets = Ember.Application.create({
//   LOG_TRANSITIONS: true,
//   rootElement: '#LeafletUploader'
// });

// Leaflets.Store = DS.Store.extend({
//   adapter: DS.RESTAdapter
// })

$('.file_input_button').change(function() {
  var el = $(this);
  var file = el.find('input')[0].files[0];
  var fr = new FileReader();
  fr.onload = receivedImage;
  fr.readAsDataURL(file);
  function receivedImage() {
    $('.file_input_preview *').remove();
    el.find('.action').text('edit')
    var img = $('<img class="uploaded_image">');
    img.attr('src', this.result);
    $('.file_input_preview').append(img);
  }
  
  
  
})