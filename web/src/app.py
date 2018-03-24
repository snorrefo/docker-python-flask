import time


from flask import Flask

import test


app = Flask(__name__)


@app.route('/')
def hello():
    # count = get_hit_count()
    count = 222311111134
    return 'Hello World! I have been seen {} times.\n'.format(test.hello())

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
