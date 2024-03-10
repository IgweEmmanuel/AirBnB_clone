def my_function():
    from models.base_model import BaseModel
    
    global my_classes
    my_classes |= {
        "BaseModel": BaseModel,
    }

my_classes = {}
