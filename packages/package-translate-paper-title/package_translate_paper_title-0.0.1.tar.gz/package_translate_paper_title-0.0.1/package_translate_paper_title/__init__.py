# version as tuple for simple comparisons
VERSION = (0, 0, 1)
# string created from tuple to avoid inconsistency
__version__ = ".".join([str(x) for x in VERSION])

NO_SAVE_CHARACTER_SET = {':', "!", "?", ".", ",", "~",
                         "：", "！", "？", "。", "，"
                         }
CHAR_TO_REPLACE = "-"


def translate_paper_title_str(title_str: str) -> str:
    """
    process the paper title to save as file
    1. replace space with `-`
    2. get rid of `:` or `/`

    :param title_str:
    :return: save-able str
    """
    # 0. strip space
    save_str: str = title_str.strip().replace(" ", CHAR_TO_REPLACE)

    # 1. remove special character
    for need_delete_char in NO_SAVE_CHARACTER_SET:
        save_str = save_str.replace(need_delete_char, CHAR_TO_REPLACE)

    return save_str
