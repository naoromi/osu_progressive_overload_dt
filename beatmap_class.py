class Beatmap:
    def __init__(self, beatmap_name):
        self.beatmap_name = beatmap_name
        self.beatmap_length = 0.0
        self.beatmap_multiplier_length = 0.0

    def calculate_beatmap_multiplier_length(self, start_speed, end_speed, interval):
        while start_speed <= end_speed:
            self.beatmap_multiplier_length += self.beatmap_length / (start_speed)
            start_speed += interval
        return self.beatmap_multiplier_length
    
    
