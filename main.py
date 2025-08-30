def load_counter(filename):
    try:
        with open(filename, "r") as f:
            return int(f.read().strip())
    except (FileNotFoundError, ValueError):
        return 0  # default if file doesn't exist or is empty


def save_counter(filename, count):
    with open(filename, "w") as f:
        f.write(str(count))


# Example usage
filename = "counter.txt"

counter = load_counter(filename)
print("Current counter:", counter)

counter += 1  # increment
print("Updated counter:", counter)

save_counter(filename, counter)
