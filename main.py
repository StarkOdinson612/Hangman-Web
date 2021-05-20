from flask import Flask, render_template

def img_get(index):
    img_switch = {
        0 : "stage0.png",
        1 : "stage1.png",
        2 : "stage2.png",
        3 : "stage3.png",
        4 : "stage4.png",
        5 : "stage5.png",
        6 : "stage6.png",
        7 : "stage7.png",
    }

    return img_switch.get(index)

img_name = img_get(0)

def game_start():
    choice = input('Single Player (1) or Two Player (2)?\n')
    if not choice == 1 or choice == 2:
        return

app = Flask(__name__)
@app.route('/')
def run():
    return render_template("index.html")

@app.route('/multiplayer')
def multiplayer():
    return render_template("multiplayer.html")

if __name__ == "__main__":
    app.run()