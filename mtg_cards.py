import argparse

class Card():

    def __init__(self, amount, tag, magicSet, no):
        self.amount = amount
        self.tag = tag
        self.magicSet = magicSet
        self.no = no
        
    def show(self):
        print("Amount = {}, Tag ={}, Set={}, CardNo={}".format(self.amount, self.tag, self.magicSet, self.no))

def main():

    parser = argparse.ArgumentParser(description='Script to process an exported deck pasted into a .txt file')
    parser.add_argument('filename', help='Make sure the input file is in the same directory')
    args = parser.parse_args()

    lines = open(args.filename).read().splitlines()
    lines = lines[1:]

    for line in lines:
        data = line.split()
        card = Card(data[0], ' '.join(data[1:-2]), data[-2], data[-1])
        card.show()

if __name__ == '__main__':

    main()
