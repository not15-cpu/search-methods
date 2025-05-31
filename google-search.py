import webbrowser


def search_param(query):
    query = query.replace(" ", "+")
    url = f"https://google.com/search?q={query}"

    webbrowser.open(url)

query = input("Insira a query para a busca: ")
search_param(query)