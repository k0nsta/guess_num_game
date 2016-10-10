import config
from flask import Flask, request, render_template, flash
from forms import NumberForm
import random

server_num = None


def generate_num():
    global server_num
    server_num = random.randrange(0, 100)
    return server_num


class Storage(object):
    itmes = None
    _obj = None

    @classmethod
    def __new__(cls, *args, **kwargs):
        if cls._obj is None:
            cls._obj = object.__new__(cls)
            cls.items = []
        return cls._obj


app = Flask(__name__, template_folder='templates')
app.config.from_object(config)
app.before_first_request(generate_num)


@app.route('/', methods=['GET', 'POST'])
def guess_number():
    storage = Storage()
    all_usr_num = storage.items
    if request.method == 'POST':
        form = NumberForm(request.form)
        usr_num = form.data['number']
        if form.validate():
            if usr_num == server_num:
                flash('Wow, you have guessed right! I guess {}'.format(server_num))
                generate_num()
            elif usr_num > server_num:
                flash('Ooops, it seems you were wrong, your number greater than secret number', 'info')
                all_usr_num.append(usr_num)
            elif usr_num < server_num:
                flash('Ooops, it seems you were wrong, your number less than secret number', 'info')
                all_usr_num.append(usr_num)
    else:
        form = NumberForm()

    return render_template(
            'index.html',
            form=form,
            items=all_usr_num
        )

if __name__ == '__main__':
    app.run()

