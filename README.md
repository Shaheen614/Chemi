# Chemical Equipment Parameter Visualizer (Hybrid Web + Desktop App)

## 📌 Description
A hybrid application that runs both as a **Web App (React.js + Chart.js)** and a **Desktop App (PyQt5 + Matplotlib)**, powered by a **Django REST API**.  
It allows users to upload CSV files of chemical equipment parameters, view summary statistics, visualize data with charts, manage upload history, and generate PDF reports.  
Authentication ensures secure access to the API.

---

## 🚀 Features
- CSV Upload (Web + Desktop)
- Data Summary API (count, averages, type distribution)
- Interactive Charts (Chart.js + Matplotlib)
- History of last 5 uploads
- PDF Report Generation
- Basic Authentication
- SQLite database for persistence

---

## 🛠️ Tech Stack
- **Backend:** Django + DRF + Pandas + SQLite
- **Web Frontend:** React.js + Chart.js
- **Desktop Frontend:** PyQt5 + Matplotlib
- **Version Control:** Git + GitHub

---

## ⚙️ Setup Instructions

### Backend
```bash
cd backend
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
