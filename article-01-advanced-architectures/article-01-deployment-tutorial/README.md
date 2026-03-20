# Article 01 — Deploying Your First Multi-Agent System with MCP

Code for my Medium article: [Hands-On Tutorial: Deploying Your First Scalable Multi-Agent System](https://medium.com/@sivareddyevuri92/hands-on-tutorial-deploying-your-first-scalable-multi-agent-system-with-mcp-optimization-5c0beda9d372)

## Run Locally

```bash
pip install -r requirements.txt
cp .env.example .env        # add your OPENAI_API_KEY
python main.py
```

## Run as API

```bash
uvicorn deploy.app:app --reload
```
Open: http://localhost:8000/docs

## Docker

```bash
docker build -t market-analyst .
docker run -p 8000:8000 --env-file .env market-analyst
```

## Author
Manideep Reddy Eevuri
[LinkedIn](https://linkedin.com/in/manideep-reddy-eevuri-661659268) · [Medium](https://medium.com/@sivareddyevuri92) · [GitHub](https://github.com/Maniredii)
