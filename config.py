config = {
    "test_mode": {
        "is_active": True,
        "row_limit": 5,
        "reminder": """
              _______  ______   _____  _______                  
             |__   __||  ____| / ____||__   __|                 
                | |   | |__   | (___     | |                    
                | |   |  __|   \___ \    | |                    
                | |   | |____  ____) |   | |                    
              __|_|_  |______||_____/ ___|_|                    
             |  \/  | / __ \ |  __ \ |  ____|                   
             | \  / || |  | || |  | || |__                      
             | |\/| || |  | || |  | ||  __|                     
             | |  | || |__| || |__| || |____                    
             |_|  |_| \____/_|_____/_|______| __      __ ______ 
                 /\    / ____||__   __||_   _|\ \    / /|  ____|
                /  \  | |        | |     | |   \ \  / / | |__   
               / /\ \ | |        | |     | |    \ \/ /  |  __|  
              / ____ \| |____    | |    _| |_    \  /   | |____ 
             /_/    \_\______|   |_|   |_____|    \/    |______|
        """                                                   
    },
    "open_ai_model": "GPT_4o",
    "add_new_topics": True,
    "labels_column" : "labels",
    "topics_property" : "Ideas for Change",
    "temperature" : 0,
    "starting_topics" : []
}
#Below is an example schema, you will need to change it to match your datasets.
datasets = {
    "dataset_1": {
        "input_dataset_name": "x1",
        "output_dataset_name": "y1",
        "columns_for_prompt": [
            'column_1',
            'column_2',
            'column_3',
            'column_4',
            'column_5',
            'column_6'
        ],
        "examples_for_prompt": [
            {
                "prompt": "",
                "output": {"Expected output for LLM example 1"},
            },
            {
                "prompt": "",
                "output": {"Expected output for LLM example 2"}
            }
        ]
    },
    "dataset_2": {
        "input_dataset_name": "x2",
        "output_dataset_name": "y2",
        "columns_for_prompt": [
        'column_1',
        'column_2',
        'column_3',
        'column_4'
        ],
        "examples_for_prompt": [
            {
                "prompt": "",
                "output": {"Expected output for LLM example 1"},
            },
            {
                "prompt": "",
                "output": {"Expected output for LLM example 2"}
            }
        ]
    },
    "dataset_3": {
        "input_dataset_name": "x3",
        "output_dataset_name": "y3",
        "columns_for_prompt": [
           'column_1',
           'column_2',
           'column_3',
           'column_4',
           'column_5',
           'column_6',
           'column_7',
           'column_8',
           'column_9'
        ],
        "examples_for_prompt": [
            {
                "prompt": "",
                "output": {"Expected output for LLM example 1"},
            },
        ]
    },
}

config["test_mode"]["reminder"].strip()

if config["test_mode"]["is_active"]:
    print(config["test_mode"]["reminder"])