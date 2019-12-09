# act_human
#### A Twilio-based text bot to remind me to act like a human during the work day

This app has two objectives:
1. Learn to use the Twilio SMS API
2. Get better at making myself act like a human at work.

Also, ostensibly, practicing Python, but that's just all the time.

##### What It Actually Does:

* Creates a daily, randomized schedule with four event timeframes:
  1. AM reminder, between 10AM - noon
  2. Lunch reminder, between noon and 1PM
  3. PM reminder, between 2PM and 5PM
  4. EOD/go home reminder, between 5PM and 6PM
* Sleeps between event windows
* At the time of an event, pulls a random reminder from a list of reminders
* Texts that reminder to me
* Sleeps until the next event

The reminders are based on making sure that I actually do things, like fix my posture, drink water, go to lunch, go home at the end of the day, etc. I'm a trashfire catastrophe, friends, so I need computers to take care of me.

I was originally doing something like this with Slackbot in my work Slack instance, but found that since Slackbot always arrives at a set time, I would just see it and dismiss it to get the notification to go away. I'm hoping that the randomized nature of the event time, and the fact that it will show up in my text messages (way more exciting than a work-related notification!) will help me do better.

This is insanely simple to utilize if you want to give it a try. Just set up your own `.env` file with your Twilio SID, auth token, and send number, then add your recipient number. You could absolutely modify this to work for multiple people, and maybe I will at some point, but right now I just have my own number hardcoded into my `.env` file, since I'm the only one I'm sending to.

The `msgs.py` file is where I keep the lists of reminders, broken out by time frame. Have fun tweaking and personalizing those. Integrate with a kitten picture API? Not a bad idea.

This is one of my first independent projects not done as part of bootcamp or for my work, so it's kind of janky and ugly, but I had a lot of fun learning some new stuff and designing this little friendo. I hope you have fun with it too!
