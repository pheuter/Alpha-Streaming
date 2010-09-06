// The following is a snippet from the Chrome Alpha Extension for Google Chrome
// If a Wolfram Alpha query is successfully received, notify the rack server
// A GET request is made and some basic information is provided

$.ajax({
	type: "GET",
	url: query_url,
	dataType: "xml",
	success: function(wolfram) {
		$.ajax({
			type: "POST",
			url: "http://alpharack.heroku.com",
			data:"url=http://www.wolframalpha.com/input/?i="+escape($("input[name='query']").val())+"&type=chrome&image_url="+escape($(wolfram).find("pod").find("subpod").find("img").attr("src")),
			success: function(m) {
				parseXml(wolfram);
			}
		});
	}
});