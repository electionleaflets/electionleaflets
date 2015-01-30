/*global Ember, DS, Leaflets:true */

window.Leaflets = Ember.Application.create({
  LOG_TRANSITIONS: true,
  rootElement: '#LeafletUploader'
});

// Leaflets.Store = DS.Store.extend({
//   adapter: DS.RESTAdapter
// })
