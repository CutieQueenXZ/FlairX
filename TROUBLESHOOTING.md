#        FlairX Hosting Troubleshooting       #

This section lists the most common problems you might face when hosting FlairX
on Railway or Replit, along with their solutions.

#              GENERAL PROBLEMS                #

❌ Problem: Bot doesn’t reply to any comments
✔ Solution:
- Double-check your Reddit credentials in environment variables.
- Make sure REDDIT_USERNAME and REDDIT_PASSWORD are correct.
- Verify your Reddit account is NOT shadowbanned (try posting a test comment).
- Check SUBREDDITS variable — if it’s empty, the bot has nowhere to listen.

❌ Problem: Error "praw not found" or "dotenv not found"
✔ Solution:
- You forgot to list dependencies in requirements.txt
- Add these lines (at minimum):
  praw
  python-dotenv
- Push the file again, then redeploy.

❌ Problem: "AttributeError: module 'praw' has no attribute 'Reddit'"
✔ Solution:
- This happens if you accidentally installed a wrong library (like prawcore).
- Reinstall praw properly:
  pip uninstall prawcore
  pip install praw

#            RAILWAY-SPECIFIC ISSUES           #

❌ Problem: Bot dies after ~20 days
✔ Solution:
- Free Railway plan = 500 hours/month.
- A month = ~720 hours, so you’ll run out of free hours.
- Either wait until the next month resets or upgrade to the $5/month plan.

❌ Problem: "No such process" or bot not starting
✔ Solution:
- Check Procfile is correct. It must be at the root of your repo.
- Content must be exactly:
  worker: python3 main.py

❌ Problem: "requirements.txt not found"
✔ Solution:
- Create requirements.txt in your repo root with your dependencies.
- Railway auto-installs from this file.


#            REPLIT-SPECIFIC ISSUES           #

❌ Problem: Replit bot stops running when I close browser
✔ Solution:
- Replit free projects don’t run in the background forever.
- You must use keep_alive.py + UptimeRobot to ping your bot.

❌ Problem: UptimeRobot says "Down"
✔ Solution:
- Copy your full Replit web URL (looks like https://project.username.repl.co)
- Paste it in UptimeRobot as an HTTP(s) monitor, check every 5 minutes.

❌ Problem: Flask already running / Port in use
✔ Solution:
- Sometimes when restarting, Replit tries to run two Flask servers.
- Stop your project fully, then restart.

❌ Problem: Bot not responding after hours
✔ Solution:
- Replit might restart projects sometimes.
- Make sure UptimeRobot is active.
- If still broken, check Replit console logs for errors.


# OTHER COMMON QUESTIONS #

❓ Q: Can I use both Railway and Replit?
✔ A: Yes! You can switch between them anytime. Railway is cleaner,
   Replit is backup if free hours run out.

❓ Q: Do I need keep_alive.py on Railway?
✔ A: No. Railway does not require pings. keep_alive.py is only for Replit.

❓ Q: How do I update my bot?
✔ A: Just push changes to your GitHub repo. Railway or Replit will redeploy
   the latest version automatically.

❓ Q: Is my Reddit account safe?
✔ A: Use a dedicated Reddit account for bots, not your personal one.
   If Reddit suspends it, your personal account won’t be affected.

# End of Troubleshooting — Happy hosting!     #
