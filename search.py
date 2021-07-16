#!/usr/bin/env python
import argparse

SEQUENCES_TO_SEARCH = ('CACGTG', 'CACATG', 'CATGTG', 'CACGCG', 'CGCGTG')
PLUS = 5
MINUS = 5
REVERSE = True
LENGTH = 20
SEQ_TO_SEARCH = 'GG'
SEQ_REV_TO_SEARCH = 'CC'
MOTIF_LENGTH = 3
# difference between motif length and sequence to search length
# eg. NGG, GG => 1
MOTIF_LENGTH_MINUS = 1


def search_sequence(full_sequence, short_sequence, position=0):
    """ Recurently search for sequence (not overlapping) """
    try:
        new_position = full_sequence[position:].index(short_sequence)+position
        return [new_position] + search_sequence(
            full_sequence, short_sequence, new_position+len(short_sequence))
    except ValueError:
        return []


def search_sequence2(full_sequence, short_sequence, position, max_position):
    """ Recurently search for sequence with step = 1"""
    new_position = None
    try:
        new_position = full_sequence[position:].index(short_sequence)+position
    except ValueError:
        return []
    if new_position > max_position:
        return []
    return [new_position] + search_sequence2(
        full_sequence, short_sequence, position+1, max_position)


def create_sequences(full_sequence, length, position):
    """ Create all sequences that not contain CCN or NGG motif, but 20
    nucleotides next to it (NGG - before NGG found, CCN - after CCN found
    NGG and CGG must be max 5 nucleotides after/before found sequence
    and may overlap with the found sequence"""
    sequences = []
    gg_positions = search_sequence2(
        full_sequence, SEQ_TO_SEARCH, position,
        max_position=position+length+PLUS-(MOTIF_LENGTH-MOTIF_LENGTH_MINUS))
    for gg_position in set(gg_positions):
        if gg_position-(MOTIF_LENGTH-MOTIF_LENGTH_MINUS) \
                < position+length+PLUS \
                and gg_position-MOTIF_LENGTH_MINUS >=position:
            sequences.append(
                (full_sequence[
                 max(0, gg_position-LENGTH-MOTIF_LENGTH_MINUS):
                 gg_position-MOTIF_LENGTH_MINUS],
                 '>'))
    cc_positions = search_sequence2(
        full_sequence, SEQ_REV_TO_SEARCH, max(position-MINUS, 0),
        max_position=position+length)
    for cc_position in set(cc_positions):
        if cc_position <= position+length-MOTIF_LENGTH:
            sequences.append(
                (reverse_complementary(
                    full_sequence[
                    cc_position+MOTIF_LENGTH:
                    min(cc_position+LENGTH+MOTIF_LENGTH, len(full_sequence))]),
                 '<'))
    return sequences


def reverse_complementary(sequence):
    """ Create reverse-complementary sequence"""
    new_sequence = ''.join([x for x in reversed(sequence)])
    new_sequence = new_sequence.replace('A', 'Z').replace('T', 'A')\
        .replace('Z', 'T').replace('C', 'Z').replace('G', 'C').replace('Z', 'G')
    return new_sequence
    

def get_data_from_csv(
        file_in, file_out, separator, header):
    input_fh = open(file_in, 'r')
    output_fh = open(file_out, 'w')
    header = True if header in (
        'true', 't', 'y', 'yes', 'True', 'Yes', 'Tak', 'tak') else False
    for line in input_fh.readlines():
        if header:
            header = False
            continue
        elements = line.split(separator)
        full_sequence = elements[3].upper().strip()
        generated_sequences = []
        for short_sequence in SEQUENCES_TO_SEARCH:
            positions = []
            positions += search_sequence(full_sequence, short_sequence)
            
            i = 0
            for position in positions:
                i+=1
                generated_sequences = create_sequences(
                    full_sequence, 6, position)
                for sequence in generated_sequences:
                    output_fh.write(
                        ";".join(elements[:3]+[short_sequence, str(i),
                                               sequence[1], sequence[0], 
                                               str(position+int(elements[1]))])+'\n')

    input_fh.close()
    output_fh.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", help="Input file")
    parser.add_argument("-o", help="Output file")
    parser.add_argument("-s", help="Separator", default=';')
    parser.add_argument("-d", help="Header", default='True')
    args = parser.parse_args()
    get_data_from_csv(args.i, args.o, args.s, args.d)



