import sys
from query import query_documents

def main():
    print("=" * 70)
    print("Welcome to AI Bot - Ask Your Questions!")
    print("=" * 70)
    print("\nUsage:")
    print("  Option 1: python ask_bot.py 'Your question here'")
    print("  Option 2: Enter questions interactively below")
    print("=" * 70)
    
    # Check if question passed as argument
    if len(sys.argv) > 1:
        user_query = " ".join(sys.argv[1:])
        print(f"\nQuestion: {user_query}\n")
        response = query_documents(user_query, use_llm=False)
        print("=" * 70)
        print("ANSWER:")
        print("=" * 70)
        print(response)
        print("=" * 70)
    else:
        # Interactive mode
        try:
            while True:
                print("\n")
                user_query = input("Enter your question (or 'quit' to exit): ").strip()
                
                if user_query.lower() == 'quit':
                    print("Goodbye!")
                    break
                
                if not user_query:
                    print("Please enter a valid question.")
                    continue
                
                print("\nSearching documents...\n")
                response = query_documents(user_query, use_llm=False)
                
                print("=" * 70)
                print("ANSWER:")
                print("=" * 70)
                print(response)
                print("=" * 70)
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()

