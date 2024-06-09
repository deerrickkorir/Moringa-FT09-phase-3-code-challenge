from database.setup import create_tables
from models.article import Article
from models.author import Author
from models.magazine import Magazine

def main():
    # Initialize the database and create tables
    create_tables()

    # Collect user input
    author_name = input("Enter author's name: ").strip('"')  # Remove quotes from input
    magazine_name = input("Enter magazine name: ").strip('"')  # Remove quotes from input
    magazine_category = input("Enter magazine category: ").strip('"')  # Remove quotes from input
    article_title = input("Enter article title: ").strip('"')  # Remove quotes from input
    article_content = input("Enter article content: ")

    # Create an author
    author = Author(name=author_name)

    # Create a magazine
    magazine = Magazine(name=magazine_name, category=magazine_category)

    # Create an article
    article = Article(title=article_title, content=article_content, author_id=author.id, magazine_id=magazine.id)

    # Display results
    print("\nMagazines:")
    for magazine in Magazine.all():
        print(magazine)

    print("\nAuthors:")
    for author in Author.all():
        print(author)

    print("\nArticles:")
    for article in Article.all():
        print(article)

if __name__ == "__main__":
    main()
