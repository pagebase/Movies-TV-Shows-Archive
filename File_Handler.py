def movie_exists(filename, movie_name):
    
    with open(filename, "r", encoding="utf-8") as f:
        lines = [line.lower() for line in f.readlines()]
    
    for line in lines:
        if movie_name in line:
            return True
    return False

def add_new_movie(filename, movie_name, movie_trailer):
    with open("Counter.txt","a+") as sr_file:
        line=sr_file.readlines()
        for i in line:
            print(i)
    with open(filename, "a+") as f:
        f.write(f"\n[{movie_name}]({movie_trailer})\n")
        f.close()
# Example usage
filename = r"Movies.md"
search_movie = input("Enter movie name: ").strip().lower()

if movie_exists(filename, search_movie):
    print(f"✅ '{search_movie}' exists in {filename}")
else:
    movie_trailer=input("Enter movie trailer: ").strip()
    add_new_movie(filename, search_movie, movie_trailer)
