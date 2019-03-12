from urllib.request import urlopen


def get_muh_words():
    with urlopen('http://sixty-north.com/c/t.txt') as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)

        print(' '.join(story_words))


if __name__ == "__main__":
    get_muh_words()
