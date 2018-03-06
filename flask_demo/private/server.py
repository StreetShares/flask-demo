"""Just playing around with some ideas."""

from flask import request

from flask_demo.util.factories import create_app


private = create_app()


@private.route('/')
def hello():
    a = 1
    b = 3
    private.logger.error('An error occurred')
    raise Exception()
    return "Hello"


@private.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username


@private.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


@private.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        print('Post')
    else:
        print('else')


if __name__ == '__main__':
    private.run(debug=True, port=private.config['PRIVATE_PORT'])
