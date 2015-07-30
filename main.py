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
        self.response.write(template.render())


class Note(ndb.Model):
    NoteWords = ndb.StringProperty()

class AddNotesHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template("addnotes.html")
        self.response.write(template.render())

class ExistingNotesHandler(webapp2.RequestHandler):
    def post(self):
        entry_note = self.request.get("note")
        your_note = Note(NoteWords = entry_note)
        your_note.put()
        list_of_notes = Note.query().fetch()
        list_of_notes.append(your_note)
        template = jinja_environment.get_template("existingnotes.html")
        self.response.write(template.render({"list_of_notes": list_of_notes}))

class Goal(ndb.Model):
    GoalWords = ndb.StringProperty()
    GoalTime = ndb.StringProperty()

class AddGoalsHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template("addgoals.html")
        self.response.write(template.render())

class ExistingGoalsHandler(webapp2.RequestHandler):
    def post(self):
        entry_number = self.request.get("goal_time")
        entry_words = self.request.get("goal_writing")
        new_goal = Goal(GoalTime = entry_number, GoalWords = entry_words)
        new_goal.put()
        list_of_goals = Goal.query().fetch()
        list_of_goals.append(new_goal)
        template = jinja_environment.get_template("existinggoals.html")
        self.response.write(template.render({"list_of_goals": list_of_goals}))


class ProgressHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template("progress.html")
        self.response.write(template.render())



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

        template_vars = {"duration": stopwatch_data.endtime - stopwatch_data.starttime}
        template_vars = {"duration": stopwatch_data.endtime - stopwatch_data.starttime,
        "maxMeter": Goal.query().fetch()[-1].GoalTime}
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

class WritingHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template("writing.html")
        self.response.write(template.render())


class StorytellingHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template("storytelling.html")
        self.response.write(template.render())

class LiteratureHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template("literature.html")
        self.response.write(template.render())


class GeometryHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template("geometry.html")
        self.response.write(template.render())

class CalculusHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template("calculus.html")
        self.response.write(template.render())

class StatisticsHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template("statistics.html")
        self.response.write(template.render())

class LifeScienceHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template("lifescience.html")
        self.response.write(template.render())

class ChemistryHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template("chemistry.html")
        self.response.write(template.render())

class PhysicsHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template("physics.html")
        self.response.write(template.render())

class HistoryHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template("history.html")
        self.response.write(template.render())

class PsychologyHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template("psychology.html")
        self.response.write(template.render())

class PhilosophyHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template("philosophy.html")
        self.response.write(template.render())

class PerformingArtsHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template("performingarts.html")
        self.response.write(template.render())

class DigitalMediaHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template("digitalmedia.html")
        self.response.write(template.render())

class FineArtsHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template("finearts.html")
        self.response.write(template.render())

jinja_environment = jinja2.Environment(loader = jinja2.FileSystemLoader(os.path.dirname(__file__)))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/login', LoginHandler),
    ('/rewards', RewardsHandler),
    ('/addgoals', AddGoalsHandler),
    ('/existinggoals', ExistingGoalsHandler),
    ('/addnotes', AddNotesHandler),
    ('/existingnotes', ExistingNotesHandler),
    ('/progress', ProgressHandler),
    ('/literature', LiteratureHandler),
    ('/stopwatchstart', StopwatchStartHandler),
    ('/writing', WritingHandler),
    ('/storytelling', StorytellingHandler),
    ('/geometry', GeometryHandler),
    ('/calculus', CalculusHandler),
    ('/statistics', StatisticsHandler),
    ('/lifescience', LifeScienceHandler),
    ('/chemistry', ChemistryHandler),
    ('/physics', PhysicsHandler),
    ('/history', HistoryHandler),
    ('/psychology', PsychologyHandler),
    ('/philosophy', PhilosophyHandler),
    ('/performingarts', PerformingArtsHandler),
    ('/digitalmedia', DigitalMediaHandler),
    ('/finearts', FineArtsHandler),
    ('/stopwatchstop', StopwatchStopHandler)

], debug=True)
