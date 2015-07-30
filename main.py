#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import jinja2
import os
import datetime
import logging
from google.appengine.ext import ndb
from google.appengine.api import users
import time




class MainHandler(webapp2.RequestHandler):
    def get(self):
        key_name = self.request.get("key_name")
        template_vars = {"timeofday": time.asctime(), "key_name": key_name}
        user = users.get_current_user()
        if user:
            logging.info(user)
            so_url = users.create_logout_url('/')
            template_vars["logout"]= "<a href="+so_url+">Welcome! sign out</a>"
            template = jinja_environment.get_template("homepage.html")
            self.response.write(template.render(template_vars))
            greeting = ('Welcome, %s! (<a href="%s">sign_out</a>)' %
                (user.nickname(), users.create_logout_url('/')))
        else:
            template_vars["login"] = "<a href="+users.create_login_url('/')+">Sign in</a>"
            logging.info("user is not logged in")
            template = jinja_environment.get_template("login.html")
            self.response.write(template.render(template_vars))


class RewardsHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template("rewards.html")
        self.response.write(template.render)

class NotesHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template("notes.html")
        self.response.write(template.render)

class ProgressHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template("progress.html")
        self.response.write(template.render)



class Stopwatch(ndb.Model):
    starttime = ndb.DateTimeProperty()
    endtime = ndb.DateTimeProperty()


class StopwatchStartHandler(webapp2.RequestHandler):
    def get(self):
        starttime = datetime.datetime.now()
        stopwatch1 = Stopwatch(starttime=starttime)
        stopwatch_key = stopwatch1.put()
        urlsafe_key = stopwatch_key.urlsafe()
        self.redirect('/?key_name=%s' %urlsafe_key)


class StopwatchStopHandler(webapp2.RequestHandler):
    def get(self):
        key_name = self.request.get("key_name")
        logging.info(key_name)
        stopwatch_key = ndb.Key(urlsafe=key_name)
        stopwatch = stopwatch_key.get()
        stopwatch.endtime = datetime.datetime.now()
        stopwatch.put()
        stopwatch_query = Stopwatch.query()
        stopwatch_query_ordered = stopwatch_query.order(-Stopwatch.endtime)
        stopwatch_list = stopwatch_query_ordered.get()
        stopwatch_data = stopwatch_list
        self.response.write(stopwatch_data.endtime - stopwatch_data.starttime)
        template_vars = {"duration": stopwatch_data.endtime - stopwatch_data.starttime}
        template = jinja_environment.get_template("stopwatch.html")
        self.response.write(template.render(template_vars))



class LoginHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            greeting = ('Welcome, %s! (<a href="%s">sign_out</a>)' %
                (user.nickname(), users.create_logout_url('/')))
        else:
            greeting = ('<a href="%s">Sign in or register</a>.' %
                users.create_login_url('/'))
        self.response.write('<html><body>%s</body></html>' % greeting)





jinja_environment = jinja2.Environment(loader = jinja2.FileSystemLoader(os.path.dirname(__file__)))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/login', LoginHandler),
    ('/rewards', RewardsHandler),
    ('/notes', NotesHandler),
    ('/progress', ProgressHandler),
    ('/stopwatchstart', StopwatchStartHandler),
    ('/stopwatchstop', StopwatchStopHandler)

], debug=True)
