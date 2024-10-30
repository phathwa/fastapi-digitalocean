# gunicorn.config.py

bind = "0.0.0.0:8000"  # or any port you want
workers = 4  # Adjust based on your server capabilities
worker_class = "uvicorn.workers.UvicornWorker"
