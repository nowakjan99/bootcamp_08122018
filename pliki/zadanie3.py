import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-i", "--input", help="input file",
                    action="store")
parser.add_argument("-o", "--output", help="output file",
                    action="store")

args = parser.parse_args()

cleaned_emails = set()

with open(args.input) as f:
    for line in f:
        line = line.strip().lower()
        if line.count("@") == 1:
            cleaned_emails.add(line)

with open(args.output, 'w') as f:
    for email in cleaned_emails:
        f.write(email + "\n")

print(args.output)

