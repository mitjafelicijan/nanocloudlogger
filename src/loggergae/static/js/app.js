$(document).ready(function () {
	
	
	
	setInterval(function() {
		
		$.getJSON(window.STREAM_SERVER_URL + 'get?stream=' + window.STREAM_ID, function(data) {
			console.log(data);
		});
	
	}, window.STREAM_READ_INTERVAL);
	
	
	
});