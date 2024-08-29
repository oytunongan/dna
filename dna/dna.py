import csv
import sys


def main():
    str_list = []
    dna = []
    longest_return = []

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")

    # TODO: Read database file into a variable
    with open(sys.argv[1]) as fl:
        subsequence = csv.reader(fl)
        for row in subsequence:
            str_list.append(row)

    # TODO: Read DNA sequence file into a variable
    with open(sys.argv[2]) as fs:
        sequence = csv.reader(fs)
        for c in sequence:
            dna.append(c)

    # TODO: Find longest match of each STR in DNA sequence

    del str_list[1:]
    str_list[0].remove("name")

    for i in range(len(str_list[0])):
        longest_return.append(longest_match(dna[0][0], str_list[0][i]))

    # TODO: Check database for matching profiles
    with open(sys.argv[1]) as fd:
        database = csv.DictReader(fd)
        for line in database:
            count = 0
            for j in range(len(str_list[0])):
                if int(line[str_list[0][j]]) == longest_return[j]:
                    count += 1
            if count == len(longest_return):
                print(line["name"])
                break
        if count != len(longest_return):
            print("No match")
    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):
        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:
            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
