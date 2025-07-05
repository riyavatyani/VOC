import cohere

co = cohere.Client("za40iksyiG7xrDtiCWXk1r5pzRlBZFuBGPnhCvIv")

def generate_recipe(ingredients):
    prompt = f"Create a recipe using the following ingredients: {', '.join(ingredients)}. Include the dish name, ingredients list, and step-by-step instructions."

    response = co.generate(
        model='command',  
        prompt=prompt,
        max_tokens=300,
        temperature=0.7
    )

    return response.generations[0].text.strip()

if __name__ == "__main__":
    user_input = input("Enter ingredients (comma-separated): ")
    ingredients = [i.strip() for i in user_input.split(",")]
    print("\nGenerating your recipe...\n")
    recipe = generate_recipe(ingredients)
    print(" Your recipe:\n")
    print(recipe)
