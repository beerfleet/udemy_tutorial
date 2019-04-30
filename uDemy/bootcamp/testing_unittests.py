def eat(food, is_healthy):
    ending = "coz YOLO!"
    if is_healthy:
        ending = "coz my body needs healthy foods"
    return f"I am eating {food}, {ending}"

def nap(num_hours):
    if num_hours > 2:
        return f"Damnit I overslept"
    else:
        return f"Power nap is great"

