import data_collection_scripts.property_data_collection as property_data_collection, data_collection_scripts.neighbourhood_data_collection as neighbourhood_data_collection, data_collection_scripts.room_data_collection as room_data_collection

if __name__ == "__main__":
    property_data_collection.collect_property_data()
    neighbourhood_data_collection.collect_neighbourhood_data()
    room_data_collection.collect_room_data()