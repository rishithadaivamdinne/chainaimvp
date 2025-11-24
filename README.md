Chain AI MVP – FastAPI & Streamlit Supply Chain Recommendation
This project demonstrates an end-to-end MVP for automated supply chain recommendations. Users upload a sales CSV, and the agent calculates a forecast and recommended order using a simple moving average.​

Features
Backend: FastAPI API endpoint /recommend accepts CSV uploads and returns predictions.

Frontend: Streamlit web app for easy CSV upload and recommendation display.

Modular Python Agent: Handles moving average forecasting and logic, easily extendable.

Local Development: Both frontend and backend run locally for quick iteration.

Setup
1. Clone the repo
bash
git clone https://github.com/<yourusername>/chainaimvp.git
cd chainaimvp
2. Create and activate a virtual environment
bash
python -m venv venv
venv\Scripts\activate  # On Windows
3. Install required packages
bash
pip install fastapi uvicorn pandas streamlit requests python-multipart
Running the Project
1. Start the backend API
bash
venv\Scripts\python.exe -m uvicorn backend.main:app --reload
Visit http://127.0.0.1:8000/docs to test API endpoints.

2. Start the Streamlit frontend
Open a new terminal and run:

bash
streamlit run frontend/app.py
Visit the address shown (usually http://localhost:8501) to upload CSV and view recommendations.

File Structure
text
chainaimvp/
│
├── agent/
│   └── basicagent.py
├── backend/
│   └── main.py
├── frontend/
│   └── app.py
├── sales.csv
├── .gitignore
├── README.md
└── venv/
Example Usage
Upload a sample sales CSV through the Streamlit UI.

Click "Get Recommendation" to see the forecast and recommended reorder quantity.
