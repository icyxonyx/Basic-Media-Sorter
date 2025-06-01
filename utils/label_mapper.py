CATEGORY_KEYWORDS = {
    'people': ['person', 'man', 'woman', 'boy', 'girl'],
    'pets': ['cat', 'dog', 'puppy', 'kitten'],
    'food': ['pizza', 'cake', 'burger', 'food'],
    'selfies': ['selfie', 'face'],
    'nature': ['tree', 'forest', 'grass', 'plant'],
    'beaches': ['beach', 'sand', 'surfboard'],
    'mountains': ['mountain'],
    'sky': ['sky'],
    'sunsets': ['sunset'],
    'cityscapes': ['building', 'skyscraper', 'city'],
    'cars': ['car', 'jeep', 'limousine', 'convertible'],
    'flowers': ['flower', 'rose', 'tulip'],
    'sports': ['sports', 'soccer', 'tennis', 'basketball'],
    'concerts': ['concert', 'stage', 'musician'],
    'screenshots': ['screenshot', 'screen', 'text'],
    'documents': ['document', 'paper', 'report'],
    'birthdays': ['birthday', 'cake'],
    'weddings': ['wedding', 'bride', 'groom'],
    'holidays': ['holiday', 'christmas', 'easter'],
    'travel': ['airplane', 'passport', 'luggage', 'travel']
}

def map_labels_to_category(labels):
    for category, keywords in CATEGORY_KEYWORDS.items():
        for label in labels:
            if any(keyword in label.lower() for keyword in keywords):
                return category.capitalize()
    return "Uncategorized"
