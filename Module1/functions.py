def firstname(fname):
    def arbname(*kids):
        print(fname + " is the father of : " + kids[1])
        print("name of my kid is : " + kids[1])
        
    arbname("kunj","rekha","srushti")
firstname("kunj")