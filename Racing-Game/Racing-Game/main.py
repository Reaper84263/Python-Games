import random
import check_input
from car import Car
from motorcycle import Motorcycle
from truck import Truck

LANES = 3
TRACK_LEN = 100
FINISH = TRACK_LEN - 1

def make_track():
    return [["-"] * TRACK_LEN for _ in range(LANES)]

def place_obstacles(track, per_lane=2):
    for lane in range(LANES):
        count = 0
        while count < per_lane:
            pos = random.randint(1, FINISH - 1)
            if track[lane][pos] == "-":
                track[lane][pos] = "0"
                count += 1

def next_obstacle(lane, start):
    try:
        return lane.index("0", start + 1)
    except ValueError:
        return None

def draw(track):
    for lane in track:
        print("".join(lane))

def move_marker(track, lane_idx, old, new, label):
    lane = track[lane_idx]
    if 0 <= old < TRACK_LEN and lane[old] != "0":
        lane[old] = "*"
    if 0 <= new < TRACK_LEN:
        lane[new] = label

def in_play(pos):
    return pos < FINISH

def describe():
    print("Rad Racer!")
    print("1. Lightning Car (Speed 7) – Nitro")
    print("2. Swift Bike (Speed 8) – Wheelie (chance to wipe out)")
    print("3. Behemoth Truck (Speed 6) – Ram (smashes obstacles)")

def main():
    track = make_track()
    place_obstacles(track)
    racers = [Car(), Motorcycle(), Truck()]
    describe()

    choice = check_input.get_int_range("Choose your vehicle (1-3): ", 1, 3)
    player_idx = choice - 1

    for i, r in enumerate(racers):
        r.initial = "P" if i == player_idx else r.initial
        track[i][0] = r.initial

    finished = []
    while len(finished) < 3:
        for r in racers:
            print(r)
        draw(track)

        p = racers[player_idx]
        if in_play(p.position):
            act = check_input.get_int_range("Choose action (1. Fast, 2. Slow, 3. Special): ", 1, 3)
            lane_idx = player_idx
            lane = track[lane_idx]
            old = p.position
            obs = next_obstacle(lane, old)
            if act == 1:
                msg = p.fast(obs, finish=FINISH)
            elif act == 2:
                msg = p.slow(obs, finish=FINISH)
            else:
                msg = p.special_move(obs, finish=FINISH)
            print(msg)
            move_marker(track, lane_idx, old, p.position, p.initial)
            if p.position >= FINISH and p not in finished:
                finished.append(p)

        for i, r in enumerate(racers):
            if i == player_idx or r in finished or not in_play(r.position):
                continue
            lane = track[i]
            old = r.position
            obs = next_obstacle(lane, old)
            roll = random.randint(1, 100)
            if r.energy == 0:
                act = 2
            elif roll <= 40:
                act = 2
            elif roll <= 70:
                act = 1
            else:
                act = 3
            if act == 1:
                msg = r.fast(obs, finish=FINISH)
            elif act == 2:
                msg = r.slow(obs, finish=FINISH)
            else:
                msg = r.special_move(obs, finish=FINISH)
            print(msg)
            move_marker(track, i, old, r.position, r.initial)
            if r.position >= FINISH and r not in finished:
                finished.append(r)

    draw(track)
    places = ["1st", "2nd", "3rd"]
    for i, r in enumerate(finished, 1):
        print(f"{places[i-1]} place: {r}")

if __name__ == "__main__":
    main()

