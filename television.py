#definition of class Television
class Television:
    #definition of class variables
    #minimum value of volume instance variable
    __MIN_VOLUME:int = 0
    #maximum value of volume instance variable
    __MAX_VOLUME:int = 2
    #minimum value of channel instance variable
    __MIN_CHANNEL:int = 0
    #maximum value of channel instance variable
    __MAX_CHANNEL:int = 3

    #initialization method definition
    def __init__(self):
        #status is a boolean, is the TV on or off
        self.status:bool = False
        #muted is a boolean, is the TV muted
        self.muted:bool = False
        #volume is an integer, how loud is the TV
        self.volume:int = Television.__MIN_VOLUME
        #channel is an integer, what channel is being shown on the TV
        self.channel:int = Television.__MIN_CHANNEL

    """
    definition of power method
    turn the TV on or off
    """
    def power(self):
        #reverse the value of status
        self.status = not self.status

    """
    definition of mute method
    mute and unmute the TV
    """
    def mute(self):
        #if the TV is on
        if self.status:
            #reverse the value of mute
            self.muted = not self.muted

    """
    definition of the channel_up method
    change the channel up and return to minimum if maximum
    """
    def channel_up(self):
        #if the TV is on
        if self.status:
            #if channel is equal to __MAX_CHANNEL
            if self.channel == Television.__MAX_CHANNEL:
                #set channel equal to __MIN_CHANNEL
                self.channel = Television.__MIN_CHANNEL
            else:
                #else add one to channel
                self.channel += 1
        #if the TV is off, do nothing

    """
    definition of channel_down method
    change the channel down and return to maximum if minimum
    """
    def channel_down(self):
        #if the TV is on
        if self.status:
            #if channel is equal to __MIN_CHANNEL
            if self.channel == Television.__MIN_CHANNEL:
                #set channel equal to __MAX_CHANNEL
                self.channel = Television.__MAX_CHANNEL
            else:
                #else subtract one from channel
                self.channel -= 1
        #if the tv is off, do nothing

    """
    definition of volume up method
    turn the volume up if not maximum
    """
    def volume_up(self):
        #if the TV is on
        if self.status:
            #if volume is less than __MAX_VOLUME
            if self.volume < Television.__MAX_VOLUME:
                #add one to volume
                self.volume += 1
            #set muted to false
            self.muted = False
        #if the TV is off, do nothing

    """
    definition of volume down method
    turn the volume down if not minimum
    """
    def volume_down(self):
        #if the TV is on
        if self.status:
            #if volume is greater than __MIN_VOLUME
            if self.volume > Television.__MIN_VOLUME:
                #subtract one from volume
                self.volume -= 1
            #set muted to false
            self.muted = False
        #if the TV is off, do nothing

    #override of __str__ method
    def __str__(self):
        #if muted is true
        if self.muted:
            #return a string containing all information about an instance of TV, use 0 instead of volume
            return f"Power = {self.status}, Channel = {self.channel}, Volume = {0}"
        #return a string containing all information about an instance of TV
        return f"Power = {self.status}, Channel = {self.channel}, Volume = {self.volume}"