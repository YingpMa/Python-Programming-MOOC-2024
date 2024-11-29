# Write your solution here
def longest(strings: list):
    count = len(strings[0])
    longest = strings[0]
    for item in strings:
        if len(item) > count:
            longest = item
            count = len(item)
    return longest


if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))