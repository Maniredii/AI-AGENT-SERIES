
# HTTP server that accepts agent queries via REST API

from flask import Flask, request, jsonify
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

def process_query(user_input, session_id):
    """Core agent logic - receives query, returns response."""
    response = llm.invoke(user_input)
    return {
        "session_id": session_id,
        "query": user_input,
        "response": response.content
    }

@app.route('/agent', methods=['POST'])
def handle_request():
    user_input = request.json['query']
    session_id = request.headers.get('X-Session-ID', 'default-session')
    result = process_query(user_input, session_id)
    return jsonify(result)

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok"})

if __name__ == '__main__':
    print("Agent server running at http://localhost:5000")
    print("Test: curl -X POST http://localhost:5000/agent \\")
    print('       -H "Content-Type: application/json" \\')
    print('       -d \'{"query": "What is an AI agent?"}\'')
    app.run(debug=True, port=5000)