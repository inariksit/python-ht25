class Crochet:
    def __init__(self):
        self.links = []
        self.prev_row = []
        self.curr_row = []
        self.stitch_count = 0


    def chain(self):
        # Creates a new stitch, unconnected to any stitch.
        # Note that chain in the middle of a row is possible!
        self.stitch_count += 1
        self.curr_row.append(self.stitch_count)


    def single(self):
        # Creates a new stitch and links it to a single stitch on the previous row.
        # If the previous row doesn’t contain enough stitches, raises a ValueError exception.

        if len(self.prev_row) < 1:
            # We can do this even if we have no idea how we would get things to prev_row in the first place!
            raise ValueError("Not enough stitches!")
            # If you don't remember syntax for raising errors, this would be 100% fine
            ### print("Not enough stitches!")
            ### return

        else:
            self.stitch_count += 1
            self.curr_row.append(self.stitch_count)

            # We stopped here—how to get the right stitch from prev row?
            link = ("?????", self.stitch_count)
            self.links.append(link)

    def inc(self):
        # Creates two new stitches and links them to a single stitch on the previous row.
        # If the previous row doesn't contain enough stitches, raises a ValueError exception.
        pass

    def dec(self):
        # Creates a new stitch and links it to two stitches on the previous row.
        # If the previous row doesn't contain enough stitches, raises a ValueError exception.
        pass

    def next_row(self):
        # Starts a new row.
        # The old current row becomes the previous row.
        pass


    def print_links(self):
        # Prints a list of all the cross-links created so far.
        pass