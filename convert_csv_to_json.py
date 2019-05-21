import pandas as pd
import sys

"""
Example of input file:
id, msg
1, Hello world
2, Hi
3, How are u doing?

Output file: 
[{"id":1," msg":" Hello world"},{"id":2," msg":" Hi"},{"id":3," msg":" How are u doing?"}]
"""

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3.x " + sys.argv[0] + " input-file.csv output-file.json")
        sys.exit()

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Read csv file with header
    df = pd.read_csv(input_file)
    df.to_json(output_file, orient="records")
