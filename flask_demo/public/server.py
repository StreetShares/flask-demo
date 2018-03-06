"""Application with public routes."""

from flask_demo.util.factories import create_app


public = create_app()


@public.route('/ping')
def ping():
    return "pong"


if __name__ == '__main__':
    public.run(debug=True, port=public.config['PUBLIC_PORT'])
