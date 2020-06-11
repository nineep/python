

@app.errorhandler(werkzeug.exceptions.BadRequest)
def handle_bad_request(e):
    return 'bad request!', 400

class InsufficientStorage(werkzeug.exceptions.HTTPException):
    code = 507
    description = 'Not enough storage space'

if __name__ == '__main__':
    app = create_app(config='config.yaml')
    use_debugger = app.debug and not(app.config.get('DEBUG_WITH_APTANA'))
    app.run(use_debugger=use_debugger, debug=app.debug,
            use_reloader=use_debugger, host='0.0.0.0')
    