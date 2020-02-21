class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"
    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"
    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    def sort(self):
        """
        Sort the robot's list.
        """
        # Let's start by doing some base cases
        # we can always do a bubble sort here because the robot can hold one item in hand and look at the next item and swap if it is smaller or larger
        while True:
            # while all the functions that we are going to be using return true, we will define
            # the base cases of when to break the loop
            while True:

                if self.can_move_right() == False:
                    break

                # but if it true that it can move right, we will compare the items and make the swap:
                self.swap_item()    # after swapping the item, we move to the right:

                self.move_right()   # since we set can_move_right()==False in the beginning, it will automatically break
                                    # if cannot move right. But if it is True, which is what we intended in the beginning, it will move_right()

                # then, we make the comparison between the item being held and the next item.
                # so the compare_item function takes care of it for us where if the item held is less than the
                # next item in the list, we get a return of -1 and if we compare that with 0, we see that the item
                # being held is larger than the one on the right so we make the swap

                if self.compare_item() < 0:
                    self.swap_item()

                # what's next?
                # after swapping the item, we get to the end of the list:
                # when we get to the end of the list, we need to swap the last item:

                if self.can_move_right() == False:      # when we are at the end of the list, can_move_right returns False
                    self.swap_item()                    # swap the last item as it belong in the last of the list and move on
                    break

            # then, we go to the outer loop of being while True and see what to do when it is false
            # let's say we are at the end of the list and and we cannot move right, it would also break the loop

            if self.compare_item() == None and self.can_move_right()==False:
                break

            # last thing to implement is to make sure the smallest item is at the beginning of the list;

            while True:
                self.move_left()
                # swap the smallest item:
                if self.compare_item() == None:
                    self.swap_item()
                    break

                # and after that we keep swapping the smaller items:
                # if the value of item being held is greater than the next item, compare_item returns 1
                # so we make the swap continuously to get to the list in order

                if self.compare_item() > 0:
                    self.swap_item()

            # if we cannot move right any further, that means we are already at the end so we break the loop and we are done!
            if self.move_right() == False:
                    break




if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)
