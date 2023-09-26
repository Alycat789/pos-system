for i in range(10):
    print(i)

# Sure would be nice if I could clear that stuff before I print the next thing
print("\033c", end="") # This clears the terminal
print("next thing")


# os.path.exists(file_path)
# os.rmdir(folder)
