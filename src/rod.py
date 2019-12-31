class Rod:
    def __init__(self, length, boost_begin, boost_count, ang_acc):
        self.length = length
        self.boost_begin = boost_begin
        self.boost_count = boost_count
        self.ang_acc = ang_acc
        self.ang_vel = 0
        self.ang_pos = 0
