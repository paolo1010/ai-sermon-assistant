# AI Sermon Assistant MVP

This is a simple AI-powered sermon assistant that:
- Generates structured sermon outlines based on topics.
- Finds relevant Bible verses related to sermon themes.

## 📌 Features
- FastAPI backend for AI sermon generation.
- React frontend for user interaction.
- OpenAI API integration for generating sermon outlines.
- Bible API integration for fetching related Bible verses.

## 🚀 Setup Instructions

### 1️⃣ Backend Setup
1. Install Python dependencies:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```
2. Create a `.env` file in `backend/` and add:
   ```bash
   OPENAI_API_KEY=your_openai_api_key_here
   ```
3. Run the FastAPI backend:
   ```bash
   uvicorn main:app --reload
   ```
4. Test the API at: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

### 2️⃣ Frontend Setup
1. Install dependencies:
   ```bash
   cd frontend
   npm install
   ```
2. Start the React app:
   ```bash
   npm start
   ```

### 3️⃣ Deploy to Railway
1. Push your code to GitHub:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/yourusername/ai-sermon-assistant.git
   git push -u origin main
   ```
2. Go to [Railway](https://railway.app) and create a new project.
3. Connect your GitHub repo and deploy the backend.
4. Add the `OPENAI_API_KEY` environment variable in Railway.
5. Update `App.js` in the frontend with your deployed backend URL.
6. Deploy the frontend using **Vercel** or **Netlify**.

### 📌 Next Steps
- Improve UI with a professional design.
- Add user authentication for pastors.
- Expand to a full sermon-building tool.

---

👨‍💻 Developed for churches to help pastors create impactful sermons faster.
