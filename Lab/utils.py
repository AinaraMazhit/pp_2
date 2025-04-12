import json

def save_game(snake, score, level, filename='save.json'):
    data = {
        "snake": snake.body,
        "direction": list(snake.direction),
        "score": score,
        "level": level
    }
    with open(filename, 'w') as f:
        json.dump(data, f)

def load_game(snake, filename='save.json'):
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
        snake.body = [tuple(pos) for pos in data['snake']]
        snake.direction = tuple(data['direction'])
        return data['score'], data['level']
    except Exception as e:
        print("Failed to load game:", e)
        return 0, 1
