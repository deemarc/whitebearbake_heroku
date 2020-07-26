from whitebearbake_heroku import create_app
import os
port = int(os.environ.get('PORT', 5000))
app = create_app()

def run():
    app.run(host='0.0.0.0', port=port)

# Run entrypoint
if __name__ == '__main__':
    run()