# Funcion para detectar secuencias de ARN en una cadena.
sequence = input('Inserte secuencia: ')

def detect_sequences(sequence):
    sequence = sequence.strip()
    start_codon = 0
    sequence_number = 0
    detected_sequence = ""

    if len(sequence) < 9:
        print('Secuencias detectadas: {}'.format(sequence_number))
        return

    for index in range(0, len(sequence), 3):
        sequence_chunk = sequence[index:index + 3]

        if start_codon == 0 and sequence_chunk == 'AUG':
            start_codon = 1
            codon = 0
            detected_sequence += sequence_chunk
    
        elif start_codon == 1 and sequence_chunk not in ['AUG','UAG','UAA','UGA']:
            for character in range(len(sequence_chunk)):
                if character not in ['A', 'C', 'G', 'U']:
                    break
            codon += 1
            detected_sequence += sequence_chunk
    
        elif start_codon == 1 and codon != 0 and sequence_chunk in ['UAG','UAA','UGA']:
            sequence_number += 1
            detected_sequence += sequence_chunk
            print('\nNumero de condones en secuencia {}: {}'.format(sequence_number, codon))
            print('Secuencia {} detectada: {}'.format(sequence_number, detected_sequence))
            detected_sequence = ""
            start_codon = 0
    
        else:
            pass

    print('\nTotal Secuencias detectadas: {}'.format(sequence_number))

detect_sequences(sequence)
