def columns_janitor(old_col_names):
    """
    input:    list
    output:   list
    """
    new_col_names_list = []
    for col_name in old_col_names:
        # strip whitespace
        col_name_stripped = col_name.strip()
        # make lowercase
        col_name_stripped_and_lower = col_name_stripped.lower()
        # replace " " with "_"
        col_name_stripped_and_lower_and_spaces_removed = col_name_stripped_and_lower.replace(" ", "_")
        # remove weird characters
        new_col_name = "".join(
            item for item in str(col_name_stripped_and_lower_and_spaces_removed) if item.isalnum() or "_" in item
        )
        # make sure there are 0 instances of 2 _'s next to each other
        while "__" in new_col_name:
            new_col_name = new_col_name.replace("__", "_")
        # make sure the column name does not lead or end with _
        while new_col_name[0] == "_":
            new_col_name = new_col_name[1 : len(new_col_name)]
        while new_col_name[len(new_col_name) - 1] == "_":
            new_col_name = new_col_name[0 : len(new_col_name) - 1]
        # append item to list of new columns
        new_col_names_list.append(new_col_name)

    # at end of loop, return the new columns 
    return new_col_names_list