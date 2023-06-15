import os

if __name__ == "__main__":
    
    commands = [
        'add-user',
        'add-product',
        'add-review',
        'average-rating',
        'get-user-reviews'
    ]

    for command in commands:
        os.system("python main.py " + command)
