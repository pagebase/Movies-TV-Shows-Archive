def movie_exists(filename, movie_name):
    movie_name = movie_name.lower()  # normalize
    
    with open(filename, "a+", encoding="UTF-8") as f:
        lines = [line.lower() for line in f.readlines()]
    
    for line in lines:
        if movie_name in line:
            return True
    return False

def add_movie_name(filename,movie_name):
    with open("Counter.txt", "a+") as file:
        number=file.readlines()
    with open(filename, "a+", encoding="UTF-8") as f:
        f.seek(2)
        movie_trailer=input("Enter movie trailer link: ").strip() # `strip()` method remove white spaces from left side and right side
        f.write(f"\n{number} [{movie_name}]({movie_trailer})\n")
        number+=1
        file.write(f"{number}")


filename ="Movies.md"
search_movie = input("Enter movie name: ")

if movie_exists(filename, search_movie):
    print(f"✅ '{search_movie}' exists in {filename}")
else:
    # print(f"❌ '{search_movie}' not found in {filename}")
    add_movie_name(filename, search_movie)
