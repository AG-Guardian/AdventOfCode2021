from numpy import prod


class Packet:
    def __init__(self, bits: str):
        self.version = int(bits[0:3], 2)
        self.type_id = int(bits[3:6], 2)
        self.length = 0
        self.val = 0
        self.children = []

        bits = self.reduce_bits(bits, 6)

        # literal val
        if self.type_id == 4:
            val = ''
            while bits[0] == '1':
                val += bits[1:5]
                bits = bits[5:]
                self.length += 5
            if bits[0] == '0':
                val += bits[1:5]
                self.length += 5
            self.val = int(val, 2)

        # operator
        else:
            length_type = bits[0]
            bits = self.reduce_bits(bits, 1)

            if length_type == '0':
                children_length = int(bits[:15], 2)
                bits = self.reduce_bits(bits, 15)
                self.length += children_length

                inner_bits = bits[:children_length]
                while '1' in inner_bits or len(inner_bits) >= 11:
                    self.children.append(Packet(inner_bits))
                    inner_bits = inner_bits[self.children[-1].length:]
            else:
                num_children = int(bits[:11], 2)
                bits = self.reduce_bits(bits, 11)

                for packet in range(num_children):
                    self.children.append(Packet(bits))
                    bits = self.reduce_bits(bits, self.children[-1].length)

            child_vals = [child.val for child in self.children]

            # sum operator
            if self.type_id == 0:
                self.val = sum(child_vals)
            # product operator
            elif self.type_id == 1:
                self.val = prod(child_vals)
            # min operator
            elif self.type_id == 2:
                self.val = min(child_vals)
            # max operator
            elif self.type_id == 3:
                self.val = max(child_vals)
            # greater than operator
            elif self.type_id == 5:
                self.val = 1 if child_vals[0] > child_vals[1] else 0
            # less than operator
            elif self.type_id == 6:
                self.val = 1 if child_vals[0] < child_vals[1] else 0
            # equal to operator
            elif self.type_id == 7:
                self.val = 1 if child_vals[0] == child_vals[1] else 0

    def reduce_bits(self, bits: str, num: int) -> str:
        self.length += num
        return bits[num:]

    def get_version_sum(self):
        total = self.version
        for child in self.children:
            total += child.get_version_sum()
        return total


with open('in.txt', 'r') as file:
    hext_message = file.read()

h_size = len(hext_message) * 4
bits = bin(int(hext_message, 16))[2:].zfill(h_size)
packet = Packet(bits)

print(packet.val)
