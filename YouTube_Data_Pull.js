var API_KEY = '';
var PLAYLIST_ID = '';

function getPlaylistData() {
  var playlistItemsUrl = 'https://www.googleapis.com/youtube/v3/playlistItems';
  
  var parameters = {
    part: 'snippet',
    maxResults: 50,
    playlistId: PLAYLIST_ID,
    key: API_KEY
  };
  
  var response = UrlFetchApp.fetch(playlistItemsUrl + '?' + toBeautyString(parameters));
  var json = JSON.parse(response.getContentText());
  
  var items = json.items;

  var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  sheet.clear();

  sheet.getRange(1, 1, 1, 1).setValues([['Video Title']]);

  var data = [];
  for (var i = 0; i < items.length; i++) {
    var item = items[i];
    var title = item.snippet.title;
    data.push([title]);
  }
  
  sheet.getRange(2, 1, data.length, 1).setValues(data);
  
  Logger.log('Data retrieved from playlist');
}

function toBeautyString(parameters) {
  return Object.keys(parameters).map(function(key) {
    return encodeURIComponent(key) + '=' + encodeURIComponent(parameters[key]);
  }).join('&');
}
//example o/p of this func would be: part=snippet&maxResults=50&playlistId=PLWz5rJ2EKKc9cb1TNriI84Y6Y6dh3fZF5&key=YOUR_API_KEY
