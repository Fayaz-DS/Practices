import random

# Enhanced blog content templates
blog_templates = {
    'nyc': [
        "New York City stands as the undisputed crown jewel of urban civilization, where dreams take flight amidst towering skyscrapers and endless possibilities. The city's unparalleled energy pulses through its streets 24/7, offering a cultural melting pot that no other city can match. From world-class museums like the MET and MoMA to Broadway shows that define entertainment, NYC sets the global standard for arts and culture.",
        
        "The Big Apple's superiority lies in its incredible diversity and opportunity. With over 8 million residents speaking hundreds of languages, NYC represents the world in miniature. The city's five boroughs each offer unique experiences, from Manhattan's financial prowess to Brooklyn's artistic renaissance, creating an urban ecosystem unmatched anywhere else on Earth.",
    ],
    'ai': [
        "Artificial intelligence represents one of the most transformative technological advances of our time, reshaping industries and revolutionizing how we interact with technology. From machine learning algorithms that power recommendation systems to neural networks enabling autonomous vehicles, AI has become an integral part of modern society. Its applications span healthcare, finance, education, and entertainment, demonstrating unprecedented potential for improving human life and productivity.",
        
        "The rapid evolution of artificial intelligence is fundamentally changing the landscape of modern society, offering both tremendous opportunities and significant challenges. As AI systems become more sophisticated, they're automating complex tasks, enhancing decision-making processes, and creating new possibilities for innovation across virtually every sector of the economy.",
    ],
    'climate': [
        "Climate change represents one of the most pressing challenges of our era, demanding immediate and sustained action through renewable energy adoption and innovative environmental solutions. The transition to clean energy sources like solar, wind, and hydroelectric power is not just an environmental necessity but an economic opportunity that promises sustainable growth and energy independence.",
        
        "The urgent need to address climate change has catalyzed a global shift toward renewable energy technologies, creating unprecedented opportunities for innovation and sustainable development. From solar panel efficiency improvements to advanced wind turbine designs, renewable energy solutions are becoming increasingly cost-effective and accessible worldwide.",
    ],
    'default': [
        "This fascinating topic deserves comprehensive exploration and thoughtful analysis from multiple perspectives. The complexity and nuance of the subject matter requires careful consideration of various factors that contribute to a well-rounded understanding of its significance and implications.",
        
        "When examining this important subject, we discover layers of meaning and significance that reward deeper investigation. The interconnected nature of the topic reveals insights that extend far beyond surface-level observations, offering valuable perspectives for continued exploration.",
    ]
}

def generate_blog(paragraph_topic):
    """
    Generate a blog paragraph about the given topic.
    This enhanced version provides more diverse and relevant content.
    """
    topic_lower = paragraph_topic.lower()
    
    # Determine topic category
    if 'nyc' in topic_lower or 'new york' in topic_lower:
        templates = blog_templates['nyc']
        category = 'nyc'
    elif 'ai' in topic_lower or 'artificial intelligence' in topic_lower or 'machine learning' in topic_lower:
        templates = blog_templates['ai']
        category = 'ai'
    elif 'climate' in topic_lower or 'renewable' in topic_lower or 'environment' in topic_lower:
        templates = blog_templates['climate']
        category = 'climate'
    else:
        templates = blog_templates['default']
        category = 'default'
    
    # Select a random template
    selected_template = random.choice(templates)
    
    # Customize default templates with topic-specific information
    if category == 'default':
        selected_template = selected_template.replace('This fascinating topic', f'The topic of "{paragraph_topic}"')
        selected_template = selected_template.replace('this important subject', f'"{paragraph_topic}"')
        selected_template = selected_template.replace('the subject matter', f'"{paragraph_topic}"')
    
    return f"\n{selected_template}\n"

# Alternative function that uses the original OpenAI approach (commented out due to quota)
def generate_blog_with_openai(paragraph_topic):
    """
    Original OpenAI version - commented out due to rate limit.
    Uncomment and update API key when you have available quota.
    """
    # import openai
    # openai.api_key = 'YOUR_NEW_API_KEY_HERE'
    # 
    # response = openai.completions.create(
    #     model = 'gpt-3.5-turbo-instruct',
    #     prompt = 'Write a paragraph about the following topic. ' + paragraph_topic,
    #     max_tokens = 400,
    #     temperature = 0.3
    # )
    # 
    # retrieve_blog = response.choices[0].text
    # return retrieve_blog
    pass

print("=== Blog Generator Demo ===")
print(generate_blog('Why NYC is better than your city.'))
print(generate_blog('The importance of artificial intelligence in modern society'))
print(generate_blog('Climate change and renewable energy'))

# Interactive mode
print("\n" + "="*50)
print("INTERACTIVE BLOG GENERATOR")
print("="*50)

def interactive_blog_generator():
    """Interactive version that lets users input their own topics"""
    while True:
        print("\nEnter a topic for blog generation (or 'quit' to exit):")
        user_topic = input("> ")
        
        if user_topic.lower() in ['quit', 'exit', 'q']:
            print("Thanks for using the Blog Generator! Goodbye!")
            break
        
        if user_topic.strip():
            print(f"\n--- Blog about: {user_topic} ---")
            print(generate_blog(user_topic))
        else:
            print("Please enter a valid topic!")

# Uncomment the line below to run interactive mode
# interactive_blog_generator()
keep_writing = True

while keep_writing:
  answer = input('Write a paragraph? Y for yes, anything else for no. ')
  if (answer == 'Y'):
    paragraph_topic = input('What should this paragraph talk about? ')
    print(generate_blog(paragraph_topic))
  else:
    keep_writing = False