from .models import Activity, Point, Society, User

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

# socities
phoenix = Society(name="Phoenix")
istelle = Society(name="iStelle")
sparks = Society(name="Sparks")
invictus = Society(name="Invictus")

# test user
user = User(
    uuid="-KdQsMt2U0ixIy_-yJEH",
    name="Larry Wachira",
    photo="https://lh6.googleusercontent.com/-1DhBLOJentg/AAAAAAAAA"
          "AI/AAAAAAAAABc/ImM13eP_cAI/photo.jpg?sz=50",
    email="lawrence.wachira@andela.com",
    country="Kenya",
    society=phoenix
    )
user.activities.extend([blog, interview, open_saturdays])

# points for each activity
blog_points = Point(value=blog.value, activity=blog, user=user,
                    society=phoenix)
interview_points = Point(value=interview.value,
                         activity=interview, user=user, society=phoenix)
open_saturday_points = Point(value=open_saturdays.value,
                             activity=open_saturdays, user=user,
                             society=phoenix)


all_data = [interview, open_saturdays, tech_event, open_source, hackathon,
            blog, app, mentor, marketing, press, outside_mentoring, phoenix,
            istelle, sparks, invictus, user, blog_points, interview_points,
            open_saturday_points]
