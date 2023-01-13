from app.models.board import Board
from app.models.card import Card
import pytest

def test_get_all_board_with_no_records(client):
    response = client.get("/boards")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == []


def test_get_all_boards(client, all_boards):
    response = client.get("/boards")
    response_body = response.get_json()

    assert response.status_code == 200
    assert len(response_body) == 3
    assert response_body == [
        {"id": 1, "owner": "Jan", "title": "Test Board 1"},
        {"id": 2, "owner": "Farrah", "title": "Test Board 2"},
        {"id": 3, "owner": "Maria", "title": "Test Board 3"}]
    

def test_get_one_board(client, one_board):
    response = client.get("/boards/1")
    response_body = response.get_json()

    assert response.status_code == 200
    assert "board" in response_body
    assert response_body == {
        "board": {
            "id": 1,
            "title": "A New Board",
            "owner": "Andrea",
        }
    }


def test_get_board_not_found(client):
    response = client.get("/boards/1")
    response_body = response.get_json()

    assert response.status_code == 404
    assert response_body == {
        "message": "Board 1 not found"}

def test_create_board(client):
    response = client.post("/boards", json={
        "title": "A New Board",
        "owner": "Andrea",
    })
    response_body = response.get_json()

    assert response.status_code == 201
    assert "board" in response_body
    assert response_body == {
        "board": {
            "id": 1,
            "title": "A New Board",
            "owner": "Andrea",
        }
    }


def test_create_board_missing_title(client):
    response = client.post("/boards", json={})
    response_body = response.get_json()

    assert response.status_code == 400
    assert response_body == {
        "details": "Invalid data"
    }


