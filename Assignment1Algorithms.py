import time
import sys

class ProductData:
# Represents the products in the array
    def __init__(self, ID=0, Name='', Price=0, Category=''):
        self.ID = ID
        self.Name = Name
        self.Price = Price
        self.Category = Category
    
    def getID(self):
        return self.ID
    
    def getName(self):
        return self.Name
    
    def getPrice(self):
        return self.Price
    
    def getCategory(self):
        return self.Category
    
    def __str__(self):
        return f"({self.ID}, {self.Name}, {self.Price}, {self.Category})"
    
def analyzeSortPerformance(data, description, time_complexity):
    print(f"\n{description} - Starting array: {[str(product) for product in data]}")
    start = time.time()
    bubbleSort(data.copy())
    end = time.time()
    space_complexity = sys.getsizeof(data) + sys.getsizeof(start) + sys.getsizeof(end) + 64
    print(f"{description} - Time taken: {end - start:.6f} seconds, Space used: {space_complexity} bytes")
    print(f"Time Complexity: {time_complexity}\n")

if __name__ == "__main__":
    # Sample product data
    product_data = [
        ProductData(57353, 'Camera SBBHC', 546.88, 'Electronics'),
        ProductData(40374, 'Smartphone ILGCU', 947.54, 'Electronics'),
        ProductData(34863, 'Biography XPESK', 287.31, 'Books'),
        ProductData(18086, 'Shirt ZQLTI', 439.07, 'Clothing'),
        ProductData(16041, 'Jacket OTBKQ', 986.73, 'Clothing'),
        ProductData(43566, 'Mystery COKPK', 836.57, 'Books'),
        ProductData(69260, 'Toaster FODKJ', 867.6, 'Home & Kitchen'),
        ProductData(30895, 'Knife Set KGFUF', 385.77, 'Home & Kitchen'),
        ProductData(19897, 'Blender DPKLR', 488.62, 'Home & Kitchen'),
        ProductData(87296, 'Skirt IRTZX', 261.08, 'Clothing'),
        ProductData(68215, 'Laptop QLBQC', 404.21, 'Electronics'),
        ProductData(68097, 'Camera SGSRZ', 36.39, 'Electronics'),
        ProductData(26556, 'Novel METLI', 376.45, 'Books'),
        ProductData(30483, 'Knife Set WRSZZ', 55.97, 'Home & Kitchen'),
        ProductData(62422, 'Camera VFQWS', 382.69, 'Electronics'),
        ProductData(22806, 'Smartwatch VVFNT', 203.55, 'Electronics'),
        ProductData(24976, 'Pants YZMAK', 449.56, 'Clothing'),
        ProductData(30631, 'Headphones JFGYQ', 115.08, 'Electronics'),
        ProductData(27939, 'Textbook TWQKZ', 108.5, 'Books'),
        ProductData(41355, 'Headphones JOUXM', 211.57, 'Electronics'),
        ProductData(94162, 'Laptop WRJOZ', 956.53, 'Electronics'),
        ProductData(28710, 'Dress FRSMO', 879.09, 'Clothing'),
        ProductData(90291, 'Pants TIPUD', 853.38, 'Clothing'),
        ProductData(20368, 'Shirt FQFPK', 83.19, 'Clothing'),
        ProductData(68960, 'Blender OMDPS', 720.06, 'Home & Kitchen'),
        ProductData(40852, 'Novel IRROY', 603.68, 'Books'),
        ProductData(97895, 'Blender KSJHL', 123.25, 'Home & Kitchen'),
        ProductData(96314, 'Cutting Board LUICX', 628.29, 'Home & Kitchen'),
        ProductData(85719, 'Laptop GZORF', 641.33, 'Electronics'),
        ProductData(98625, 'Mystery BOPTP', 160.68, 'Books'),
        ProductData(66208, 'Blender GCZSK', 161.83, 'Home & Kitchen'),
        ProductData(86128, 'Biography ASTVE', 90.44, 'Books'),
        ProductData(10889, 'Shirt DNRZU', 316.48, 'Clothing'),
        ProductData(82777, 'Shirt OZWXU', 790.46, 'Clothing'),
        ProductData(43451, 'Mixer CKVJQ', 379.5, 'Home & Kitchen'),
        ProductData(12848, 'Toaster VZXUE', 867.97, 'Home & Kitchen'),
        ProductData(17646, 'Biography BPWXR', 424.83, 'Books'),
        ProductData(85197, 'Cutting Board IJVPP', 986.89, 'Home & Kitchen'),
        ProductData(13471, 'Knife Set TPCMO', 831.9, 'Home & Kitchen'),
        ProductData(66237, 'Headphones LTPLK', 995.13, 'Electronics'),
        ProductData(30251, 'Pants HCBKI', 450.68, 'Clothing'),
        ProductData(46944, 'Smartwatch QNALX', 647.08, 'Electronics'),
        ProductData(93533, 'Novel WOHSN', 516.39, 'Books'),
        ProductData(95090, 'Cutting Board RBACL', 568.63, 'Home & Kitchen'),
        ProductData(98827, 'Shirt RSQGL', 231.54, 'Clothing'),
        ProductData(64489, 'Novel EFPYC', 502.61, 'Books'),
        ProductData(39148, 'Cutting Board OYHCV', 220.15, 'Home & Kitchen'),
        ProductData(25425, 'Mystery MGSPG', 783.17, 'Books'),
        ProductData(69525, 'Camera XROCD', 76.05, 'Electronics'),
        ProductData(44574, 'Knife Set ASRHX', 64.62, 'Home & Kitchen')
    ]
    print("\nInitial:")
    for product in product_data:
        print(product)
    
    # Insert a new product at index 5
    new_product = ProductData(44444, 'Cookies', 2.99, 'Food & Drinks')
    product_data.insert(0, new_product)

    # Print each product's information after insertion
    print("\nAfter Insertion:")
    for product in product_data:
        print(product)
    
    product_data[0] =(44444, 'Cake', 2.99, 'Food & Drinks')
    print("\nAfter Update:")
    for product in product_data:
        print(product)

    product_data.pop(0)
    print("\nAfter Deletion:")
    for product in product_data:
        print(product)

    search_id = 64489
    found = False
    for product in product_data:
        if product.getID() == search_id:
            print(f"\nProduct with ID {search_id} found:")
            print(product)
            found = True
            break
    
    if not found:
        print(f"\nProduct with ID {search_id} not found in the list.")

def bubbleSort(product_data):
    n = len(product_data)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if product_data[j].getPrice() > product_data[j+1].getPrice():
                product_data[j], product_data[j+1] = product_data[j+1], product_data[j]
                swapped = True
        if not swapped:
            break
bubbleSort(product_data)
print("\nAfter Bubble Sort by Price:")
for product in product_data:
    print(product)


# Sorting already sorted data
analyzeSortPerformance(product_data, "Already Sorted Data", "Best Case: O(n)")

    # Sorting reverse sorted data
reverse_product_data = product_data[::-1]  # Reverse the list
analyzeSortPerformance(reverse_product_data, "Reverse Sorted Data", "Worst Case: O(n^2)")

    # Sorting random data
import random
random.shuffle(product_data)
analyzeSortPerformance(product_data, "Random Data", "Average Case: O(n^2)")

