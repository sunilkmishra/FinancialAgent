# Financial Analyst Tool

## Description
A financial analysis tool that fetches stock data using Yahoo Finance API and provides a multi-agent interface for analysis. Built with the Agno framework and integrated with DuckDuckGo search capabilities.

## Prerequisites
- Python 3.11+
- Agno framework installed
- `yfinance`, `pandas`, and `fastapi` libraries

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/FinancialAnalyst.git
   cd FinancialAnalyst
   ```

2. Setup virtual environment (if not using provided FA/):
   ```bash
   python -m venv FA
   FA/Scripts/activate
   pip install -r requirements.txt  # (Create requirements.txt if missing)
   ```

3. Set environment variables:
   ```bash
   cp .env.template .env
   # Edit .env with your GROQ_API_KEY
   ```

## Usage
Start the analysis server:
```bash
FA/Scripts/python Playground.py
```
Access the interface at [http://localhost:7777](http://localhost:7777)


## Contributing
1. Fork the repository
2. Create feature branch: `git checkout -b feature/YourFeature`
3. Commit changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature/YourFeature`
5. Create new Pull Request
