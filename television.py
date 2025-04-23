
class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """
        Function to create instance variables for the Television class.
        These include status, muted, volume, and channel.
        """
        self.__status = False
        self.__muted = False
        self.__volume = self.MIN_VOLUME
        self.__channel = self.MIN_CHANNEL

    def power(self) -> None:
        """
        Function to turn on or off the television.
        This uses a conditional to turn on if the TV is off and turn off if the TV is on.
        :return: Nothing
        """
        if self.__status:
            self.__status = False
        else:
            self.__status = True

    def mute(self) -> None:
        """
        Function to mute the television.
        This mutes the TV if the TV is on by setting the muted variable and changing the volume to the minimum.
        :return: Nothing
        """
        if self.__status and not self.__muted:
            self.__muted = True
            self.__volume = self.MIN_VOLUME
        elif self.__status and self.__muted:
            self.__muted = False

    def channel_up(self) -> None:
        """
        Function to increase the channel of the television.
        This increases the channel if it is not the max channel, if it is the max then it changes to the minimum.
        :return: Nothing
        """
        if self.__status:
            if self.__channel == self.MAX_CHANNEL:
                self.__channel = self.MIN_CHANNEL
            else:
                self.__channel = self.__channel + 1

    def channel_down(self) -> None:
        """
        Function to decrease the channel of the television.
        This decreases the channel if it is not the min channel, if it is the min then it changes to the max.
        :return: Nothing
        """
        if self.__status:
            if self.__channel == self.MIN_CHANNEL:
                self.__channel = self.MAX_CHANNEL
            else:
                self.__channel = self.__channel - 1

    def volume_up(self) -> None:
        """
        Function to increase the volume of the television.
        This increases the volume if it is not the max volume, if it is the max then it does nothing.
        This also changes the muted and volume variable if it was previously muted, it will unmute and set to max volume.
        :return: Nothing
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.MAX_VOLUME
            if self.__volume != self.MAX_VOLUME:
                self.__volume = self.__volume + 1

    def volume_down(self) -> None:
        """
        Function to Decrease the volume of the television.
        This decreases the volume if it is not the min volume, if it is the min then it does nothing.
        This also changes the muted and volume variable if it was previously muted, it will unmute and set to max volume.
        :return: Nothing
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.MAX_VOLUME
            if self.__volume != self.MIN_VOLUME:
                self.__volume = self.__volume - 1

    def __str__(self) -> str:
        """
        Function to return a string comprised of important variables such as Power, Channel, and Volume.
        :return: String in the format "Power = [status], Channel = [channel], Volume = [volume]"
        """
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"