import re
import json
from datetime import datetime
from openclaw import cron, message

def run(args):
    """
    Dynamic Scheduler: add tasks through chat commands.
    Example message: "Every day at 8 AM, fetch AI news and send via WhatsApp"
    """
    user_msg = args.get("message", "").strip()
    if not user_msg:
        return "No message received"

    # Simple regex to parse time e.g., "8 AM" or "08:30"
    time_match = re.search(r"(\d{1,2})(?::(\d{2}))?\s*(AM|PM)?", user_msg, re.IGNORECASE)
    if not time_match:
        return "Could not find a valid time in your message."

    hour = int(time_match.group(1))
    minute = int(time_match.group(2) or 0)
    ampm = time_match.group(3)

    if ampm and ampm.upper() == "PM" and hour != 12:
        hour += 12
    elif ampm and ampm.upper() == "AM" and hour == 12:
        hour = 0

    cron_expr = f"{minute} {hour} * * *"

    # Create cron payload
    job_payload = {
        "action": "add",
        "job": {
            "name": f"DynamicTask_{datetime.now().strftime('%Y%m%d%H%M%S')}",
            "schedule": {"kind": "cron", "expr": cron_expr},
            "payload": {
                "kind": "agentTurn",
                "message": user_msg
            }
        }
    }

    # Add job to OpenClaw cron
    cron.add_job(job_payload)

    return f"✅ Scheduled task added at {hour:02d}:{minute:02d} → {user_msg}"
