from apscheduler.schedulers.blocking import BlockingScheduler


def job_function():
    print "Hello World"

sched = BlockingScheduler()
sched.add_job(job_function, 'cron', hour=18, minute=16)
sched.start()