# alerts/alert_handler.py

class Alert:
    def __init__(self, source, timestamp, message):
        self.source = source
        self.timestamp = timestamp
        self.message = message

class AlertHandler:
    def __init__(self):
        self.alerts = []

    def generate_alert(self, source, message):
        # This method creates a new alert and adds it to the list
        alert = Alert(source, self.get_current_timestamp(), message)
        self.alerts.append(alert)

    def get_alerts(self):
        # This method returns the list of alerts
        return self.alerts

    def clear_alerts(self):
        # This method clears all existing alerts
        self.alerts = []

    def get_current_timestamp(self):
        # In a real system, you would use a more sophisticated way to get the current timestamp
        # This is a simple placeholder for demonstration purposes
        import datetime
        return datetime.datetime.now()

# Example Usage:

if __name__ == "__main__":
    # Create an instance of AlertHandler
    alert_handler = AlertHandler()

    # Generate some sample alerts
    alert_handler.generate_alert("Firewall", "Possible intrusion attempt detected.")
    alert_handler.generate_alert("Authentication System", "Multiple failed login attempts.")

    # Get and print the list of alerts
    alerts = alert_handler.get_alerts()
    print("Current Alerts:")
    for alert in alerts:
        print(f"Source: {alert.source}, Timestamp: {alert.timestamp}, Message: {alert.message}")

    # Clear alerts
    alert_handler.clear_alerts()
    print("Alerts Cleared.")
