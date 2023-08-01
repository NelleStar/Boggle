from boggle import Boggle
from flask import Flask, render_template, request, jsonify, session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECRETKEY'
boggle_game = Boggle()

# Flask decorator for / url
@app.route('/')
def index():
    """Render the main game page with the Boggle board."""
    board = boggle_game.make_board()
    session['board'] = board
    return render_template('game.html', board=board)

@app.route('/check-word')
def check_word():
    """Receive word submissions and check if they are valid."""
    
    word = request.args['word']
    board = session['board']

    if not word:
        return jsonify(error="Invalid request."), 400
    
    print("Received word:", word)
    print("Board:", board)


    # # Check if the word is a valid word on the board
    valid_word_result = boggle_game.check_valid_word(board, word)

    # # Calculate points for the word (1 point per letter in the word)
    points = len(word)

    

    return jsonify({'result': {'valid_word_result': valid_word_result, 'points': points}})
    # return jsonify({'result': valid_word_result})


if __name__ == '__main__':
    app.run(debug=True)
