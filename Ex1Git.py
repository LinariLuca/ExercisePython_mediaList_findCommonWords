# Write 2 functions that perform the following tasks:

# 1. The first function, calculate_average(numbers), accepts a list of numbers as a parameter
#    and calculates the average of these numbers using the sum() function and arithmetic operations.
#    Example: calcola_media([10, 20, 30, 40, 50]) → returns the average (30.0)

# 2. The second function, find_words_common(text1, text2), accepts two texts as parameters.
#    - It must find the words that are common between the two texts,
#      using string operations, sets, and methods like split() and intersection().
#    - It must operate on words (not characters).
#    - It returns the set of common words.
#    Example input: "This is a sample text", "This is another sample"
#    Output: {"this", "is", "sample"}

############################################################################################################

class Ex1Git():

    #check_list: method to check that all numbers in a list are integers, because i want this constraint to be able to average
    def check_list(self, list_int):
        
        return all(isinstance(item, (int)) for item in list_int)

    #calculate_average: Given a list of numbers return the average of them
    def calculate_average(self, array):
        average = 0

        if self.check_list(array):
            average = sum(array) / len(array)
            print(f"Average of list {average}")
        else:
            print("Sorry, but I could not calculate the average of the list, as one of the elements is not an integer type!")

    #find_words_common: function that given two strings finds common words
    def find_words_common(self, str_1, str_2):
        ar_1 = str_1.lower().split() #.lower() for have all words in lower case
        ar_2 = str_2.lower().split()
        ar_common = []

        for x in ar_1:
            if x in ar_2:
                ar_common.append(x)
        
        ar_set = set(ar_common)
        ar_common_order = sorted(ar_set)

        print(f"First text: ", str_1)
        print(f"Second text: ", str_2)
        print(f"Common words {ar_common_order}") #in this case i use set to remove duplicates

    
    #find_words_common_with_set: given two words, one finds the communicating words, but in this case by using methods linked to the data structure 'set'
    def find_words_common_with_set(self, str_1, str_2):
        set_1 = set(str_1.lower().split())
        set_2 = set(str_2.lower().split())
        set_common = set_1.intersection(set_2)
        sorted_set = sorted(set_common) #sorted return a new sorted list
        
        print(f"First text: ", str_1)
        print(f"Second text: ", str_2)
        print(f"Common words {sorted_set}")



def main():
    print("-" * 45)
    print("Welcome to my program! I hope you can appreciate this exercise! 🙏🏻")
    print("-" * 45)
    objEx = Ex1Git()
    objEx.calculate_average([1,2,3,4,10])
    # objEx.calculate_average([1,2,3,4,[1,2,3]]) #remove the comment if you want to see a case where the average is not calculated
    print("-" * 45)
    objEx.find_words_common("My NAME is LUCA", "LUCA is NOT NAME in my TOWN is")
    print("-" * 45)
    objEx.find_words_common_with_set("My NAME is LUCA", "LUCA is NOT NAME in my TOWN is")
    print("-" * 45)


if __name__ == "__main__":
    main()

        

