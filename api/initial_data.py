from .models import User, Society, Activity, Point


# activities
interview = Activity(name="Bootcamp Interviews",
                     description="Interviewing candidate for a fellow"
                                 " recruiting event",
                     value=20)
open_saturdays = Activity(name="Open Saturdays Guides",
                          description="Guide applicants with the recruitment"
                                      " team during open Saturdays",
                          value=50)
tech_event = Activity(name="Tech Event",
                      description="Organize a tech event",
                      value=2500)
open_source = Activity(name="Open Source Project",
                       description="Starting an open source project which has"
                                   " at least 40 stars from non-Andelans",
                       value=2500)
hackathon = Activity(name="Hackathon",
                     description="Participating in a Hackathon",
                     value=100)
blog = Activity(name="Blog",
                description="Write a blog that is published on Andela's"
                            " website",
                value=1000)
app = Activity(name="App",
               description="Build an app that is marketed on Andela's website",
               value=10000)
mentor = Activity(name="Mentoring",
                  description="Mentor a prospect for Andela 21",
                  value=250)
marketing = Activity(name="Marketing",
                     description="Participating in an Andela marketing event"
                                 " with partners",
                     value=2000)
press = Activity(name="Press Interview",
                 description="Participating in a press interview for"
                             " Andela marketing",
                 value=3000)
outside_mentoring = Activity(name="External Mentoring",
                             description="Mentoring students outside of Andela"
                                         " e.g. via SheLovesCode",
                             value=250)


all_data = [interview, open_saturdays, tech_event, open_source, hackathon,
            blog, app, mentor, marketing, press, outside_mentoring]
