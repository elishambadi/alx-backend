#!/usr/bin/python3
"""
Test
"""
import inspect
import sys

try:
    imported_file = __import__('1-fifo_cache')
    if imported_file.__doc__ is None or len(imported_file.__doc__) < 10:
        print("No documentation found")
    else:
        imported_file_items = imported_file.__dict__
        for k_item in imported_file_items.keys():
            item = imported_file_items[k_item]
        
            if inspect.isclass(item) and k_item not in ["Swagger", "flask", "Blueprint", "sqlalchemy", "CORS", "literal_processor", "Column", "String", "Queue"]:
                item_doc = item.__doc__
                if item_doc is None or len(item_doc) < 10:
                    print("Class {} not documented or not enough".format(k_item))
                    exit(1)
                class_items = item.__dict__
                for k_class_item in class_items.keys():
                    class_item = class_items[k_class_item]
                    if not inspect.isfunction(class_item) or k_class_item.startswith("__"):
                        continue
                    class_item_doc = class_item.__doc__
                    if class_item_doc is None or len(class_item_doc) < 10:
                        print("Function {} in class {} not documented or not enough".format(k_class_item, k_item))
                        exit(1)
            elif inspect.isfunction(item):
                item_doc = item.__doc__
                if item_doc is None or len(item_doc) < 10:
                    print("Function {} not documented or not enough".format(k_item))
                    exit(1)
        print("OK")

except:
    print(sys.exc_info()[1])
