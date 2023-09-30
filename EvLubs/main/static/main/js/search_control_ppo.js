// (function() {
//     var placeAutoComplete = places({
//         appId: 'AN12KG8ZN1',
//         apiKey: 'f69d2b0500ecb88a26b244e40b9e708c',
//         container: document.querySelector('#address'),
//         templates: {
//             value: function(suggestion) {
//                 return suggestion.name;
//             }
//         }
//     }).configure({
//         type: 'address'
//     });

//     placesAutoComplete.on('change', function resultSelected(e) {
//         document.querySelector('#state').value = e.suggestion.administrative || '';
//         document.querySelector('#citya').value = e.suggestion.city || '';
//         document.querySelector('#postalCode').value = e.suggestion.postalCode || '';
//     })
// })();
