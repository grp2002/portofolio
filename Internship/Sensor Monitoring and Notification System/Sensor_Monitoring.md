# Sensor Monitoring System - Java Console Application

## 📌 Overview
This section describes a **Java-based configurable console application** developed to monitor sensor activity. The system tracks the status of sensors, determining whether they are **online** and functioning properly or **offline** due to inactivity. Additionally, the application is responsible for sending email alerts when a sensor's status changes.

## 📂 Project Structure
- `Config.java` – Handles application configuration settings from a properties file.
- `DatabaseConfig.java` – Establishes a database connection for retrieving sensor data.
- `Monitoring.java` – Core class responsible for:
  - Checking sensor activity status.
  - Processing signals and sensor data.
  - Sending email notifications when a status change is detected.
- `Sensor.java` – Defines the sensor object with attributes such as ID, status, last timestamp, and associated email addresses.

## 📊 How It Works
### 🛠 Data Flow & Processing
1. **Configuration Loading:**
   - The application reads settings (e.g., database credentials, check intervals) from a properties file.
2. **Database Interaction:**
   - Fetches the **latest recorded timestamp** of each sensor to determine its status.
   - Retrieves the **email addresses** associated with each sensor.
3. **Sensor Status Check:**
   - Compares the last recorded signal timestamp against a predefined threshold to determine if the sensor is **online** or **offline**.
4. **Automated Email Notifications:**
   - If a sensor's status changes (e.g., from **online** to **offline**), an email alert is sent to the associated contacts.

## 🔍 Key Functionalities
- **Real-Time Monitoring:**
  - Uses a **concurrent thread-based system** to continuously check sensor status at a defined interval.
- **Configurable Thresholds:**
  - Each sensor has a customizable interval for determining inactivity.
- **Efficient Queue Processing:**
  - Uses **blocking queues** to handle signal updates and email notifications asynchronously.
- **Robust Logging & Error Handling:**
  - Logs every action using `Log4j`, ensuring visibility into system behavior.

## 🚀 Implementation Details
### **Configuration (Config.java)**
Handles retrieving settings from `config.properties`:
```java
public static int getCheckInterval() {
    return Integer.parseInt(properties.getProperty("checkInterval", "5000"));
}
```

### **Database Connection (DatabaseConfig.java)**
Creates a connection to the database:
```java
public static Connection getConnection() throws SQLException {
    return DriverManager.getConnection(Config.getDatabaseUrl(), Config.getDatabaseUser(), Config.getDatabasePassword());
}
```

### **Sensor Monitoring & Processing (Monitoring.java)**
Loads sensor data, checks status, and sends notifications:
```java
private void updateSensorStatus(int sensorId, String newStatus) {
    Sensor sensor = sensors.get(sensorId);
    if (!newStatus.equals(sensor.getStatus())) {
        sensor.setStatus(newStatus);
        emailQueue.put(sensorId); // Triggers email notification
    }
}
```

### **Email Notification System**
Emails are sent when a sensor changes state:
```java
private void sendEmail(int sensorId) {
    Sensor sensor = sensors.get(sensorId);
    for (String email : sensor.getEmails()) {
        logger.info("Sending email to: " + email + " - Sensor ID " + sensorId + " is " + sensor.getStatus());
    }
}
```

## 📈 System Workflow
1️⃣ **Sensors send periodic signals to the system.**

2️⃣ **The application retrieves the latest timestamps from the database.**

3️⃣ **Each sensor's last signal is checked against its threshold interval.**

4️⃣ **If the sensor is inactive beyond its allowed threshold, it is marked as offline.**

5️⃣ **An email notification is triggered for any status changes.**

6️⃣ **The system continuously checks for updates at regular intervals.**

## 🎯 Key Takeaways
✅ **Automated real-time monitoring of sensors.**

✅ **Efficient email alert system for status changes.**

✅ **Thread-safe design using concurrent data structures.**

✅ **Database-driven approach for configurable thresholds.**

This project provides a scalable and efficient solution for **monitoring sensors, detecting faults, and notifying responsible personnel in real-time**. 🚀

