from dotenv import load_dotenv
load_dotenv(".flaskenv")

if __name__ == "__main__":
    from src.app import app
    app.run(host="0.0.0.0", port=5000)
