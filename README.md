#           FlairX Hosting Tutorial(old guide, please dont try it again)           #
#        How to run this Reddit bot 24/7      #

This guide will walk you step-by-step through TWO different hosting methods:

1. Hosting on Railway (recommended, easier, cleaner)
2. Hosting on Replit (backup option if Railway free hours run out)

Both options are fully supported. You don’t need coding knowledge, just patience and following the steps carefully.


# OPTION 1: Hosting FlairX on RAILWAY (Paid) #

Railway is a cloud platform that can run your bot in the background
without requiring UptimeRobot or extra tricks. It’s the easiest way.

STEP 1: Create a Railway account
- Go to https://railway.app
- Sign in with your GitHub account
- You’ll need to link your GitHub repo (where FlairX is stored)

STEP 2: Prepare your repo for Railway
Make sure your GitHub repo has these two important files:

1) requirements.txt
   This file tells Railway which Python libraries to install.
   Example content:
   praw
   python-dotenv
   (add more if your bot uses them, e.g. requests, flask, etc.)

2) Procfile
   This tells Railway how to run your bot.
   Example content:
   worker: python3 main.py

   - “worker” = background task that stays running
   - “python3 main.py” = starts your bot file

STEP 3: Deploy to Railway
- Go to Railway dashboard
- Click “New Project” → “Deploy from GitHub Repo”
- Select your FlairX repo
- Railway will automatically install requirements.txt

STEP 4: Add your Environment Variables
These are your secrets. Don’t put them in code. 
Go to Railway → Project → Variables → Add:

```python
REDDIT_CLIENT_ID=your_client_id_here
REDDIT_CLIENT_SECRET=your_client_secret_here
REDDIT_USER_AGENT=your_user_agent_here
REDDIT_USERNAME=your_reddit_username
REDDIT_PASSWORD=your_reddit_password
SUBREDDITS=funny,memes,test   (comma separated)
```

STEP 5: Start your bot
Railway should auto-detect and start using the Procfile.
If not, go to Project Settings → Start Command → type:
python3 main.py

STEP 6: Confirm it’s working
- Go to Railway → Deployments → Logs
- You should see:
  “Bot started in r/test1+test_+test...”
- That means FlairX is alive and running

STEP 7: Keep it alive
- Free plan gives 500 free hours/month (about 20 days nonstop)
- When hours run out, your bot pauses until next month resets
- If you want true 24/7 uptime, upgrade plan ($5/month)
- OR switch to Replit temporarily (see below)


# OPTION 2: Hosting FlairX on REPLIT (hosting url also paid sadly, uptimerobot is free) #

Replit doesn’t keep bots alive on its own. 
You’ll need to use a “keep_alive.py” file + UptimeRobot.

STEP 1: Create a Replit account
- Go to https://replit.com
- Sign up with Google/GitHub

STEP 2: Import your repo
- Create a new Python project
- Connect it to your GitHub repo with FlairX

STEP 3: keep_alive.py
- This file runs a small webserver
- Example (already included in repo):


```python
  from flask import Flask
  from threading import Thread

  app = Flask('')

  @app.route('/')
  def home():
      return "FlairX is alive!"

  def run():
      app.run(host='0.0.0.0', port=8080)

  def keep_alive():
      t = Thread(target=run)
      t.start()
```

STEP 4: Edit main.py
- At the top, import keep_alive if available:
  try:

```python
from keep_alive import keep_alive
      USE_KEEP_ALIVE = True
  except ImportError:
      USE_KEEP_ALIVE = False
```

- Before starting the bot:
  if USE_KEEP_ALIVE:

```python
        keep_alive()
```

- This way:
  Railway users → doesn’t matter
  Replit users → keeps bot alive via Flask

STEP 5: Add Environment Variables
- In Replit, go to “Secrets (Environment Variables)”
- Add the same vars as Railway:

```python
  REDDIT_CLIENT_ID
  REDDIT_CLIENT_SECRET
  REDDIT_USER_AGENT
  REDDIT_USERNAME
  REDDIT_PASSWORD
  SUBREDDITS
```

STEP 6: Use UptimeRobot
- Go to https://uptimerobot.com
- Create a free account
- Add a “New Monitor” → HTTP(s)
- Paste your Replit web URL (it looks like https://yourproject.yourname.repl.co)
- UptimeRobot will ping your bot every 5 minutes to keep it alive

STEP 7: Confirm it’s working
- Check Replit console logs
- Should print:
  “Bot started in r/funny+memes+test...”

STEP 8: Done
- Your bot now stays alive as long as UptimeRobot keeps pinging it
- No downtime unless Replit restarts or has issues


# Final Notes #

- RAILWAY: simpler, no UptimeRobot needed, but free plan = 500 hrs
- REPLIT: works with paid plan with url + UptimeRobot, can run 24/7
- Keep both options available for flexibility
- NEVER put your Reddit passwords or secrets in your code (replit)
- Always use environment variables
- Keep your repo clean so others can easily fork + host


# End of Tutorial — Good luck with FlairX!     #

