import arcpy

# Set the workspace
workspace = r'C:/Users/Hanan/OneDrive/Documents/ArcGIS/Projects/MyProject2/MyProject2.gdb'
arcpy.env.workspace = workspace

def create_feature_class():
    name = input("Enter the name for the new feature class: ")
    arcpy.CreateFeatureclass_management(workspace, name, "POINT")

def delete_feature_class():
    name = input("Enter the name of the feature class to delete: ")
    arcpy.Delete_management(name)

def delete_fields():
    feature_class = input("Enter the name of the feature class: ")
    fields = arcpy.ListFields(feature_class)
    for field in fields:
        field_name = field.name
        print(f"Field: {field_name}")
    field_to_delete = input("Enter the name of the field to delete: ")
    arcpy.DeleteField_management(feature_class, field_to_delete)

def search_fields():
    feature_class = input("Enter the name of the feature class: ")
    fields = arcpy.ListFields(feature_class)
    for field in fields:
        field_name = field.name
        print(f"Field: {field_name}")

def add_fields():
    feature_class = input("Enter the name of the feature class: ")
    field_name = input("Enter the name of the new field: ")
    field_type = input("Enter the data type of the new field: ")
    arcpy.AddField_management(feature_class, field_name, field_type)

def edit_fields():
    feature_class = input("Enter the name of the feature class: ")
    fields = arcpy.ListFields(feature_class)
    for field in fields:
        field_name = field.name
        print(f"Field: {field_name}")
    field_to_edit = input("Enter the name of the field to edit: ")
    new_field_name = input("Enter the new name for the field: ")
    arcpy.AlterField_management(feature_class, field_to_edit, new_field_name)

def list_fields():
    feature_class = input("Enter the name of the feature class: ")
    fields = arcpy.ListFields(feature_class)
    for field in fields:
        field_name = field.name
        print(f"Field: {field_name}")

def add_row_attributes():
    feature_class = input("Enter the name of the feature class: ")
    fields = arcpy.ListFields(feature_class)
    for field in fields:
        field_name = field.name
        print(f"Field: {field_name}")
    field_values = []
    for field in fields:
        field_value = input(f"Enter a value for field '{field.name}': ")
        field_values.append(field_value)
    with arcpy.da.InsertCursor(feature_class, [field.name for field in fields]) as cursor:
        cursor.insertRow(field_values)

def edit_row_attributes():
    feature_class = input("Enter the name of the feature class: ")
    object_id = input("Enter the Object ID of the row to edit: ")
    fields = arcpy.ListFields(feature_class)
    field_names = [field.name for field in fields]
    with arcpy.da.UpdateCursor(feature_class, field_names, f"OBJECTID = {object_id}") as cursor:
        for row in cursor:
            for i, field in enumerate(fields):
                field_name = field.name
                new_value = input(f"Enter a new value for field '{field_name}': ")
                row[i] = new_value
            cursor.updateRow(row)

def search_attributes():
    feature_class = input("Enter the name of the feature class: ")
    search_value = input("Enter the value to search for: ")
    fields = arcpy.ListFields(feature_class)
    field_names = [field.name for field in fields]
    with arcpy.da.SearchCursor(feature_class, field_names, f"OBJECTID = {search_value}") as cursor:
        for row in cursor:
            for i, field in enumerate(fields):
                field_name = field.name
                value = row[i]
                print(f"{field_name}: {value}")

def delete_row_attributes():
    feature_class = input("Enter the name of the feature class: ")
    object_id = input("Enter the Object ID of the row to delete: ")
    with arcpy.da.UpdateCursor(feature_class, "OBJECTID", f"OBJECTID = {object_id}") as cursor:
        for row in cursor:
            cursor.deleteRow()

# Menu
while True:
    print("Menu:")
    print("1. Create Feature Class")
    print("2. Delete Feature Class")
    print("3. Delete Fields")
    print("4. Search Fields")
    print("5. Add Fields")
    print("6. Edit Fields")
    print("7. List Fields")
    print("8. Add Row Attributes")
    print("9. Edit Row Attributes")
    print("10. Search Attributes")
    print("11. Delete Row Attributes")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        create_feature_class()
    elif choice == "2":
        delete_feature_class()
    elif choice == "3":
        delete_fields()
    elif choice == "4":
        search_fields()
    elif choice == "5":
        add_fields()
    elif choice == "6":
        edit_fields()
    elif choice == "7":
        list_fields()
    elif choice == "8":
        add_row_attributes()
    elif choice == "9":
        edit_row_attributes()
    elif choice == "10":
        search_attributes()
    elif choice == "11":
        delete_row_attributes()
    elif choice == "0":
        break
    else:
        print("Invalid choice. Please try again.")
