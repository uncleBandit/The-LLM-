# 🧠 LLM Pawa — Your AI-Powered Question Assistant

LLM Pawa is a modern full-stack web app that enables users to input natural language questions and receive intelligent responses in real-time, powered by a Large Language Model (LLM) via the OpenRouter API.

Built with **FastAPI** and **Next.js**, this project demonstrates solid full-stack development skills, thoughtful UX/UI, and clean software architecture.

---

## 🚀 Live Demo  
[🔗 COMING SOON ]

---

## 🧩 Features

### ✅ Implemented
- 🔎 Input any natural language question
- 💬 Real-time streamed responses via OpenRouter API
- 🎨 Responsive, modern UI using TailwindCSS
- ⚡ Loading indicators and error handling
- 🧪 Clean API structure with Swagger docs (via FastAPI)

### 🔜 Coming Soon
- 🕓 Query history for session persistence
- ☁️ Cloud deployment (currently running locally)

---

## 🛠️ Tech Stack

### ⚙️ Backend (Python / FastAPI)
- FastAPI (async API framework)
- Uvicorn (ASGI server)
- Pydantic (input validation and type safety)
- `python-dotenv` for env config
- OpenRouter API integration for LLM responses

### 💻 Frontend (Next.js / React)
- Next.js 14 App Router (React server components)
- React with TypeScript
- TailwindCSS for styling
- Axios for client-server communication

---

## 📁 Project Structure

The-LLM-/
│
├── backend/ # FastAPI backend
│ ├── main.py # Entry point for FastAPI app
│ ├── api/ # API route handlers
│ ├── services/ # OpenRouter API logic
│ ├── models/ # Pydantic schemas
│ ├── utils/ # Helper functions
│ ├── .env.example # Environment variable template
│ └── requirements.txt
│
├── frontend/ # Next.js frontend
│ ├── app/ # App Router pages and layouts
│ ├── components/ # Reusable UI components
│ ├── utils/ # Axios and API logic
│ ├── styles/ # Tailwind config and globals
│ └── .env.local.example
│
└── README.md # You're reading it



---

## ⚙️ Getting Started

### Prerequisites
- Python 3.11+
- Node.js 18+
- Git

---

### 1. Clone the Repository

```bash
git clone https://github.com/uncleBandit/The-LLM-.git
cd The-LLM-
2. Backend Setup (FastAPI)
bash
Copy
Edit
cd backend
python -m venv .venv
# On macOS/Linux:
source .venv/bin/activate
# On Windows:
.venv\Scripts\activate

pip install -r requirements.txt
cp .env.example .env
Fill in the required .env variables (like your OpenRouter key).

Run the backend:

uvicorn main:app --reload
FastAPI docs available at:


http://localhost:8000/docs
3. Frontend Setup (Next.js)
t
cd ../frontend
npm install
cp .env.local.example .env.local
Fill in the frontend .env.local (such as backend API base URL).

Run the frontend:

npm run dev
Visit the app at:
http://localhost:3000
🧪 Prompt Engineering (Dev Notes)
The app sends user prompts directly to the OpenRouter LLM API with controlled system messages to format tone, ensure clarity, and simulate helpful assistant-like behavior.
Example prompt structure:

{
  "model": "openrouter/your-model",
  "messages": [
    { "role": "system", "content": "You are a helpful AI assistant." },
    { "role": "user", "content": "What is the capital of Kenya?" }
  ]
}
🔐 Environment Variables
Backend .env
ini
Copy
Edit
OPENROUTER_API_KEY=your_openrouter_key_here
Frontend .env.local
ini
Copy
Edit
NEXT_PUBLIC_API_BASE_URL=http://localhost:8000
💡 Future Improvements
Query history using localStorage or backend DB

Auth support (e.g., GitHub OAuth)
Better error UX and retry options
Deployment (e.g., Vercel + Render combo)

🧾 License
This project is open-source under the MIT License.

✍️ Author
Baba Nanii (uncleBandit)

GitHub: @uncleBandit

LinkedIn: [[Your LinkedIn Profile Here]](https://www.linkedin.com/in/peter-mwania-893375113/)



📬 Feedback or Questions?
Feel free to open an issue or fork the project and build your own assistant!
