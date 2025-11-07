require 'twilio-ruby'
require 'dotenv/load'

account_sid = ENV['TWILIO_ACCOUNT_SID']
auth_token = ENV['TWILIO_AUTH_TOKEN']
client = Twilio::REST::Client.new(account_sid, auth_token)

begin
  message = client.messages.create(
    from: ENV['TWILIO_PHONE_NUMBER'],
    to: '+919967640968', # replace with your own verified number
    body: 'Test message from Twilio Sandbox!'
  )
  puts "Message sent successfully! SID: #{message.sid}"
rescue Twilio::REST::RestError => e
  puts "Error: #{e.message}"
end