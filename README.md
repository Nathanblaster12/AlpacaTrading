# Decided to create an efficient gambling tool, was fed up of robinhood - too much green.
# Expected tech stack - ReactJS, MySql, Python, Fast API 

## Dependencies

- alpaca-trade-api: Python client for Alpaca's trade API
  ```bash
  pip install alpaca-trade-api
  ```
- python-dotenv: For loading environment variables
  ```bash
  pip install python-dotenv
  ```

## Environment Setup

1. Create a `.env` file in the backend directory by copying `.env.example`:
   ```bash
   cp backend/.env.example backend/.env
   ```
2. Add your Alpaca API credentials to the `.env` file:
   ```
   ALPACA_API_KEY=your_api_key_here
   ALPACA_SECRET_KEY=your_secret_key_here
   ```

⚠️ Never commit your actual API keys to the repository. The `.env` file is ignored by git for security reasons.
