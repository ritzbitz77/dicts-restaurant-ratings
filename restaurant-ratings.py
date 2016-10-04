def sort_ratings(restaurant_file):
    with open(restaurant_file) as restaurant_ratings:

        alpha_ratings = {}

        for line in restaurant_ratings:
            data = line.rstrip().split(":")
            restaurant_name = data[0]
            restaurant_rating = data[1]

            alpha_ratings[restaurant_name] = restaurant_rating


        new_restaurant = raw_input("What is the name of the restaurant that are rating?: ")

        alpha_ratings[new_restaurant] = int(raw_input ("What rating would you give this restaurant?: "))

        alpha_ratings = sorted(alpha_ratings.items())        

        for restaurant_info in alpha_ratings:
            sorted_restaurant_name = restaurant_info[0]
            sorted_restaurant_rating = int(restaurant_info[1])

            print "%s is rated at %d." % (sorted_restaurant_name, sorted_restaurant_rating)


sort_ratings("scores.txt")