from collections import defaultdict

def main():
   fruits = ['apple', 'pear', 'orange', 'banana',
             'apple','grape','banana','banana']
   
   ## solution 1
   # # use a dictionary to count each element
   # fruitCounter = {}

   # # Count the elements in the list
   # for fruit in fruits:
   #    if fruit in fruitCounter.keys():
   #         fruitCounter[fruit] += 1
   #    else:
   #        fruitCounter[fruit] = 1
      
   ## solution 2
   # collection object
   fruitCounter = defaultdict(int)

   for fruit in fruits:
       fruitCounter[fruit] += 1
       
   
   # print the result
   for (k,v) in fruitCounter.items():
       print(k + ": " +str(v))


if __name__ == "__main__":
    main()