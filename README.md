# AI Wiki Quiz Generator

A full-stack application that transforms Wikipedia articles into engaging, educational quizzes using AI (Gemini via LangChain).

## Features

- **Wikipedia Scraping**: Automatically extracts and cleans content from Wikipedia articles
- **AI-Powered Quiz Generation**: Uses Google Gemini AI to generate 5-10 questions with varying difficulty levels
- **Structured Output**: Includes questions, answers, explanations, key entities, and related topics
- **Quiz History**: View and access all previously generated quizzes
- **Modern UI**: Clean, responsive interface built with React and Tailwind CSS

## Project Structure

```
wiki-quiz/
├── backend/
│   ├── database.py                 # SQLAlchemy setup and Quiz model
│   ├── models.py                   # Pydantic schemas for LLM output
│   ├── scraper.py                  # Wikipedia scraping functions
│   ├── llm_quiz_generator.py       # LangChain setup and quiz generation
│   ├── main.py                     # FastAPI application and endpoints
│   ├── requirements.txt            # Python dependencies
│   └── .env                        # Environment variables (create this)
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── QuizDisplay.jsx     # Reusable quiz display component
│   │   │   └── Modal.jsx           # Modal component
│   │   ├── services/
│   │   │   └── api.js              # API service functions
│   │   ├── tabs/
│   │   │   ├── GenerateQuizTab.jsx # Quiz generation tab
│   │   │   └── HistoryTab.jsx      # History tab
│   │   ├── App.jsx                 # Main React component
│   │   └── index.css               # Tailwind CSS directives
│   └── package.json
│
└── README.md
```

## Setup Instructions

### Backend Setup

1. **Navigate to backend directory:**
   ```bash
   cd backend
   ```

2. **Create virtual environment:**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # Linux/Mac
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   Create a `.env` file in the `backend` directory:
   ```env
   GEMINI_API_KEY=your_gemini_api_key_here
   DATABASE_URL=postgresql://postgres:postgres@localhost:5432/wiki_quiz
   ```
   
   **For MySQL:**
   ```env
   DATABASE_URL=mysql+pymysql://user:password@localhost:3306/wiki_quiz
   ```
   
   **For SQLite (development only):**
   ```env
   DATABASE_URL=sqlite:///./quiz_history.db
   ```
   And update `database.py` to use SQLite instead of PostgreSQL.

5. **Set up database:**
   - **PostgreSQL**: Create a database named `wiki_quiz`
     ```sql
     CREATE DATABASE wiki_quiz;
     ```
   - **MySQL**: Create a database named `wiki_quiz`
     ```sql
     CREATE DATABASE wiki_quiz;
     ```

6. **Run the backend server:**
   ```bash
   uvicorn main:app --reload --port 8000
   ```

   The API will be available at `http://localhost:8000`
   - API docs: `http://localhost:8000/docs`
   - Alternative docs: `http://localhost:8000/redoc`

### Frontend Setup

1. **Navigate to frontend directory:**
   ```bash
   cd frontend
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Run the development server:**
   ```bash
   npm run dev
   ```

   The frontend will be available at `http://localhost:5173` (or another port if 5173 is busy)

## API Endpoints

### 1. Generate Quiz
- **Endpoint**: `POST /generate_quiz`
- **Request Body**:
  ```json
  {
    "url": "https://en.wikipedia.org/wiki/Alan_Turing"
  }
  ```
- **Response**: Complete quiz data including questions, answers, explanations, key entities, and related topics

### 2. Get History
- **Endpoint**: `GET /history`
- **Response**: List of all previously generated quizzes with id, url, title, and date_generated

### 3. Get Quiz by ID
- **Endpoint**: `GET /quiz/{quiz_id}`
- **Response**: Complete quiz data for the specified quiz ID

## Usage

1. **Start the backend server** (from `backend` directory):
   ```bash
   uvicorn main:app --reload
   ```

2. **Start the frontend server** (from `frontend` directory):
   ```bash
   npm run dev
   ```

3. **Open your browser** and navigate to the frontend URL (usually `http://localhost:5173`)

4. **Generate a Quiz**:
   - Go to the "Generate Quiz" tab
   - Enter a Wikipedia URL (e.g., `https://en.wikipedia.org/wiki/Alan_Turing`)
   - Click "Generate Quiz"
   - Wait for the AI to process and generate the quiz
   - View the generated quiz with questions, answers, and explanations

5. **View History**:
   - Go to the "History" tab
   - See all previously generated quizzes
   - Click "Details" on any quiz to view it in a modal

## Example Wikipedia URLs to Test

- `https://en.wikipedia.org/wiki/Alan_Turing`
- `https://en.wikipedia.org/wiki/Quantum_computing`
- `https://en.wikipedia.org/wiki/Artificial_intelligence`
- `https://en.wikipedia.org/wiki/Photosynthesis`
- `https://en.wikipedia.org/wiki/World_War_II`

## LangChain Prompt Template

The quiz generation uses a detailed prompt template that instructs the LLM to:
- Generate 5-10 questions with varying difficulty levels
- Include exactly 4 options per question
- Provide accurate answers based on the article content
- Extract key entities (people, organizations, locations)
- Identify main sections
- Suggest related topics for further reading

The prompt is defined in `backend/llm_quiz_generator.py` and uses LangChain's `JsonOutputParser` to enforce the Pydantic schema structure.

## Database Schema

The `Quiz` model includes:
- `id`: Primary key
- `url`: Wikipedia article URL
- `title`: Article title
- `date_generated`: Timestamp
- `scraped_content`: Raw scraped HTML content (for bonus feature)
- `full_quiz_data`: JSON-serialized quiz data

## Error Handling

The application handles:
- Invalid Wikipedia URLs
- Network errors during scraping
- LLM API errors
- Database connection issues
- Missing or malformed data



## Technologies Used

### Backend
- **FastAPI**: High-performance web framework
- **SQLAlchemy**: ORM for database operations
- **BeautifulSoup4**: HTML parsing and scraping
- **LangChain**: LLM framework
- **Google Gemini AI**: Language model for quiz generation
- **Pydantic**: Data validation

### Frontend  
- **React**: UI library
- **Tailwind CSS**: Utility-first CSS framework
- **Vite**: Build tool and dev server

### Database
- **PostgreSQL** (or MySQL/SQLite)

### Screenshots

<img width="1910" height="969" alt="Screenshot 2026-05-01 104624" src="https://raw.githubusercontent.com/NikhithaMengani/AI-WIKI-QUIZ/main/assets/img1.png" />
<img width="1894" height="893" alt="Screenshot 2026-05-01 104650" src="https://raw.githubusercontent.com/NikhithaMengani/AI-WIKI-QUIZ/main/assets/img2.png" />
<img width="1886" height="888" alt="Screenshot 2026-05-01 104742" src="https://raw.githubusercontent.com/NikhithaMengani/AI-WIKI-QUIZ/main/assets/img3.png" />
<img width="1823" height="888" alt="Screenshot 2026-05-01 104755" src="https://raw.githubusercontent.com/NikhithaMengani/AI-WIKI-QUIZ/main/assets/img4.png" />
<img width="1288" height="877" alt="Screenshot 2026-05-01 104813" src="https://raw.githubusercontent.com/NikhithaMengani/AI-WIKI-QUIZ/main/assets/img5.png" />
<img width="1855" height="878" alt="Screenshot 2026-05-01 104822" src="https://raw.githubusercontent.com/NikhithaMengani/AI-WIKI-QUIZ/main/assets/img6.png" />
<img width="1875" height="878" alt="Screenshot 2026-05-01 105021" src="https://raw.githubusercontent.com/NikhithaMengani/AI-WIKI-QUIZ/main/assets/img7.png" />
<img width="1799" height="913" alt="Screenshot 2026-05-01 105040" src="https://raw.githubusercontent.com/NikhithaMengani/AI-WIKI-QUIZ/main/assets/img8.png" />




## Troubleshooting

### Backend Issues

1. **Database Connection Error**:
   - Ensure PostgreSQL/MySQL is running
   - Check `DATABASE_URL` in `.env` file
   - Verify database credentials

2. **Gemini API Error**:
   - Verify `GEMINI_API_KEY` is set in `.env`
   - Check API key is valid and has quota remaining

3. **Import Errors**:
   - Ensure virtual environment is activated
   - Reinstall dependencies: `pip install -r requirements.txt`

### Frontend Issues

1. **CORS Errors**:
   - Ensure backend is running on port 8000
   - Check CORS settings in `backend/main.py`

2. **API Connection Failed**:
   - Verify backend server is running
   - Check API URL in `frontend/src/services/api.js`

## Development Notes

- The LLM model used is `gemini-2.0-flash-exp` (can be changed in `llm_quiz_generator.py`)
- Text is limited to 8000 characters to avoid token limits
- Quiz questions are generated with 5-10 questions per article
- Difficulty levels: easy, medium, hard



