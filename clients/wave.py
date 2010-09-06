"""
The following is a snippet for the wave robot, specifically in the OnBlipSubmitted procedure
It basically sends a POST request to the rack server to dispatch that a query was submitted

Data:
  - Query type (wave)
  - Query image result source url
  - Bitly shortened url
"""

form_fields = {
  'type': 'wave', 
  'image_url': result_list[0].getElementsByTagName('subpod')[0].getElementsByTagName('img')[0].getAttribute('src'), 
  'url': bitly_url
}
form_data = urllib.urlencode(form_fields)
result = urlfetch.fetch(url="http://alpharack.heroku.com",
                        payload=form_data,
                        method=urlfetch.POST,
                        headers={'Content-Type': 'application/x-www-form-urlencoded'})