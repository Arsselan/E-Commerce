# edited by Miles Sasportas
#Mock example to test filter search by parameter
from .models import Product


def get_mock_products():
    """
    Generates 6 mock products
    """
    return [
        Product(id=1, name="Product 1", desc="Description 1", price=19.99, stock=10, imgpath="path/to/img1"),
        Product(id=2, name="Product 2", desc="Description 2", price=99.99, stock=20, imgpath="path/to/img2"),
        Product(id=3, name="Product 3", desc="Description 3", price=57.99, stock=15, imgpath="path/to/img3"),
        Product(id=4, name="Product 4", desc="Description 4", price=280.00, stock=5, imgpath="path/to/img4"),
        Product(id=5, name="Product 5", desc="Description 5", price=77.77, stock=12, imgpath="path/to/img5"),
        Product(id=6, name="Product 6", desc="Description 6", price=333.33, stock=8, imgpath="path/to/img6"),
    ]

# # def sort_table_by_parameter(parameter,reverse=False):
# #     mock_table = get_mock_products()
# #     sorted_table = sorted(mock_table,key=lambda x: x[parameter],reverse=reverse)

# #     return sorted_table


# #Sort the mock table by parameter, Reverse order is activated 
# # sorted_table = sort_table_by_parameter("Rating",reverse=True)

# # for row in sorted_table:
# #     print(row)


  