from whitebearbake_heroku import create_app

app = create_app()

def run(app=app):
    app.run(host='0.0.0.0', port=5002)

# Run entrypoint
if __name__ == '__main__':
    run()