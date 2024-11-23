class Television:
    __MIN_VOLUME = 0
    __MAX_VOLUME = 2
    __MIN_CHANNEL = 0
    __MAX_CHANNEL = 3

    def __init__(self):
        self.status = False
        self.muted = False
        self.volume = Television.__MIN_VOLUME
        self.channel = Television.__MIN_CHANNEL

    def power(self):
        self.status = not self.status

    def mute(self):
        if self.status:
            self.muted = not self.muted


    def channel_up(self):
        if self.status:
            if self.channel == Television.__MAX_CHANNEL:
                self.channel = Television.__MIN_CHANNEL
            else:
                self.channel += 1

    def channel_down(self):
        if self.status:
            if self.channel == Television.__MIN_CHANNEL:
                self.channel = Television.__MAX_CHANNEL
            else:
                self.channel -= 1

    def volume_up(self):
        if self.status:
            if self.volume < Television.__MAX_VOLUME:
                self.volume += 1
        self.muted = False

    def volume_down(self):
        if self.status:
            if self.volume > Television.__MIN_VOLUME:
                self.volume -= 1
        self.muted = False

    def __str__(self):
        if self.muted:
            return f"Power = {self.status}, Channel = {self.channel}, Volume = {0}."
        return f"Power = {self.status}, Channel = {self.channel}, Volume = {self.volume}."