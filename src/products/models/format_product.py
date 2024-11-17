def format_product(product):
    product["id"] = str(product["_id"])
    del product["_id"]
    return product