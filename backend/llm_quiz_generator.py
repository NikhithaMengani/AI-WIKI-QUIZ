from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
import os
from dotenv import load_dotenv
import json
from pathlib import Path

# Load .env
env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path)

class QuizGenerator:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")

        print("API KEY LOADED:", api_key)

        if not api_key:
            raise ValueError("GEMINI_API_KEY not found")

        # ✅ FIXED MODEL (IMPORTANT)
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-1.5-flash-latest",
            google_api_key=api_key,
            temperature=0.7,
            convert_system_message_to_human=True
        )

        self.parser = JsonOutputParser()

        # ✅ FIXED PROMPT (VERY IMPORTANT)
        self.prompt_template = ChatPromptTemplate.from_messages([
            ("system", """You are an expert quiz generator.

STRICT RULES:
- ALWAYS generate at least 5 questions
- Each question MUST have:
  question, 4 options, correct answer, explanation
- NEVER return empty quiz
- Return ONLY valid JSON

OUTPUT FORMAT:
{
  "summary": "string",
  "key_entities": {
    "people": ["string"],
    "organizations": ["string"],
    "locations": ["string"]
  },
  "sections": ["string"],
  "quiz": [
    {
      "question": "string",
      "options": ["A", "B", "C", "D"],
      "answer": "string",
      "explanation": "string",
      "difficulty": "easy/medium/hard"
    }
  ],
  "related_topics": ["string"]
}
"""),

            ("human", """Article Title: {title}

Article Content:
{article_text}
""")
        ])

        self.chain = self.prompt_template | self.llm | self.parser

    def generate_quiz(self, article_text: str, title: str) -> dict:
        try:
            result = self.chain.invoke({
                "article_text": article_text,
                "title": title
            })

            # Convert string → JSON if needed
            if isinstance(result, str):
                result = json.loads(result)

            print("LLM OUTPUT:", result)  # 🔥 debug

            return result

        except Exception as e:
            print("ERROR:", str(e))
            return {"error": str(e)}