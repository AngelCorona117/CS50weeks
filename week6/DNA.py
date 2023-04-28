import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        sys.exit("Usage: python dna.py databases/large.csv sequences/5.txt")

    # TODO: Read database file into a variable
    with open(sys.argv[1]) as Dfile:
        Dreader = csv.DictReader(Dfile)
        DNA = []
        for row in Dreader:
            DNA_dict = {}
            for column in row:
                DNA_dict[column] = row[column]
                if DNA_dict[column].isdigit():
                    DNA_dict[column] = int(DNA_dict[column])
            DNA.append(DNA_dict)

    # TODO: Read DNA sequence file into a variable
    with open(sys.argv[2]) as Sfile:
        Sreader = Sfile.read()

    # TODO: Find longest match of each STR in DNA sequence
    STR = []
    for i in DNA_dict.keys():
        subsequence = i
        sequence = Sreader
        for x in subsequence:
            # how many times the STR repeats starting at that position
            tmp = longest_match(sequence, subsequence)
        STR.append(tmp)

    # # TODO: Check database for matching profile
    for row in DNA:
        counter = 0
        dupla = zip(STR, row.values())
        for dup in dupla:
            if dup[0] == dup[1]:
                counter += 1
            else:
                counter = counter
        if counter == (len(STR))-1:
            print(row["name"])
            return
    if counter != (len(STR))-1:
        print("no match")
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
