require 'rubygems'
require 'sinatra'
require 'pusher'
require 'couchrest'

Pusher.app_id = '1160'
Pusher.key = 'appkey'
Pusher.secret = 'appsecret'

db = CouchRest.database("http://webapp.com:couchdbport")

post '/' do
  if params[:url] != nil
    Pusher['stream'].trigger('new-query', {:type => params[:type], :image_url => params[:image_url], :url => params[:url]}) 
    db.save_doc({:type => params[:type], :image_url => params[:image_url], :url => params[:url], :created_at => Time.now}) if params[:url] != nil
  end
end