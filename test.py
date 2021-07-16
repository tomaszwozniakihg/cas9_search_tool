import unittest

from search import search_sequence, search_sequence2, create_sequences


class TestStringMethods(unittest.TestCase):

    def test_create_sequences_forward_1(self):
        sequence = 'XXXXXXXXXXXXXXXXXXXXXXXXXMMMMMMXXXXXXXXXXXXXXXXXXXXXXXXX'
        sequences = create_sequences(sequence, 6, 25)
        self.assertEqual(len(sequences), 0)

    def test_create_sequences_forward_1prim(self):
        sequence = 'XXXXXXXXXXXXXXXXXXXXXXXXXMMMMMMXXXXGGXXXXXXXXXXXXXXXXXXXX'
        sequences = create_sequences(sequence, 6, 25)
        self.assertEqual(len(sequences), 0)

    def test_create_sequences_forward_2(self):
        sequence = 'XXXXXXXXXXXXXXXXXXXXXXXXXMMMMMMXXXGGXXXXXXXXXXXXXXXXXXXX'
        sequences = create_sequences(sequence, 6, 25)
        self.assertEqual(len(sequences), 1)
        self.assertEqual(sequences[0][0], 'XXXXXXXXXXXXMMMMMMXX')
        self.assertEqual(sequences[0][1], '>')

    def test_create_sequences_forward_3(self):
        sequence = 'XXXXXXXXXXXXXXXXXXXXXXXXXMMMMMMXXGGXXXXXXXXXXXXXXXXXXXXX'
        sequences = create_sequences(sequence, 6, 25)
        self.assertEqual(len(sequences), 1)
        self.assertEqual(sequences[0][0], 'XXXXXXXXXXXXXMMMMMMX')
        self.assertEqual(sequences[0][1], '>')

    def test_create_sequences_forward_4(self):
        sequence = 'XXXXXXXXXXXXXXXXXXXXXXXXXMMMMMMXGGXXXXXXXXXXXXXXXXXXXXXX'
        sequences = create_sequences(sequence, 6, 25)
        self.assertEqual(len(sequences), 1)
        self.assertEqual(sequences[0][0], 'XXXXXXXXXXXXXXMMMMMM')
        self.assertEqual(sequences[0][1], '>')

    def test_create_sequences_forward_5(self):
        sequence = 'XXXXXXXXXXXXXXXXXXXXXXXXXMMMMMMGGXXXXXXXXXXXXXXXXXXXXXXX'
        sequences = create_sequences(sequence, 6, 25)
        self.assertEqual(len(sequences), 1)
        self.assertEqual(sequences[0][0], 'XXXXXXXXXXXXXXXMMMMM')
        self.assertEqual(sequences[0][1], '>')

    def test_create_sequences_forward_6(self):
        sequence = 'XXXXXXXXXXXXXXXXXXXXXXXXXMMMMMGGXXXXXXXXXXXXXXXXXXXXXXXX'
        sequences = create_sequences(sequence, 6, 25)
        self.assertEqual(len(sequences), 1)
        self.assertEqual(sequences[0][0], 'XXXXXXXXXXXXXXXXMMMM')
        self.assertEqual(sequences[0][1], '>')

    def test_create_sequences_forward_7(self):
        sequence = 'XXXXXXXXXXXXXXXXXXXXXXXXXMMMMGGXXXXXXXXXXXXXXXXXXXXXXXXX'
        sequences = create_sequences(sequence, 6, 25)
        self.assertEqual(len(sequences), 1)
        self.assertEqual(sequences[0][0], 'XXXXXXXXXXXXXXXXXMMM')
        self.assertEqual(sequences[0][1], '>')

    def test_create_sequences_forward_8(self):
        sequence = 'XXXXXXXXXXXXXXXXXXXXXXXXXMMMGGMXXXXXXXXXXXXXXXXXXXXXXXXX'
        sequences = create_sequences(sequence, 6, 25)
        self.assertEqual(len(sequences), 1)
        self.assertEqual(sequences[0][0], 'XXXXXXXXXXXXXXXXXXMM')
        self.assertEqual(sequences[0][1], '>')

    def test_create_sequences_forward_9(self):
        sequence = 'XXXXXXXXXXXXXXXXXXXXXXXXXMMGGMMXXXXXXXXXXXXXXXXXXXXXXXXX'
        sequences = create_sequences(sequence, 6, 25)
        self.assertEqual(len(sequences), 1)
        self.assertEqual(sequences[0][0], 'XXXXXXXXXXXXXXXXXXXM')
        self.assertEqual(sequences[0][1], '>')

    def test_create_sequences_forward_10(self):
        sequence = 'XXXXXXXXXXXXXXXXXXXXXXXXXMGGMMMXXXXXXXXXXXXXXXXXXXXXXXXX'
        sequences = create_sequences(sequence, 6, 25)
        self.assertEqual(len(sequences), 1)
        self.assertEqual(sequences[0][0], 'XXXXXXXXXXXXXXXXXXXX')
        self.assertEqual(sequences[0][1], '>')

    def test_create_sequences_forward_11(self):
        sequence = 'XXXXXXXXXXXXXXXXXXXXXXXXXGGMMMMXXXXXXXXXXXXXXXXXXXXXXXXX'
        sequences = create_sequences(sequence, 6, 25)
        self.assertEqual(len(sequences), 0)

    def test_create_sequences_forward_12(self):
        sequence = 'XXXXXXXXXXXXXXXXXXXXXXXXGGMMMMMXXXXXXXXXXXXXXXXXXXXXXXXX'
        sequences = create_sequences(sequence, 6, 25)
        self.assertEqual(len(sequences), 0)

    def test_create_sequences_forward_13(self):
        sequence = 'XXXXXXXXXXXXXXXXXXXXXXXGGMMMMMMXXXXXXXXXXXXXXXXXXXXXXXXX'
        sequences = create_sequences(sequence, 6, 25)
        self.assertEqual(len(sequences), 0)

    def test_create_sequences_forward_14(self):
        sequence = 'XXXXXXXXXXXXXXXXXXXXXXGGXMMMMMMXXXXXXXXXXXXXXXXXXXXXXXXX'
        sequences = create_sequences(sequence, 6, 25)
        self.assertEqual(len(sequences), 0)

    def test_create_sequences_forward__ends_15(self):
        sequence = 'XXXXXXXXXXXXXXXXXXXXXXXXXMMMMMMXXXGG'
        sequences = create_sequences(sequence, 6, 25)
        self.assertEqual(len(sequences), 1)
        self.assertEqual(sequences[0][0], 'XXXXXXXXXXXXMMMMMMXX')
        self.assertEqual(sequences[0][1], '>')

    def test_create_sequences_forward__ends_16(self):
        sequence = 'MMMMMMXXXGGXXXXXXXXXXXXXXXXXXXX'
        sequences = create_sequences(sequence, 6, 0)
        self.assertEqual(len(sequences), 1)
        self.assertEqual(sequences[0][0], 'MMMMMMXX')
        self.assertEqual(sequences[0][1], '>')

    def test_create_sequences_reverse_0(self):
        sequence = 'XXXXXXXXXXXXXXXXXXXCCXXXXMMMMMMXXXXXXXXXXXXXXXXXXXXXXXXX'
        sequences = create_sequences(sequence, 6, 25)
        self.assertEqual(len(sequences), 0)

    def test_create_sequences_reverse_1(self):
        sequence = 'XXXXXXXXXXXXXXXXXXXXCCXXXMMMMMMXXXXXXXXXXXXXXXXXXXXXXXXX'
        sequences = create_sequences(sequence, 6, 25)
        self.assertEqual(len(sequences), 1)
        self.assertEqual(sequences[0][0], 'XXXXXXXXXXXXMMMMMMXX')
        self.assertEqual(sequences[0][1], '<')

    def test_create_sequences_reverse_2(self):
        sequence = 'XXXXXXXXXXXXXXXXXXXXXCCXXMMMMMMXXXXXXXXXXXXXXXXXXXXXXXXX'
        sequences = create_sequences(sequence, 6, 25)
        self.assertEqual(len(sequences), 1)
        self.assertEqual(sequences[0][0], 'XXXXXXXXXXXXXMMMMMMX')
        self.assertEqual(sequences[0][1], '<')

    def test_create_sequences_reverse_3(self):
        sequence = 'XXXXXXXXXXXXXXXXXXXXXXCCXMMMMMMXXXXXXXXXXXXXXXXXXXXXXXXX'
        sequences = create_sequences(sequence, 6, 25)
        self.assertEqual(len(sequences), 1)
        self.assertEqual(sequences[0][0], 'XXXXXXXXXXXXXXMMMMMM')
        self.assertEqual(sequences[0][1], '<')

    def test_create_sequences_reverse_4(self):
        sequence = 'XXXXXXXXXXXXXXXXXXXXXXXCCMMMMMMXXXXXXXXXXXXXXXXXXXXXXXXX'
        sequences = create_sequences(sequence, 6, 25)
        self.assertEqual(len(sequences), 1)
        self.assertEqual(sequences[0][0], 'XXXXXXXXXXXXXXXMMMMM')
        self.assertEqual(sequences[0][1], '<')

    def test_create_sequences_reverse_5(self):
        sequence = 'XXXXXXXXXXXXXXXXXXXXXXXXCCMMMMMXXXXXXXXXXXXXXXXXXXXXXXXX'
        sequences = create_sequences(sequence, 6, 25)
        self.assertEqual(len(sequences), 1)
        self.assertEqual(sequences[0][0], 'XXXXXXXXXXXXXXXXMMMM')
        self.assertEqual(sequences[0][1], '<')

    def test_create_sequences_reverse_6(self):
        sequence = 'XXXXXXXXXXXXXXXXXXXXXXXXXCCMMMMXXXXXXXXXXXXXXXXXXXXXXXXX'
        sequences = create_sequences(sequence, 6, 25)
        self.assertEqual(len(sequences), 1)
        self.assertEqual(sequences[0][0], 'XXXXXXXXXXXXXXXXXMMM')
        self.assertEqual(sequences[0][1], '<')

    def test_create_sequences_reverse_7(self):
        sequence = 'XXXXXXXXXXXXXXXXXXXXXXXXXMCCMMMXXXXXXXXXXXXXXXXXXXXXXXXX'
        sequences = create_sequences(sequence, 6, 25)
        self.assertEqual(len(sequences), 1)
        self.assertEqual(sequences[0][0], 'XXXXXXXXXXXXXXXXXXMM')
        self.assertEqual(sequences[0][1], '<')

    def test_create_sequences_reverse_8(self):
        sequence = 'XXXXXXXXXXXXXXXXXXXXXXXXXMMCCMMXXXXXXXXXXXXXXXXXXXXXXXXX'
        sequences = create_sequences(sequence, 6, 25)
        self.assertEqual(len(sequences), 1)
        self.assertEqual(sequences[0][0], 'XXXXXXXXXXXXXXXXXXXM')
        self.assertEqual(sequences[0][1], '<')

    def test_create_sequences_reverse_9(self):
        sequence = 'XXXXXXXXXXXXXXXXXXXXXXXXXMMMCCMXXXXXXXXXXXXXXXXXXXXXXXXX'
        sequences = create_sequences(sequence, 6, 25)
        self.assertEqual(len(sequences), 1)
        self.assertEqual(sequences[0][0], 'XXXXXXXXXXXXXXXXXXXX')
        self.assertEqual(sequences[0][1], '<')

    def test_create_sequences_reverse_10(self):
        sequence = 'XXXXXXXXXXXXXXXXXXXXXXXXXMMMMCCXXXXXXXXXXXXXXXXXXXXXXXXX'
        sequences = create_sequences(sequence, 6, 25)
        self.assertEqual(len(sequences), 0)

    def test_create_sequences_reverse_11(self):
        sequence = 'XXXXXXXXXXXXXXXXXXXXXXXXXMMMMMCCXXXXXXXXXXXXXXXXXXXXXXXX'
        sequences = create_sequences(sequence, 6, 25)
        self.assertEqual(len(sequences), 0)

    def test_create_sequences_reverse_12(self):
        sequence = 'XXXXXXXXXXXXXXXXXXXXXXXXXMMMMMMCCXXXXXXXXXXXXXXXXXXXXXXX'
        sequences = create_sequences(sequence, 6, 25)
        self.assertEqual(len(sequences), 0)

    def test_create_sequences_reverse_13(self):
        sequence = 'XXXXXXXXXXXXXXXXXXXXXXXXXMMMMMMXCCXXXXXXXXXXXXXXXXXXXXXX'
        sequences = create_sequences(sequence, 6, 25)
        self.assertEqual(len(sequences), 0)

    def test_create_sequences_reverse_14(self):
        sequence = 'XXXXXXXXXXXXXXXXXXXXXXXXXMMMMMMXXCCXXXXXXXXXXXXXXXXXXXXX'
        sequences = create_sequences(sequence, 6, 25)
        self.assertEqual(len(sequences), 0)

    def test_create_sequences_reverse_ends_15(self):
        sequence = 'XXXXXXXXXXXXXXXXXXXXXCCXXMMMMMM'
        sequences = create_sequences(sequence, 6, 25)
        self.assertEqual(len(sequences), 1)
        self.assertEqual(sequences[0][0], 'MMMMMMX')
        self.assertEqual(sequences[0][1], '<')

    def test_create_sequences_reverse_ends_16(self):
        sequence = 'CCXXMMMMMMXXXXXXXXXXXXXXXXXXXXXXXXX'
        sequences = create_sequences(sequence, 6, 4)
        self.assertEqual(len(sequences), 1)
        self.assertEqual(sequences[0][0], 'XXXXXXXXXXXXXMMMMMMX')
        self.assertEqual(sequences[0][1], '<')



if __name__ == '__main__':
    unittest.main()

