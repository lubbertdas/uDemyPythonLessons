# https://www.youtube.com/watch?v=bD05uGo_sVI&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=36&ab_channel=CoreySchafer

condition = False

if condition:
    # Original function, before turning it into a generator
    def square_numbers(nums):
        result = []
        for i in nums:
            result.append(i*i)
        return result

    my_nums = square_numbers([1,2,3,4,5])
    print (my_nums)
    # output: [1, 4, 9, 16, 25]


    # now as generator, note the yield command
    def square_numbers(nums):
        for i in nums:
            yield(i*i)

    my_nums = square_numbers([1,2,3,4,5])
    #print (my_nums)
    # output: <generator object square_numbers at 0x033FC728>
    # the reason is that generators don't hold the entire result in memory, they yield one result at a time
    # simply put it's waiting for us to ask for the next result, it hasn't actually computed anything yet
    # in order to get the result, we have to use next
    print (next(my_nums))
    # output: 1
    print (next(my_nums))
    # output: 4
    print (next(my_nums))
    # output: 9
    # eventaully when we exceed the number of items to iterate over, we would get a StopIteration exception

    # in order to iterate over the number we can do this:
    for num in my_nums:
        print (num)

    # instead of our function this couldd also have been written as a "list comprehension" thing
    my_nums = [x*x for x in [1,2,3,4,5]]
    # in order to iterate over the number we can do this:
    print(my_nums)

    # if want to turn the list comprehension into a generator, we'd simpyl replace the brackets with parentheses
    my_nums = (x*x for x in [1,2,3,4,5])
    # in order to iterate over the number we can do this:
    for num in my_nums:
        print (num)

    my_nums = (x*x for x in [1,2,3,4,5])
    # as we said, the entire list isn't stored in memory as it hasn't been computed yet
    # we can however convert it into a list, like so:
    print (list(my_nums))
    # calling the list function, however, does lose the benefit of saving runtime and memory when using a generator

    # another generator example
    import random
    names = ['jack', 'jeff', 'joeph', 'bob']
    majors= ['kino', 'fern', 'mathe', 'bobsled']

    def people_generator(num_people):
        for i in range(num_people):
            person = {
                'id': i,
                'name': random.choice(names),
                'major': random.choice(majors)
            }
            yield person

    people = people_generator(400)
    for pople in people:
        print(pople)

