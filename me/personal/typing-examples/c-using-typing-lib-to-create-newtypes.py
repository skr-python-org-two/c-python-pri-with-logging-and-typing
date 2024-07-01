from typing import NewType



def typing_on_creating_new_datatype():
    # Creating new types for user IDs and product IDs to prevent mixing them up
    UserID = NewType('UserID', int)
    ProductID = NewType('ProductID', int)

    def get_user_name(user_id: UserID) -> str:
        # Function that requires a UserID
        print(user_id*10)
        return str(f"sekhar_{user_id}")

    def get_product_name(product_id: ProductID) -> str:
        # Function that requires a ProductID
        print(product_id*20)
        return str(f"dark_chocolate_{product_id}")

    user_id = UserID(523)
    product_id = ProductID(987)

    # These calls are now type-safe, preventing mix-ups
    user_name = get_user_name(user_id)
    product_name = get_product_name(product_id)
    print(f"user_name is ::: {user_name}")
    print("product_name is ::: {0} ".format(product_name))



def main():
    typing_on_creating_new_datatype()


if __name__ == "__main__":
    main()





