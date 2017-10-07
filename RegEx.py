import re
for test_string in ['555-1212', 'ILL-EGAL']:
    if re.match(r'^\d{3}-\d{4}$', test_string):
        print test_string, 'is a valid US local phone number'
    else:
        print test_string, 'rejected'

for test_email in ['bob@gmail.com', 'toddgmail.com', 'joe@gmailcom']:
    if re.match(r'[^@]+@[^@]+\.[^@]+', test_email):
        print test_email, 'is a valid email'
    else:
        print test_email, 'rejected'

for test_image_url in ['image.jpg', 'image.png', 'image.gif', 'notanimage.mp3', 'https://www.google.com/image.jpg', 'http://www.google.com/image.jpg']:
    if re.match(r'^https?:.*\.(jpg|png|gif)$', test_image_url):
        print test_image_url, 'is a valid image url'
    else:
        print test_image_url, 'rejected'

for test_username in ['usernameyay', 'thisisareallyreallyreallylongusername']:
    if re.match(r'^[a-z0-9_-]{3,16}$', test_username):
        print test_username, 'is a valid username'
    else:
        print test_username, 'rejected'

for test_password in ['thisisapassword', 'thisisapa$$word']:
    if re.match(r'^[a-z0-9_-]{6,18}$', test_password):
        print test_password, 'is a valid password'
    else:
        print test_password, 'rejected'

for test_hex_value in ['#a3c113', '#4d82h4']:
    if re.match(r'^#?([a-f0-9]{6}|[a-f0-9]{3})$', test_hex_value):
        print test_hex_value, 'is a valid hex value'
    else:
        print test_hex_value, 'rejected'

for test_slug in ['title-here', 'title_here']:
    if re.match(r'^[a-z0-9-]+$', test_slug):
        print test_slug, 'is a valid slug'
    else:
        print test_slug, 'rejected'

for test_url in ['http://google.com/some/file!.html', 'http://net.google.com/about']:
    if re.match('^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$', test_url):
        print test_url, 'is a valid url'
    else:
        print test_url, 'rejected'

for test_ip_address in ['73.60.124.136', '256.60.124.136']:
    if re.match(r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$', test_ip_address):
        print test_ip_address, 'is a valid url'
    else:
        print test_ip_address, 'rejected'
