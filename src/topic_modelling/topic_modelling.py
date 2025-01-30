from foundry.transforms import Dataset


def get_topic_list_from_datasets(datasets, labels_column, topics_property, config):
    """
    Extracts a list of topics from multiple datasets.

    This function reads data from a list of datasets, extracts specific columns, and compiles a list of topics.
    It supports a test mode that limits the number of rows processed from each dataset.

    Args:
        datasets (dict): A dictionary where keys are dataset identifiers and values are dictionaries containing dataset metadata, including the "output_dataset_name".
        labels_column (str): The name of the column containing the labels in the datasets.
        topics_property (str): The property name for topics (not used in the current implementation).
        config (dict): Configuration dictionary containing test mode settings. Expected keys are:
            - "test_mode": A dictionary with:
                - "is_active" (bool): Flag to activate test mode.
                - "row_limit" (int): Number of rows to process in test mode.

    Returns:
        list: A list of dictionaries, each containing the "tm_id" and "labels" from the datasets.
    """
    all_topics = []
    for dataset_name, dataset in datasets.copy().items():
        
        if not dataset["use"]:
            print(dataset_name + " not in use, skipping...")
            del datasets[dataset_name]
            continue
        print("getting labels from " + dataset_name)
        
        df_dataset =  Dataset.get(dataset["output_dataset_name"]).read_table(format="pandas")
        if config["test_mode"]["is_active"]:
            df_dataset = df_dataset[0:config["test_mode"]["row_limit"]]
        
        id_and_labels = df_dataset[["tm_id", "labels"]].to_dict(orient="records")

        all_topics += id_and_labels

    return all_topics

def add_topics(all_responses, topic_array, current_topics, add_new_topics):
    """
    Adds a new array of topics to the list of all responses and updates the current topics list.

    This function appends the provided `topic_array` to the `all_responses` list. It then iterates
    through each topic in `topic_array` and adds it to `current_topics` if it is not already present.

    All topics are converted to lower case.

    Args:
        all_responses (list): A list containing all topic arrays.
        topic_array (list): A list of topics to be added.
        current_topics (list): A list of currently tracked topics.
        add_new_topics (bool): Sets whether the LLM is allowed to add new topics or not

    Returns:
        tuple: A tuple containing the updated `all_responses`, `topic_array`, and `current_topics`.
    """ 
   
    topic_array = {
        "tm_id": topic_array["tm_id"],
        "topics": [topic.lower() for topic in topic_array["topics"]]
    }

    all_responses.append(topic_array)
    
    if add_new_topics:
        for topic in topic_array["topics"]:
            if topic not in current_topics:
                current_topics.append(topic)
            
    return all_responses, topic_array, current_topics

def contains_nests(arr):
    """
    Checks if a given list contains any nested lists.

    Args:
        arr (list): The list to check for nested lists.

    Returns:
        bool: True if the list contains at least one nested list, False otherwise.
    """
    for element in arr:
        if isinstance(element, list):
            return True
    return False
    
def flatten_list(array):
    """
    Flattens a nested list into a single list of elements.

    Args:
        array (list): The list to flatten, which may contain nested lists.

    Returns:
        list: A single list containing all the elements from the nested lists.
    """
    result = []
    for item in array:
        if isinstance(item, list):
            result.extend(flatten_list(item))  # Recursively flatten nested lists
        else:
            result.append(item)
    return result

def add_topic_flag_cols(df_labels_and_topics, current_topics):
    """
    Adds flag columns to the dataframe for each topic in the current topics list.

    This function iterates over the list of current topics and adds a new column to the dataframe `df_labels_and_topics` for each topic. Each new column is a boolean flag indicating whether the topic is present in the "Topics" column of the dataframe. 
    
    Args:
        df_labels_and_topics (pandas.DataFrame): A dataframe containing a "Topics" column with lists of topics.
        current_topics (list of str): A list of topics to create flag columns for.

    Returns:
        pandas.DataFrame: The modified dataframe with added topic flag columns
    """
    for topic in current_topics:
        df_labels_and_topics[topic] = df_labels_and_topics["Topics"].apply(lambda x: topic in x)
    
    return df_labels_and_topics