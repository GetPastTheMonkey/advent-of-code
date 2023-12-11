from utils import get_input_lines, chunk


def main():
    seeds = []
    mappings = []
    current_mapping = []

    for line in get_input_lines(__file__):
        if line.startswith("seeds"):
            seeds = list(chunk(list(map(int, line.split(": ")[1].split(" "))), 2))
        elif line.endswith(":"):
            if current_mapping:
                mappings.append(current_mapping)
                current_mapping = []
        elif len(line) == 0:
            continue
        else:
            current_mapping.append(tuple(map(int, line.split(" "))))

    if current_mapping:
        mappings.append(current_mapping)

    leftovers = seeds

    for mapping in mappings:
        new_ranges = []

        for m_d, m_s, m_l in mapping:
            new_leftovers = []

            for l_s, l_l in leftovers:
                # Short-circuit for non-overlap
                if l_s + l_l - 1 < m_s or m_s + m_l - 1 < l_s:
                    new_leftovers.append((l_s, l_l))
                    continue

                # Handle different overlaps
                contains_start = m_s <= l_s < m_s + m_l
                contains_end = m_s <= l_s + l_l - 1 < m_s + m_l

                if contains_start and contains_end:
                    # CASE 1: The leftover is fully contained
                    #  --> Add single new range, no new leftovers
                    new_ranges.append((m_d + l_s - m_s, l_l))
                elif contains_start:
                    # CASE 2: The leftover start is contained, but the end not
                    #  --> Add new range, new leftover from end of mapping to end of leftover
                    new_ranges.append((m_d + l_s - m_s, m_l - l_s + m_s))
                    new_leftovers.append((m_s + m_l, l_l - (m_l - l_s + m_s)))
                elif contains_end:
                    # CASE 3: The leftover end is contained, but the start not
                    #  --> Add new range, new leftover from start of leftover to start of mapping
                    new_ranges.append((m_d, l_l - (m_s - l_s)))
                    new_leftovers.append((l_s, m_s - l_s))
                else:
                    # CASE 4: The leftover fully contains the mapping
                    #  --> Add new range, two new leftovers
                    #    --> One from start of leftover to start of mapping
                    #    --> One from end of mapping to end of leftover
                    new_ranges.append((m_d, m_l))
                    new_leftovers.append((l_s, m_s - l_s))
                    new_leftovers.append((m_s + m_l, m_s + m_l - l_s))

            leftovers = new_leftovers

        # Add non-translated leftovers --> Not contained in any mapping
        new_ranges.extend(leftovers)

        # Set new ranges obtained from this mapping
        leftovers = new_ranges

    print(min(map(lambda x: x[0], leftovers)))


if __name__ == '__main__':
    main()
