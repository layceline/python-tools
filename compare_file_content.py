import sys
import filecmp

def read_file(filename):
    line_list = []
    with open(filename, 'r') as f:
        for line in f.read().splitlines():
            line_list.append(line)
    return line_list

def has_duplicates(list_to_check):
    return len(left_list) != len(set(left_list))
        

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3.x " + sys.argv[0] + " left-file right-file")
        sys.exit()

    left_file = sys.argv[1]
    right_file = sys.argv[2]

    left_list = read_file(left_file)
    right_list = read_file(right_file)
   
    if has_duplicates(left_list):
        print("Found duplicates in file: " + left_file)
    
    if has_duplicates(right_list):
        print("Found duplicates in file: " + right_file)

    left_set = set(left_list)
    right_set = set(right_list)

    left_more = left_set - right_set
    if left_more:
        print("Items found in", left_file, "but not in", right_file + ":", left_more)

    right_more = right_set - left_set
    print(right_more)