"""Scheduler service for job automation."""

class Scheduler:
    """Job scheduler."""
    
    def __init__(self):
        self.callback = None
        self.is_running = False
    
    def set_automation_callback(self, callback):
        """Set the automation callback."""
        self.callback = callback
    
    def start(self):
        """Start scheduler."""
        self.is_running = True
    
    def stop(self):
        """Stop scheduler."""
        self.is_running = False

_scheduler = Scheduler()

def get_scheduler():
    """Get the scheduler instance."""
    return _scheduler
