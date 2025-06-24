🔥 TDEE Calculator Web App

This is a lightweight, responsive web application that calculates your Total Daily Energy Expenditure (TDEE) based on user inputs like age, gender, height, weight, and activity level.

Built with HTML + Flask (Python)
Deployed on Google Cloud Platform using Cloud Functions and Cloud Storage 
No login required, open to all

---

 🔗 Live App

👉 [Click to Open the TDEE Calculator](https://storage.googleapis.com/smrithi-tdee-bucket/index.html)

---

🖼️ UI Preview

![Screenshot (317)](https://github.com/user-attachments/assets/74e338a4-c558-4008-b11e-0afc63733c26)




---

## ⚙️ How It Works

1. User fills the form with age, gender, weight, height, and activity level.
2. The form sends data as a JSON POST request to a Google Cloud Function.
3. The Cloud Function calculates TDEE using the Mifflin-St Jeor Equation.
4. Result is displayed instantly on the page.

---

## ☁️ Google Cloud Services Used

| GCP Service                 | Purpose                                                                 |
|----------------------------|-------------------------------------------------------------------------|
| Cloud Shell                | Used to write, test, and manage code directly from browser              |
| Cloud Storage (GCS)        | Hosts the static frontend (`index.html`) for public access              |
| Cloud Functions (Gen 2)    | Backend logic for TDEE calculation via HTTP POST                        |
| IAM Roles                  | Configured to allow public access to the function and storage bucket    |
| Cloud Build                | Automatically builds and deploys the backend function                   |
| Artifact Registry          | Stores build artifacts used by Cloud Functions                          |

---

## 🧰 Tech Stack

| Layer       | Technology                         |
|-------------|-------------------------------------|
| Frontend    | HTML5, CSS3                         |
| Backend     | Python 3.10, Flask                  |
| Hosting     | Google Cloud Storage (Static Site) |
| API Hosting | Google Cloud Functions (Gen 2)     |

---

📁 Project Structure
tdee-calculator/
│
├── frontend/
│ └── index.html # Frontend web page
│
├── backend/
│ ├── main.py # Cloud Function code
│ └── requirements.txt # Python dependencies
│
└── README.md









