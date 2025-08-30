filename = "Movies.md"
search_data = input("Enter movie name: ").lower()

# Read existing lines
with open(filename, "a+") as f:
    f.seek(0)  # move to start to read
    lines = [line.lower() for line in f.read().splitlines()]  # read all lines without newline chars

    if search_data in lines:
        print(f"{search_data} already exists!")
    else:
        f.write(search_data + "\n")
        print(f"{search_data} added successfully!")
