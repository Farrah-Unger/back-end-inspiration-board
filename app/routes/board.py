from flask import Blueprint, request, jsonify, make_response, abort
from app import db
from app.routes.routes_helper import validate_model, validate_input_data, error_message
from app.models.board import Board
from app.models.card import Card

boards_bp = Blueprint('boards_bp', __name__, url_prefix = '/boards')

# read one board - "/boards/id" (GET)
@boards_bp.route("/<id>", methods=["GET"])
def read_one_board(id):
    board = validate_model(Board, id)

    return jsonify({"board": board.to_dict()}), 200
     
    
# read all boards - "/boards" (GET)
@boards_bp.route("", methods=["GET"])
def read_all_boards():
    boards = Board.query.all()
    boards_response = [board.to_dict() for board in boards]

    return jsonify(boards_response)


# read all cards by board id - "/boards/id/cards"
@boards_bp.route("/<id>/cards", methods=["GET"])
def get_cards_by_board_id(id):
    board = validate_model(Board, id)
    if not board:
        return make_response({"details": "Id not found"}, 404)

    cards = [Card.to_dict(card) for card in Board.cards]

    return make_response({"id": Board.id, "title": board.title, "cards": cards})

<<<<<<< HEAD

# create one card under board id - "/boards/id/cards"
=======
# create one card under board id
>>>>>>> 8b0f3debfb7bb259fe3356e7d97d02ada94afff4
@boards_bp.route("/<id>/cards", methods=["POST"])
def create_card(id):
    request_body = request.get_json()
    if "message" not in request_body:
        error_message("Message not found", 400) # we need a helper function here

    request_body["board_id"] = id 
    card = Card.from_dict(request_body) # we need a helper function here
    
    db.session.add(card)
    db.session.commit()
    

# create a board (POST) - "/boards"
@boards_bp.route("", methods=["POST"])
def create_board():
    request_body = request.get_json()

    new_board = validate_input_data(Board, request_body)

    db.session.add(new_board)
    db.session.commit()

    return jsonify({"board": new_board.to_dict()}), 201


# update a board (PUT) - "/boards/id"
@boards_bp.route("/<id>", methods=["PUT"])
def update_board(id):
    board = validate_model(board, id)
    request_body = request.get_json()

    board.update(request_body)
    db.session.commit()
    
    response = {"board": board.to_dict()}
    return response


# delete a board - "/boards/id"
@boards_bp.route("/<id>", methods=["DELETE"])
def delete_board(id):
    board = validate_model(board, id)
    title = str(board.title)
    db.session.delete(board)
    db.session.commit()

    return(make_response({"details": f"board {id} \"{title}\" successfully deleted"}), 200)

