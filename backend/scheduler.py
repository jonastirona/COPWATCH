"""
Scheduler module for COPWATCH
Handles scheduled tasks and background jobs
"""

import schedule
import time
from datetime import datetime


class TaskScheduler:
    def __init__(self):
        self.jobs = []
    
    def add_job(self, func, interval, unit='minutes'):
        """Add a scheduled job"""
        job = getattr(schedule.every(interval), unit).do(func)
        self.jobs.append(job)
        return job
    
    def start(self):
        """Start the scheduler"""
        print(f"Scheduler started at {datetime.now()}")
        while True:
            schedule.run_pending()
            time.sleep(1)
    
    def stop(self):
        """Stop all scheduled jobs"""
        schedule.clear()
        self.jobs.clear()
        print("Scheduler stopped")


# Global scheduler instance
scheduler = TaskScheduler() 