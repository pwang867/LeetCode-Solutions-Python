# Akuna Capital
class Bowling:
    def __init__(self):
        self.total = 0
        self.total_frames = 0
        self.pre_frame_state = 0   # 0 means regular, 1 strike, 2 sparse
        self.cur_frame_first = -1  # val of the first throw in current frame
        self.scores = []           # scores for all frames

    def on_ball_rolled(self, number_pinned_down):
        self.total += number_pinned_down
        if self.cur_frame_first == -1:  # the first ball
            self.cur_frame_first = number_pinned_down
            self.total_frames += 1
            self.scores.append(number_pinned_down)
            if self.pre_frame_state == 1 or self.pre_frame_state == 2:
                self.total += number_pinned_down
            if number_pinned_down == 10:
                self.pre_frame_state = 1
                self.cur_frame_first = -1
                return (10, self.total)
            else:
                return (self.cur_frame_first, self.total)
        else:
            cur = self.cur_frame_first + number_pinned_down
            self.scores[-1] = cur
            if self.pre_frame_state == 1:
                self.total += number_pinned_down
            if cur == 10:
                self.pre_frame_state = 2
            else:
                self.pre_frame_state = 0
            self.cur_frame_first = -1
            return (cur, self.total)

    def score(self, frame_idx):
        return (self.scores[frame_idx], self.total)


if __name__ == "__main__":
    ball = Bowling()
    for i, num in enumerate([3, 3, 1, 0, 10, 7, 3, 5, 2]):
        print(ball.on_ball_rolled(num))
    print(ball.scores)
